import React, {useState, useEffect} from 'react';

const PreguntaExtra = () => {
  const [texto, setTexto] = useState("");
  const [textoOuput, setTextoOuput] = useState('');

  //limitar input para que solo se puedan introducir 100 caracteres
  const handleInputChange=(e)=> {
    const inputText = e.target.value;
    setTexto(inputText);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const urls = texto.match(/https?:\/\/[^\s]+/g);
    const path = urls.map(url => url.split("/")[2].replace(/^(www\.|ww2\.)/, ''))
    //const quitarWWW = path.map(palabra => palabra.replace('www.', ''));
    setTextoOuput(path)
  }
  
  return (
    <div onSubmit={(e)=>handleSubmit(e)}className="PreguntaExtra flex flex-j-c flex-a-i flex-f-d-c">
      <h1>Pregunta Extra</h1>
      <form  className='flex flex-j-c flex-a-i flex-f-d-c'>
        <ul>
          <li className='flex'>
            <label for="name">fragmento de marcado HTML:</label>
            <input onChange={handleInputChange} type="text" />
          </li>
        </ul>
        <button>Obtener Dominio</button>
      </form>
      <h2>Dominio</h2>
      <p>{textoOuput==null?'soy null':textoOuput }</p>
    </div>
    );
  }
  
export default PreguntaExtra;