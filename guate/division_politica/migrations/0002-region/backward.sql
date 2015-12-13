
DROP INDEX departamentos_region_id_nombre_key;
DROP INDEX departamentos_region_id_codigo_key;
DROP INDEX municipios_departamento_id_nombre_key;
DROP INDEX municipios_departamento_id_codigo_key;

CREATE UNIQUE INDEX ui_departamentos_nombre ON departamentos (lower(nombre));
CREATE UNIQUE INDEX ui_departamentos_codigo ON departamentos (codigo);
CREATE UNIQUE INDEX ui_municipios_nombre ON municipios (departamento_id, lower(nombre));
CREATE UNIQUE INDEX ui_municipios_codigo ON municipios (departamento_id, codigo);

ALTER TABLE departamentos DROP COLUMN region_id;

DROP TABLE regiones;