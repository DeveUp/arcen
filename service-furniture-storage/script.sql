CREATE TABLE block(
	id BIGINT NOT NULL,
    letter VARCHAR(255) NOT NULL,
    flat VARCHAR(255),
    creation_date date,
    PRIMARY KEY (id)
);

CREATE TABLE furniture(
	id BIGINT NOT NULL,
    id_block BIGINT NOT NULL,
    id_type_furniture BIGINT NOT NULL,
    number_furniture INT NOT NULL,
    creation_date date,
    PRIMARY KEY (id)
);


CREATE TABLE type_furniture(
	id BIGINT NOT NULL,
    number_type_furniture INT NOT NULL,
    count_rack INT NOT NULL,
    count_row INT NOT NULL,
    depth INT NOT NULL,
    height INT NOT NULL,
    width INT NOT NULL,
    creation_date date,
    PRIMARY KEY (id)
);
