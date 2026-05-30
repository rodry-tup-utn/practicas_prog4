import type { Categoria } from "../../types";

interface CategoryListProps {
  categories: Categoria[];
  loading: boolean;
  onEdit: (cat: Categoria) => void;
  onDelete: (id: number) => void;
}

export function CategoryList({
  categories,
  loading,
  onEdit,
  onDelete,
}: CategoryListProps) {
  if (loading) {
    return <p className="text-gray-500">Cargando...</p>;
  }

  if (categories.length === 0) {
    return <p className="text-gray-500">No hay categorías registradas.</p>;
  }

  return (
    <div className="overflow-x-auto rounded-lg border border-gray-200 overflow-hidden">
      <table className="w-full table-auto">
        <thead>
          <tr className="bg-gray-100 text-gray-600 uppercase text-sm leading-normal">
            <th className="text-right px-4 py-2">Nombre</th>
            <th className="text-center px-4 py-2">Descripción</th>
            <th className="text-center px-4 py-2">Acciones</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm">
          {categories.map((cat) => (
            <tr
              key={cat.id}
              className="border-b border-gray-300 hover:bg-gray-100"
            >
              <td className="px-4 py-2">{cat.name}</td>
              <td className="px-4 py-2 text-gray-700">
                {cat.description || "—"}
              </td>
              <td className="px-4 py-2 text-right">
                <div className="flex justify-around">
                  <button
                    onClick={() => onEdit(cat)}
                    className="bg-blue-600 text-white font-bold tracking-tight rounded-2xl py-2 px-4 cursor-pointer hover:bg-blue-800 "
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => onDelete(cat.id)}
                    className="bg-red-600 text-white font-bold tracking-tight rounded-2xl py-2 px-4 cursor-pointer hover:bg-red-800 "
                  >
                    Eliminar
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
