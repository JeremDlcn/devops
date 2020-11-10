CREATE TABLE unites (
    numero_unite INT AUTO_INCREMENT PRIMARY KEY,
    nom_unite VARCHAR(25)
);

INSERT INTO unites(nom_unite) VALUES 
("Yaourt"),
("Fromage"),
("Beurre"),
("Lait"),
("Creme");

CREATE TABLE automates(
    id_automate INT AUTO_INCREMENT PRIMARY KEY,
    numero_automate INT,
    type_automate VARCHAR(10),
    numero_unite INT,
    FOREIGN KEY(numero_unite) REFERENCES unites(numero_unite)
);

INSERT INTO automates(numero_automate, type_automate, numero_unite) VALUES
    (1, '0X0000BA20', 1),
    (2, '0X0000BA21', 1),
    (3, '0X0000BA22', 1),
    (4, '0X0000BA23', 1),
    (5, '0X0000BA24', 1),
    (6, '0X0000BA25', 1),
    (7, '0X0000BA26', 1),
    (8, '0X0000BA27', 1),
    (9, '0X0000BA28', 1),
    (10, '0X0000BA29', 1);


CREATE TABLE donnes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    horaire INT,
    temperature_cuve FLOAT
    temperature_exterieure FLOAT
    poids_lait_cuve FLOAT
    poids_final FLOAT
    mesure_pH FLOAT
    mesure_K+ INT
    Concentration_NaCI FLOAT
    niveau_bacterie_salmonelle INT
    niveau_bacterie_E-coli INT
    niveau_bacterie_listeria INT
);