import { useEffect, useState } from 'react'

import { loadYMaps, type YMaps } from './ymaps'
import { demoSpots, type DemoSpot } from './spots'
import { SpotPanel } from './SpotPanel'
import { CreateSpotPanel } from './CreateSpotPanel'
import { Sidebar } from '../menu/Sidebar'
import { SectionPanel } from '../menu/SectionPanel'
import type { SectionId } from '../menu/sections'

type PanelState =
  | { kind: 'spot'; spot: DemoSpot }
  | { kind: 'create'; coordinates: [number, number] }
  | { kind: 'section'; section: SectionId }
  | null

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
              setPanel({ kind: 'create', coordinates: [event.coordinates[0], event.coordinates[1]] })
            }
          }}
        />
        <YMapControls position="right">
          <YMapZoomControl />
        </YMapControls>
        {demoSpots.map((spot) => (
          <YMapMarker key={spot.id} coordinates={spot.coordinates} onClick={() => setPanel({ kind: 'spot', spot })}>
            <div className="map-marker" />
          </YMapMarker>
        ))}
      </YMap>
      <Sidebar onSelect={(section) => setPanel({ kind: 'section', section })} />
      {panel?.kind === 'spot' && <SpotPanel spot={panel.spot} onClose={() => setPanel(null)} />}
      {panel?.kind === 'create' && <CreateSpotPanel coordinates={panel.coordinates} onClose={() => setPanel(null)} />}
      {panel?.kind === 'section' && <SectionPanel section={panel.section} onClose={() => setPanel(null)} />}
    </div>
  )
}
