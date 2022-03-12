


export const InputBoostrap = ({ tituloSpan, estiloClassName, placeholder, type }) => {
  return (
    <div className="input-group">
      <span className="input-group-text">{tituloSpan}</span>
      <input type={type} aria-label="First name" className={estiloClassName} placeholder={placeholder}  />
    </div>
  )
}
