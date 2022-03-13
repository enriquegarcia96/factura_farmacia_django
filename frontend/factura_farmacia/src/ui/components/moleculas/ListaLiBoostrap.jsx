import { LiBoostrap } from "../atomos/LiBoostrap";

export const ListaLiBoostrap = () => {
  return (
    <div className="col-6">
      <ul className="list-group mt-6">
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Resgistro de clientes"}
          to={"/registro"}
        />
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Registro de categorias"}
          to={"/categoria"}
        />
        <LiBoostrap
          estiloClassName={"list-group-item"}
          titulo={"Facturacion"}
          to={"/factura"}
        />
      </ul>
    </div>
  );
};
