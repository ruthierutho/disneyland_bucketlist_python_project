DROP TABLE attractions;
DROP TABLE lands;
DROP TABLE parks;



CREATE TABLE parks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE lands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    park_id INT REFERENCES parks(id),
    theme VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    land_id INT REFERENCES lands(id),
    visited BOOLEAN,
    visit_count INT,
    notes TEXT
);