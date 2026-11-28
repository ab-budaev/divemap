const API_BASE: string = import.meta.env.VITE_API_BASE ?? '/api'

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, init)
  if (!response.ok) {
    throw new Error(`API request failed: ${response.status} ${response.statusText}`)
  }
  return response.json() as Promise<T>
}
