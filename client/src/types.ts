export interface Categoria {
  id: number
  name: string
  description: string | null
}

export interface CreateCategoria {
  name: string
  description?: string | null
}

export interface UpdateCategoria {
  name?: string | null
  description?: string | null
}

export interface CategoriaFilters {
  name?: string
  offset?: number
  limit?: number
}

export interface PaginatedCategoria {
  items: Categoria[]
  total: number
}

export interface Producto {
  id: number
  name: string
  description: string | null
  base_price: number
  image_url: string[] | null
  active: boolean
  categories: Categoria[]
}

export interface CreateProducto {
  name: string
  description?: string | null
  base_price: number
  image_url?: string[] | null
  category_ids?: number[]
}

export interface UpdateProducto {
  name?: string | null
  description?: string | null
  base_price?: number | null
  active?: boolean | null
}

export interface ProductoFilters {
  name?: string
  min_price?: number
  max_price?: number
  active?: boolean
  category_id?: number
  offset?: number
  limit?: number
}

export interface PaginatedProducto {
  items: Producto[]
  total: number
}
