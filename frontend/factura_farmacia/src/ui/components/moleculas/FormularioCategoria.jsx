import { InputBoostrap } from "../atomos/InputBootstrap";
import { SelectBoostrap } from "../atomos/SelectBoostrap";

export const FormularioCategoria = ({
  nombreCategoria,
  descripcion,
  categoria,
  event,
}) => {
  return (
    <form>
      <fieldset>
        <legend>Disabled fieldset example</legend>
        <div className="mb-3">
          <SelectBoostrap categoria={categoria} />
        </div>
        <div className="mb-3">
          <InputBoostrap
            tituloSpan={descripcion}
            type={"text"}
            estiloClassName="form-control"
            placeholder={"Panadol"}
          />
        </div>
      </fieldset>

      <button type="submit" onClick={event} className="btn btn-primary">
        Primary
      </button>
    </form>
  );
};
