import React, {useState, useEffect} from 'react';
import { GiWorld } from 'react-icons/gi';

const NuevoOrdenMundial = () => {
  const [texto, setTexto] = useState("");
  const [textoOuput, setTextoOuput] = useState('');
  const [pruebaTecnica, setPruebaTecnica] = useState(1)

  //limitar input para que solo se puedan introducir 100 caracteres
  const handleInputChange=(e)=> {
    const inputText = e.target.value;
    if (inputText.length <= 100) {
      setTexto(inputText);
    }
  }

  const handleSubmit = (e) =>{
    e.preventDefault()
    let Texto = texto.split("").sort()
    //adquirir minuscula del array y ordenarlos en orden numerico
    let minusculas = Texto.filter(letra => letra >= 'a' && letra <= 'z').join("")
    //adquirir mayusculas del array y ordenarlos en orden numerico
    let mayusculas = Texto.filter(letra => letra >= 'A' && letra <= 'Z').join("")
    //adquirir numeros del array
    let numeros = Texto.filter(elemento => !isNaN(elemento))
    let pares = numeros.filter(elemento => elemento % 2 === 0).join("")
    let impares = numeros.filter(elemento => elemento % 2 !== 0).join("")
    setTextoOuput(`${minusculas}${mayusculas}${impares}${pares}`)
  }

  return (
    <div onSubmit={(e)=>handleSubmit(e)} className="NuevoOrdenMundial flex flex-j-c flex-a-i flex-f-d-c">
      <h1 className='NuevoOrdenMundial__title'>Nuevo Orden Mundial <GiWorld/></h1>
      <form className='flex flex-j-c flex-a-i flex-f-d-c'>
        <ul>
          <li className='flex flex-f-d-c'>
            <label for="name">S:</label>
            <input onChange={handleInputChange} type="text" maxLength="100" className='inputStyle' />
          </li>
        </ul>
        <button className='btn'>Ordenar</button>
      </form>
      <h2>Salida de la cadena ordenada S</h2>
      <p>{textoOuput}</p>
    </div>
    );
  }
  
export default NuevoOrdenMundial;