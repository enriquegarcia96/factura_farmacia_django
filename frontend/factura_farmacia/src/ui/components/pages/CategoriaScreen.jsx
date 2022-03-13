import { useEffect, useState } from "react";
import { FormularioCategoriaScreen } from "../moleculas/FormularioCategoriaScreen";
import { apiCategorias } from "./ApiFactura";

export const CategoriaScreen = () => {
  const [categoria, setCategoria] = useState([]);
  const [descripcion2, setDescripcion] = useState();

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

  //TODO: hacer la inserccion de categoria

  const handleButton = (e) => {
    e.preventDefault();
    console.log(categoria);
  };

  return (
    <div>
      <FormularioCategoriaScreen
        nombreCategoria={"Descripcion"}
        descripcion={"Descripcion"}
        categoria={categoria}
        event={handleButton}
      />
    </div>
  );
};
