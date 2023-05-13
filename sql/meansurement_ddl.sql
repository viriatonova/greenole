\connect greenole_iot;

CREATE SCHEMA sensor_measurement;

CREATE TABLE sensor_measurement.measurements (
    id SERIAL PRIMARY KEY,
    sensor_id varchar(255) NOT NULL,
    timestamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    variable varchar(255) NOT NULL,
    value float NOT NULL,
    unit varchar(255) NOT NULL,
    CONSTRAINT sensor_measurement UNIQUE (sensor_id, timestamp, variable, value)
);