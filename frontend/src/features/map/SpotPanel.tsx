import type { Spot } from '../../api/spots'

interface SpotPanelProps {
  spot: Spot
  onClose: () => void
}

export function SpotPanel({ spot, onClose }: SpotPanelProps) {
  return (
    <aside className="map-panel">
      <header className="map-panel-header">
        <h2>{spot.name}</h2>
        <button type="button" onClick={onClose} aria-label="Закрыть">
          ×
        </button>
      </header>
      {spot.description && <p>{spot.description}</p>}
    </aside>
  )
}
