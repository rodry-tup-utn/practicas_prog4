import type { Categoria, CreateCategoria, UpdateCategoria, PaginatedCategoria, CategoriaFilters } from '../../types'

const BASE_URL = 'http://localhost:8000/categories'

export async function fetchCategories(filters?: CategoriaFilters): Promise<PaginatedCategoria> {
  const params = new URLSearchParams()
  if (filters?.name) params.set('name', filters.name)
  if (filters?.offset) params.set('offset', String(filters.offset))
  if (filters?.limit) params.set('limit', String(filters.limit))

  const url = params.toString() ? `${BASE_URL}/?${params}` : `${BASE_URL}/`
  const res = await fetch(url)
  if (!res.ok) throw new Error(`Error fetching categories: ${res.statusText}`)
  return res.json()
}

export async function fetchCategory(id: number): Promise<Categoria> {
  const res = await fetch(`${BASE_URL}/${id}`)
  if (!res.ok) throw new Error(`Error fetching category: ${res.statusText}`)
  return res.json()
}

export async function createCategory(data: CreateCategoria): Promise<Categoria> {
  const res = await fetch(`${BASE_URL}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error(`Error creating category: ${res.statusText}`)
  return res.json()
}

export async function updateCategory(id: number, data: UpdateCategoria): Promise<Categoria> {
  const res = await fetch(`${BASE_URL}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error(`Error updating category: ${res.statusText}`)
  return res.json()
}

export async function deleteCategory(id: number): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, { method: 'DELETE' })
  if (!res.ok) throw new Error(`Error deleting category: ${res.statusText}`)
}
