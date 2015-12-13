CREATE TABLE regiones (
  id SERIAL PRIMARY KEY,
  codigo TEXT NOT NULL,
  nombre TEXT NOT NULL
);

CREATE UNIQUE INDEX ui_regiones_nombre ON regiones (lower(nombre));
CREATE UNIQUE INDEX ui_regiones_codigo ON regiones (lower(codigo));

DROP INDEX ui_departamentos_nombre;
DROP INDEX ui_departamentos_codigo;
DROP INDEX ui_municipios_nombre;
DROP INDEX ui_municipios_codigo;

ALTER TABLE departamentos ADD COLUMN region_id INTEGER NOT NULL;
ALTER TABLE departamentos ADD CONSTRAINT departamentos_region_id_fkey FOREIGN KEY (region_id) REFERENCES regiones(id);

CREATE UNIQUE INDEX departamentos_region_id_nombre_key ON departamentos (region_id, lower(nombre));
CREATE UNIQUE INDEX departamentos_region_id_codigo_key ON departamentos (region_id, codigo);
CREATE UNIQUE INDEX municipios_departamento_id_nombre_key ON municipios (departamento_id, lower(nombre));
CREATE UNIQUE INDEX municipios_departamento_id_codigo_key ON municipios (departamento_id, codigo);

