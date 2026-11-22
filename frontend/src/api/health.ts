import { apiFetch } from './client'

export interface HealthStatus {
  status: string
}

export function fetchHealth(): Promise<HealthStatus> {
  return apiFetch<HealthStatus>('/health')
}
