
-- Tabla principal: Terminologías Unificadas (TAU)
CREATE SCHEMA tau;

CREATE TABLE IF NOT EXISTS tau.terminologias (
    id SERIAL PRIMARY KEY,
    sistema VARCHAR(50), -- Ej: CIE-O, SNOMED, CIE-11
    codigo VARCHAR(50),
    termino_preferido TEXT,
    sinonimos TEXT,
    definicion TEXT,
    traduccion_termino TEXT,
    traduccion_sinonimos TEXT,
    traduccion_definicion TEXT,
    fuente TEXT,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: Relaciones entre códigos de diferentes sistemas
CREATE TABLE IF NOT EXISTS tau.relaciones_equivalentes (
    id SERIAL PRIMARY KEY,
    codigo_origen VARCHAR(50),
    sistema_origen VARCHAR(50),
    codigo_destino VARCHAR(50),
    sistema_destino VARCHAR(50),
    tipo_equivalencia VARCHAR(50), -- Ej: exacto, amplio, estrecho, relacionado
    descripcion TEXT,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
