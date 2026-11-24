import { useState } from 'react'

import { sectionList, sections, type SectionId } from './sections'

interface SidebarProps {
  onSelect: (section: SectionId) => void
}

export function Sidebar({ onSelect }: SidebarProps) {
  const [expanded, setExpanded] = useState(false)

  return (
    <nav className={expanded ? 'sidebar sidebar--expanded' : 'sidebar'}>
      <ul className="sidebar-list">
        {sectionList.map((id) => {
          const { title, icon: Icon } = sections[id]
          return (
            <li key={id}>
              <button type="button" title={title} aria-label={title} onClick={() => onSelect(id)}>
                <Icon />
                <span className="sidebar-label">{title}</span>
              </button>
            </li>
          )
        })}
      </ul>
      <button
        type="button"
        className="sidebar-toggle"
        aria-label={expanded ? 'Свернуть меню' : 'Развернуть меню'}
        aria-expanded={expanded}
        onClick={() => setExpanded(!expanded)}
      >
        {expanded ? '←' : '→'}
      </button>
    </nav>
  )
}
