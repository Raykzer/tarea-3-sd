CREATE TABLE paginas(
    id INT NOT NULL PRIMARY KEY,
    url TEXT NOT NULL
);

CREATE TABLE registros (
    palabra varchar NOT NULL,
    documento INT NOT NULL REFERENCES paginas(id) ON DELETE CASCADE,
    frecuencia INT NOT NULL,
    CONSTRAINT tuplas UNIQUE (palabra, documento)
);