import type { ComponentType } from 'react'

import { MapPinIcon, SlidersIcon, TankIcon } from './icons'
import { GearSection, MyPlacesSection, SettingsSection } from './placeholders'

export type SectionId = 'places' | 'gear' | 'settings'

export interface Section {
  title: string
  icon: ComponentType
  component: ComponentType
}

export const sections: Record<SectionId, Section> = {
  places: { title: 'Мои места', icon: MapPinIcon, component: MyPlacesSection },
  gear: { title: 'Мое снаряжение', icon: TankIcon, component: GearSection },
  settings: { title: 'Настройки', icon: SlidersIcon, component: SettingsSection },
}

export const sectionList: SectionId[] = ['places', 'gear', 'settings']
