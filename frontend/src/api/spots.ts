import { apiFetch } from './client'

export interface Spot {
  id: string
  name: string
  description: string | null
  lat: number
  lng: number
}

export interface SpotCreatePayload {
  name: string
  description: string | null
  lat: number
  lng: number
}

export function fetchSpots(): Promise<Spot[]> {
  return apiFetch<Spot[]>('/spots')
}

export function createSpot(payload: SpotCreatePayload): Promise<Spot> {
  return apiFetch<Spot>('/spots', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
}
