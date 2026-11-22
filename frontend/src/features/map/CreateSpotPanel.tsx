interface CreateSpotPanelProps {
  coordinates: [number, number]
  onClose: () => void
}

export function CreateSpotPanel({ coordinates, onClose }: CreateSpotPanelProps) {
  const [lng, lat] = coordinates

  return (
    <aside className="map-panel">
      <header className="map-panel-header">
        <h2>Новое место</h2>
        <button type="button" onClick={onClose} aria-label="Закрыть">
          ×
        </button>
      </header>
      <p>
        Координаты: {lat.toFixed(5)}, {lng.toFixed(5)}
      </p>
      <p>Форма создания места появится в этапе «Карта + Spot».</p>
    </aside>
  )
}
