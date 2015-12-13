CREATE TABLE departamentos (
  id SERIAL PRIMARY KEY,
  codigo INTEGER NOT NULL,
  nombre TEXT NOT NULL
);

CREATE UNIQUE INDEX ui_departamentos_nombre ON departamentos (lower(nombre));
CREATE UNIQUE INDEX ui_departamentos_codigo ON departamentos (codigo);

CREATE TABLE municipios (
  id SERIAL PRIMARY KEY,
  departamento_id INTEGER NOT NULL REFERENCES departamentos (id),
  codigo INTEGER NOT NULL,
  nombre TEXT NOT NULL
);

CREATE UNIQUE INDEX ui_municipios_nombre ON municipios (departamento_id, lower(nombre));
CREATE UNIQUE INDEX ui_municipios_codigo ON municipios (departamento_id, codigo);
