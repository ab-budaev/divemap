import { useEffect, useMemo, useRef, useState, type ChangeEvent } from 'react'

const MAX_PHOTOS = 10

interface PhotoPickerProps {
  photos: File[]
  onChange: (photos: File[]) => void
}

export function PhotoPicker({ photos, onChange }: PhotoPickerProps) {
  const [limitMessage, setLimitMessage] = useState<string | null>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const previews = useMemo(() => photos.map((file) => ({ file, url: URL.createObjectURL(file) })), [photos])

  useEffect(() => () => previews.forEach(({ url }) => URL.revokeObjectURL(url)), [previews])

  const handleSelect = (event: ChangeEvent<HTMLInputElement>) => {
    const selected = Array.from(event.target.files ?? [])
    event.target.value = ''
    const accepted = selected.slice(0, Math.max(0, MAX_PHOTOS - photos.length))
    setLimitMessage(accepted.length < selected.length ? `Можно загрузить не более ${MAX_PHOTOS} фотографий` : null)
    if (accepted.length > 0) {
      onChange([...photos, ...accepted])
    }
  }

  const handleRemove = (index: number) => {
    setLimitMessage(null)
    onChange(photos.filter((_, i) => i !== index))
  }

  return (
    <div className="photo-picker">
      <span className="modal-field-label">Фотографии</span>
      <input ref={inputRef} type="file" multiple accept="image/*" onChange={handleSelect} hidden />
      <button type="button" onClick={() => inputRef.current?.click()}>
        Выбрать фото
      </button>
      {limitMessage && (
        <p className="photo-picker-message" role="alert">
          {limitMessage}
        </p>
      )}
      {previews.length > 0 && (
        <ul className="photo-picker-previews">
          {previews.map(({ file, url }, index) => (
            <li key={url}>
              <img src={url} alt={file.name} />
              <button type="button" onClick={() => handleRemove(index)} aria-label={`Удалить ${file.name}`}>
                ×
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
