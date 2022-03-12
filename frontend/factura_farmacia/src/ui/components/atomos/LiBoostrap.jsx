import { Link, NavLink } from "react-router-dom";


// todo: terminar la navegacion

export const LiBoostrap = ({ estiloClassName, titulo }) => {
  return (
    <>
      <nav>
        {/* <NavLink
        className={({ isActivate }) =>
          "nav-item nav-link" + (isActivate ? "active" : "")
        }
        to="categoria"
      >{titulo}</NavLink> */}


        <li className={estiloClassName}>{titulo}</li> 
      </nav>
    </>
  );
};
