import { LiBoostrap } from "../atomos/LiBoostrap";

export const ListaLiBoostrap = () => {
  return (
    <div className="col-6">
      <ul className="list-group mt-6">
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Ingreso de Categorias"}
        />
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Ingreso de Categorias"}
        />
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Ingreso de Categorias"}
        />
      </ul>
    </div>
  );
};
