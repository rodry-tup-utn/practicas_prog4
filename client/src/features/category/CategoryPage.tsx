import { useState, useEffect, useCallback } from "react";
import type { Categoria, CreateCategoria, UpdateCategoria } from "../../types";
import {
  fetchCategories,
  createCategory,
  updateCategory,
  deleteCategory,
} from "./api";
import { CategoryList } from "./CategoryList";
import { CategoryModal } from "./CategoryModal";

export function CategoryPage() {
  const [categories, setCategories] = useState<Categoria[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingCategory, setEditingCategory] = useState<Categoria | null>(
    null,
  );

  const loadCategories = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetchCategories();
      setCategories(res.items);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error al cargar categorías");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCategories();
  }, [loadCategories]);

  function handleOpenCreate() {
    setEditingCategory(null);
    setModalOpen(true);
  }

  function handleOpenEdit(cat: Categoria) {
    setEditingCategory(cat);
    setModalOpen(true);
  }

  function handleCloseModal() {
    setModalOpen(false);
    setEditingCategory(null);
  }

  async function handleSave(data: CreateCategoria | UpdateCategoria) {
    try {
      if (editingCategory) {
        await updateCategory(editingCategory.id, data as UpdateCategoria);
      } else {
        await createCategory(data as CreateCategoria);
      }
      handleCloseModal();
      await loadCategories();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error al guardar categoría");
    }
  }

  async function handleDelete(id: number) {
    if (!window.confirm("¿Eliminar esta categoría?")) return;
    try {
      await deleteCategory(id);
      await loadCategories();
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error al eliminar categoría");
    }
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold">Categorías</h1>
        <button
          onClick={handleOpenCreate}
          className="bg-blue-600 text-white p-2 rounded-3xl hover:bg-blue-700 cursor-pointer"
        >
          + Nueva categoría
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 rounded mb-4">
          {error}
        </div>
      )}

      <CategoryList
        categories={categories}
        loading={loading}
        onEdit={handleOpenEdit}
        onDelete={handleDelete}
      />

      <CategoryModal
        isOpen={modalOpen}
        category={editingCategory}
        onClose={handleCloseModal}
        onSave={handleSave}
      />
    </div>
  );
}
