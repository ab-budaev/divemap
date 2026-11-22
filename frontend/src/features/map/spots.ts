export interface DemoSpot {
  id: number
  name: string
  description?: string
  coordinates: [number, number]
}

export const demoSpots: DemoSpot[] = [
  {
    id: 1,
    name: 'Байкал, Листвянка',
    description: 'Ледовые погружения, прозрачность до 40 метров.',
    coordinates: [104.8722, 51.8461],
  },
  {
    id: 2,
    name: 'Шарм-эль-Шейх, Рас Умм Сид',
    description: 'Коралловая стенка, круглый год тёплая вода.',
    coordinates: [34.2974, 27.8667],
  },
  {
    id: 3,
    name: 'Голубая дыра',
    description: 'Знаменитый карстовый провал у барьерного рифа Белиза.',
    coordinates: [-87.5351, 17.3156],
  },
]
