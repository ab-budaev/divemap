import { apiFetch } from './client'

export interface Spot {
  id: string
  name: string
  description: string | null
  lat: number
  lng: number
}

export function fetchSpots(): Promise<Spot[]> {
  return apiFetch<Spot[]>('/spots')
}
