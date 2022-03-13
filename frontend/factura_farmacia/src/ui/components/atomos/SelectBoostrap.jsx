export const SelectBoostrap = ({ categoria = [] }) => {
  console.log(categoria);
  return (
    <select className="form-select" aria-label="Default select example">
      {categoria.map((categoria) => (
        <option key={categoria.id} value={categoria.id}>
          {categoria.nombre}
        </option>
      ))}
    </select>
  );
};
