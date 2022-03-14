import { useEffect, useState } from "react";
import { FormularioCategoria } from "../moleculas/FormularioCategoria";

import { apiCategorias } from "./ApiFactura";

export const CategoriaScreen = () => {
  const [categoria, setCategoria] = useState([]);

  const categorias = async () => {
    try {
      const res = await apiCategorias();
      const { Categoria } = await res.json();
      setCategoria(Categoria);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    categorias();
  }, []);

  const ingresoCategotia = (e, categoria) => {
    //e.preventDefault();
    console.log(categoria);
  };

  const event = (e) => {
    //e.preventDefault();
  };

  return (
    <div>
      <FormularioCategoria
        nombreCategoria={"Descripcion"}
        descripcion={"Descripcion"}
        categoria={categoria}
        submit={ingresoCategotia}
        event={event}
      />
    </div>
  );
};
