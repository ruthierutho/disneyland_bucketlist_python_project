DROP TABLE attractions;
DROP TABLE lands;
DROP TABLE parks;



CREATE TABLE parks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREAT TABLE lands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    park_id INT REFERENCES users(id),
    theme VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    land_id INT REFERENCES lands(id),
    category VARCHAR(255),
    visited BOOLEAN,
    visit_count INT,
    notes TEXT
);