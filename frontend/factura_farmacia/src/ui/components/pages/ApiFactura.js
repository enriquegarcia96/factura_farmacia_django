const API = "http://127.0.0.1:8000/api";



export const ApiFactura = async () => {
  return await fetch(API);
};

export const apiCategorias = async () => {
  return await fetch(`${API}/categoria`);
};

export const apiProductos = async() =>{
  return await fetch(`${API}/producto`)
}