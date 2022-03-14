import { useEffect, useState } from "react";
import { InputBoostrap } from "../atomos/InputBootstrap";
import { TablaDetalle } from "./TablaDetalle";

export const FormularioFactura = ({ productos = [] }) => {
  const [id, setId] = useState("");
  const [datosDelProducto, setDatosDelProducto] = useState({});
  const [cantidad, setCantidad] = useState(0);

  const handleSubmit = (productoSeleccionado) => {
    console.log(productoSeleccionado);
  };

  const agregar = () => {
    console.log("Hlaa omar");
  };
  const capturaType = (e) => {
    setId(e.target.value);
  };

  useEffect(() => {
    const pre = productos.filter(
      (producto) => producto.categoria_categoria_id_id == id
    );

    setDatosDelProducto(Object.assign({}, pre[0]));
  }, [id, productos, setDatosDelProducto]);

  console.log(datosDelProducto.precio_venta);

  return (
    <>
      <form>
        <fieldset>
          <legend>Compra</legend>
          <div className="mb-3">
            <select
              className="form-select"
              aria-label="Default select example"
              onChange={capturaType}
            >
              {productos.map(
                ({ id, categoria_categoria_id_id, nombre_producto }) => (
                  <option key={id} value={categoria_categoria_id_id}>
                    {nombre_producto}
                  </option>
                )
              )}
            </select>
          </div>

          {/* {id === productos.filter( producto => producto.categoria_categoria_id_id === id )
          ? productos.map(({ precio_venta }) => (
              <div className="mb-3">
                <InputBoostrap
                  type={"text"}
                  tituloSpan={"Precio"}
                  estiloClassName="form-control"
                  placeholder={precio_venta}
                />
              </div>
            ))
          : ""} */}

          <div className="mb-3">
            <InputBoostrap
              type={"text"}
              tituloSpan={"Precio"}
              estiloClassName="form-control"
              placeholder={datosDelProducto.precio_venta}
              value={datosDelProducto.precio_venta}
              disabled={true}
            />
          </div>

          <div className="input-group">
            <span className="input-group-text">Cantidad</span>

            <input
              type="number"
              className="form-control"
              value={cantidad}
              onChange={(e) => setCantidad(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <InputBoostrap
              tituloSpan={"Numero de Identidad"}
              type={"text"}
              estiloClassName={"form-control"}
              placeholder={"0209200089765"}
              value={0}
            />
          </div>

          <button type="button" className="btn btn-primary" onClick={agregar}>
            Agregar
          </button>
        </fieldset>
      </form>

      <TablaDetalle />
    </>
  );
};
