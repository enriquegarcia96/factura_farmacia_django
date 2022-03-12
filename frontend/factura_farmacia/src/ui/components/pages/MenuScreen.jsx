import { AppRouter } from "../../../routes/AppRouter";
import { ListaLiBoostrap } from "../moleculas/ListaLiBoostrap";


export const MenuScreen = () => {
  return (
    <div className="row container mt-4 animate__animated animate__fadeInDown">
      <div className="col-6">
        <h2>Busquedas</h2>
        <hr />
        <ListaLiBoostrap />
      </div>

        {/* para las navegacion del menu */}
        <div className="col" >
          <AppRouter /> 
        </div>
    </div>
  );
};
