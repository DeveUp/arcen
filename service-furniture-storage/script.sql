CREATE TABLE public.block(
	id BIGINT NOT NULL,
    letter VARCHAR(255) NOT NULL,
    flat VARCHAR(255),
    creation_date date,
    PRIMARY KEY (id)
);

INSERT INTO public.block
(id, letter, flat, creation_date)
VALUES(1, 'Test Letter', 'Test Flat', '2000/08/09');

CREATE TABLE public.furniture(
	id BIGINT NOT NULL,
    id_block BIGINT NOT NULL,
    id_type_furniture BIGINT NOT NULL,
    number_furniture INT NOT NULL,
    creation_date date,
    PRIMARY KEY (id)
);


CREATE TABLE public.type_furniture(
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
