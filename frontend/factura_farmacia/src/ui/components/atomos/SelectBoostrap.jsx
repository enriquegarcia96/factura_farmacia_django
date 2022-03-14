import { useState } from "react";

export const SelectBoostrap = ({ categoria = [], submit }) => {
  const [categoriaSeleccionada, setCategoriaSeleccionada] = useState("");

  submit(categoriaSeleccionada);

  return (
    <select className="form-select" aria-label="Default select example">
      {categoria.map((categoria) => (
        <option
          key={categoria.id}
          onChange={setCategoriaSeleccionada}
          value={categoriaSeleccionada}
        >
          {categoria.nombre}
        </option>
      ))}
    </select>
  );
};
