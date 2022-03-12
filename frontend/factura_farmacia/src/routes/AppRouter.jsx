import { BrowserRouter, Routes, Route } from "react-router-dom";

import { CategoriaScreen } from "../ui/components/pages/CategoriaScreen";
import { RegistroScreen } from "../ui/components/pages/RegistroScreen";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="registro" element={<RegistroScreen />} />
        <Route path="categoria" element={ <CategoriaScreen /> } />
      </Routes>
    </BrowserRouter>
  );
};
