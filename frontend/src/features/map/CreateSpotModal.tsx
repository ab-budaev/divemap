import { useEffect, useState, type FormEvent } from 'react'

import { PhotoPicker } from './PhotoPicker'

export interface SpotDraft {
  name: string
  description: string
  coordinates: [number, number]
  photos: File[]
}

interface CreateSpotModalProps {
  coordinates: [number, number]
  onSubmit: (draft: SpotDraft) => void
  onClose: () => void
}

export function CreateSpotModal({ coordinates, onSubmit, onClose }: CreateSpotModalProps) {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [photos, setPhotos] = useState<File[]>([])
  const [lng, lat] = coordinates

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose()
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [onClose])

  const handleSubmit = (event: FormEvent) => {
    event.preventDefault()
    onSubmit({ name: name.trim(), description, coordinates, photos })
  }

  return (
    <div className="modal-backdrop">
      <div className="modal" role="dialog" aria-modal="true" aria-labelledby="create-spot-title">
        <header className="map-panel-header">
          <h2 id="create-spot-title">Новое место</h2>
          <button type="button" onClick={onClose} aria-label="Закрыть">
            ×
          </button>
        </header>
        <form className="modal-form" onSubmit={handleSubmit}>
          <label className="modal-field">
            Наименование
            <input type="text" value={name} onChange={(event) => setName(event.target.value)} autoFocus />
          </label>
          <p className="modal-coordinates">
            Координаты: {lat.toFixed(5)}, {lng.toFixed(5)}
          </p>
          <label className="modal-field">
            Описание
            <textarea value={description} onChange={(event) => setDescription(event.target.value)} rows={4} />
          </label>
          <PhotoPicker photos={photos} onChange={setPhotos} />
          <footer className="modal-actions">
            <button type="button" onClick={onClose}>
              Отмена
            </button>
            <button type="submit" disabled={!name.trim()}>
              Сохранить
            </button>
          </footer>
        </form>
      </div>
    </div>
  )
}
