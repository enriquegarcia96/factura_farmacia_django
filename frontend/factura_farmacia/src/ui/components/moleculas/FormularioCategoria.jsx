import { InputBoostrap } from "../atomos/InputBootstrap";
import { SelectBoostrap } from "../atomos/SelectBoostrap";

export const FormularioCategoria = ({
  nombreCategoria,
  descripcion,
  categoria,
  submit,
  event,
}) => {
  return (
    <form>
      <fieldset>
        <legend>Ingreso de categoria</legend>
        <div className="mb-3">
          <SelectBoostrap categoria={categoria} submit={submit} />
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

      <button type="submit" onClick={submit} className="btn btn-primary">
        Primary
      </button>
    </form>
  );
};
