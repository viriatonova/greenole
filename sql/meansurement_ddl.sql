\connect greenole_iot;

CREATE SCHEMA sensor_measurement;

CREATE TABLE sensor_measurement.measurements (
    id SERIAL PRIMARY KEY,
    sensor_id integer NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    variable varchar(20) NOT NULL,
    value float NOT NULL,
    unit varchar(10) NOT NULL,
    CONSTRAINT sensor_measurement UNIQUE (sensor_id, created_at, variable, value)
);