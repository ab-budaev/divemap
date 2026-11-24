import { sections, type SectionId } from './sections'

interface SectionPanelProps {
  section: SectionId
  onClose: () => void
}

export function SectionPanel({ section, onClose }: SectionPanelProps) {
  const { title, component: Content } = sections[section]

  return (
    <aside className="map-panel">
      <header className="map-panel-header">
        <h2>{title}</h2>
        <button type="button" onClick={onClose} aria-label="Закрыть">
          ×
        </button>
      </header>
      <Content />
    </aside>
  )
}
