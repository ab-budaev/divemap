import * as React from 'react'
import * as ReactDOM from 'react-dom'

const apiKey: string | undefined = import.meta.env.VITE_YANDEX_MAPS_API_KEY

function loadApiScript(): Promise<void> {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.src = `https://api-maps.yandex.ru/v3/?apikey=${apiKey}&lang=ru_RU`
    script.onload = () => resolve()
    script.onerror = () => reject(new Error('сервер карт недоступен'))
    document.head.appendChild(script)
  })
}

async function createYMaps() {
  if (!apiKey) {
    throw new Error('не задан ключ VITE_YANDEX_MAPS_API_KEY')
  }
  await loadApiScript()
  const [ymaps3React, ymaps3Controls] = await Promise.all([
    ymaps3.import('@yandex/ymaps3-reactify'),
    ymaps3.import('@yandex/ymaps3-controls@0.0.1'),
    ymaps3.ready,
  ])
  const reactify = ymaps3React.reactify.bindTo(React, ReactDOM)
  return { ...reactify.module(ymaps3), ...reactify.module(ymaps3Controls) }
}

export type YMaps = Awaited<ReturnType<typeof createYMaps>>

let ymapsPromise: Promise<YMaps> | null = null

export function loadYMaps(): Promise<YMaps> {
  ymapsPromise ??= createYMaps().catch((error: unknown) => {
    const reason = error instanceof Error ? error.message : 'неизвестная ошибка'
    throw new Error(`Не удалось загрузить Яндекс.Карты: ${reason}`)
  })
  return ymapsPromise
}
