import { InputBoostrap } from "../atomos/InputBootstrap";
import { SelectBoostrap } from "../atomos/SelectBoostrap";

export const FormularioRegistro = () => {
  return (
    <form>
      <fieldset>
        <legend>Disabled fieldset example</legend>
        <div className="mb-3">
          <InputBoostrap
            tituloSpan={"Nombre"}
            type={"text"}
            estiloClassName="form-control"
            placeholder={"Enrique"}
          />
        </div>
        <div className="mb-3">
          <InputBoostrap
            type={"text"}
            tituloSpan={"Apellido"}
            estiloClassName="form-control"
            placeholder={"García"}
          />
        </div>

        <div className="mb-3">
          <InputBoostrap
            estiloClassName={"form-control"}
            type={"text"}
            tituloSpan={"Direccion"}
            placeholder={"Barrio las flores"}
          />
        </div>

        <div className="mb-3">
          <InputBoostrap
            estiloClassName={"form-control"}
            type={"text"}
            tituloSpan={"Telefono"}
            placeholder={"98782211"}
          />
        </div>

        <div className="mb-3">
          <InputBoostrap
            tituloSpan={"Numero de Identidad"}
            type={"text"}
            estiloClassName={"form-control"}
            placeholder={"0209200089765"}
          />
        </div>

        {/* <div className="mb-3">
          <SelectBoostrap />
        </div> */}
      </fieldset>
    </form>
  );
};
