
import React, { useState } from 'react';
import TerminologiaPanel from './TerminologiaPanel';

function Tabs() {
  const sistemas = ['CIE-O', 'SNOMED', 'CIE-11'];
  const [activeTab, setActiveTab] = useState('CIE-O');

  return (
    <div>
      <div style={{ display: 'flex' }}>
        {sistemas.map(s => (
          <button key={s} onClick={() => setActiveTab(s)} style={{ marginRight: '10px' }}>
            {s}
          </button>
        ))}
      </div>
      <TerminologiaPanel sistema={activeTab} />
    </div>
  );
}

export default Tabs;
