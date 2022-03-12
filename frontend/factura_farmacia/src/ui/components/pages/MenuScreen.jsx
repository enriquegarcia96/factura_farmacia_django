import { ListaLiBoostrap } from "../moleculas/ListaLiBoostrap";

export const MenuScreen = () => {
  return (
    <div className="row container mt-6 animate__animated animate__fadeInDown">
      <div class="col-6">
        <h2>Busquedas</h2>
        <hr />
        <ListaLiBoostrap />

        {/* Todo poner el router  */}
      </div>
    </div>
  );
};
