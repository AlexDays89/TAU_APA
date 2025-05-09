
import React, { useState } from 'react';

function FloaterEditor({ data, onClose }) {
  const [traduccion, setTraduccion] = useState(data.termino_preferido);
  const [sinonimos, setSinonimos] = useState('');

  const handleGuardar = () => {
    alert('Guardado: ' + traduccion + ' | Sinónimos: ' + sinonimos);
    onClose();
  };

  return (
    <div style={{
      position: 'fixed',
      top: '100px',
      right: '50px',
      backgroundColor: 'white',
      border: '1px solid #ccc',
      padding: '20px',
      zIndex: 1000
    }}>
      <h3>Editar {data.sistema}</h3>
      <p><b>Código:</b> {data.codigo}</p>
      <p><b>Ruta árbol (simulada):</b> Neoplasias → Malignas → Carcinoma</p>
      <div>
        <label>Traducción término:</label><br />
        <input value={traduccion} onChange={e => setTraduccion(e.target.value)} /><br />
        <label>Sinónimos (separados por ;):</label><br />
        <input value={sinonimos} onChange={e => setSinonimos(e.target.value)} /><br /><br />
        <button onClick={handleGuardar}>Guardar</button>
        <button onClick={onClose} style={{ marginLeft: '10px' }}>Cerrar</button>
      </div>
    </div>
  );
}

export default FloaterEditor;
