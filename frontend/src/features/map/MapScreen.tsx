import { useEffect, useState } from 'react'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'

import { loadYMaps, type YMaps } from './ymaps'
import { createSpot, fetchSpots, type Spot } from '../../api/spots'
import { SpotPanel } from './SpotPanel'
import { CreateSpotModal, type SpotDraft } from './CreateSpotModal'
import { Sidebar } from '../menu/Sidebar'
import { SectionPanel } from '../menu/SectionPanel'
import type { SectionId } from '../menu/sections'

type PanelState = { kind: 'spot'; spot: Spot } | { kind: 'section'; section: SectionId } | null

export default function MapScreen() {
  const [maps, setMaps] = useState<YMaps | null>(null)
  const [loadError, setLoadError] = useState<string | null>(null)

  useEffect(() => {
    loadYMaps().then(setMaps, (error: Error) => setLoadError(error.message))
  }, [])

  if (loadError) {
    return (
      <main className="map-message">
        <h1>divemap</h1>
        <p>{loadError}</p>
        <p>Проверьте ключ VITE_YANDEX_MAPS_API_KEY в frontend/.env и перезапустите dev-сервер.</p>
      </main>
    )
  }

  if (!maps) {
    return (
      <main className="map-message">
        <p>Загружаем карту…</p>
      </main>
    )
  }

  return <MapView maps={maps} />
}

function MapView({ maps }: { maps: YMaps }) {
  const [panel, setPanel] = useState<PanelState>(null)
  const [createDraft, setCreateDraft] = useState<{ coordinates: [number, number] } | null>(null)
  const queryClient = useQueryClient()
  const { data: spots, isError, refetch } = useQuery({ queryKey: ['spots'], queryFn: fetchSpots })
  const createSpotMutation = useMutation({
    mutationFn: createSpot,
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: ['spots'] })
      setCreateDraft(null)
    },
  })

  const handleCreateSubmit = (draft: SpotDraft) => {
    createSpotMutation.mutate({
      name: draft.name,
      description: draft.description.trim() ? draft.description.trim() : null,
      lat: draft.coordinates[1],
      lng: draft.coordinates[0],
    })
  }
  const { YMap, YMapDefaultSchemeLayer, YMapDefaultFeaturesLayer, YMapListener, YMapControls, YMapMarker, YMapZoomControl } =
    maps

  return (
    <div className="map-screen">
      <YMap location={{ center: [45, 40], zoom: 3 }}>
        <YMapDefaultSchemeLayer />
        <YMapDefaultFeaturesLayer />
        <YMapListener
          onClick={(object, event) => {
            if (!object) {
              setPanel(null)
              setCreateDraft({ coordinates: [event.coordinates[0], event.coordinates[1]] })
            }
          }}
        />
        <YMapControls position="right">
          <YMapZoomControl />
        </YMapControls>
        {(spots ?? []).map((spot) => (
          <YMapMarker
            key={spot.id}
            coordinates={[spot.lng, spot.lat]}
            onClick={() => {
              setCreateDraft(null)
              setPanel({ kind: 'spot', spot })
            }}
          >
            <div className="map-marker" />
          </YMapMarker>
        ))}
        {createDraft && (
          <YMapMarker coordinates={createDraft.coordinates}>
            <div className="map-marker map-marker--draft" />
          </YMapMarker>
        )}
      </YMap>
      <Sidebar
        onSelect={(section) => {
          setCreateDraft(null)
          setPanel({ kind: 'section', section })
        }}
      />
      {isError && (
        <div className="map-error" role="alert">
          <span>Не удалось загрузить места погружений.</span>
          <button type="button" onClick={() => void refetch()}>
            Повторить
          </button>
        </div>
      )}
      {panel?.kind === 'spot' && <SpotPanel spot={panel.spot} onClose={() => setPanel(null)} />}
      {panel?.kind === 'section' && <SectionPanel section={panel.section} onClose={() => setPanel(null)} />}
      {createDraft && (
        <CreateSpotModal
          coordinates={createDraft.coordinates}
          isSubmitting={createSpotMutation.isPending}
          submitError={createSpotMutation.isError ? 'Не удалось сохранить место. Попробуйте ещё раз.' : null}
          onSubmit={handleCreateSubmit}
          onClose={() => setCreateDraft(null)}
        />
      )}
    </div>
  )
}
