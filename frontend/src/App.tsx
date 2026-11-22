import { useQuery } from '@tanstack/react-query'

import { fetchHealth } from './api/health'

export default function App() {
  const health = useQuery({ queryKey: ['health'], queryFn: fetchHealth })

  return (
    <main className="app">
      <h1>divemap</h1>
      {health.isPending && <p>Проверяем связь с сервером…</p>}
      {health.isError && <p>Сервер недоступен</p>}
      {health.isSuccess && <p>Сервер отвечает: {health.data.status}</p>}
    </main>
  )
}
