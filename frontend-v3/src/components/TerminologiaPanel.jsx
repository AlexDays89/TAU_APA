
import React, { useState } from 'react';
import FloaterEditor from './FloaterEditor';

function TerminologiaPanel({ sistema }) {
  const [showEditor, setShowEditor] = useState(false);
  const [data, setData] = useState({
    codigo: '8500/3',
    termino_preferido: 'Carcinoma ductal infiltrante',
    sinonimos: '',
    definicion: 'Tumor maligno de los conductos',
    sistema
  });

  const handleEdit = () => {
    setShowEditor(true);
  };

  return (
    <div>
      <h2>{sistema}</h2>
      <p><b>Código:</b> {data.codigo}</p>
      <p><b>Término:</b> {data.termino_preferido}</p>
      <button onClick={handleEdit}>Revisar / Editar</button>
      {showEditor && <FloaterEditor data={data} onClose={() => setShowEditor(false)} />}
    </div>
  );
}

export default TerminologiaPanel;
