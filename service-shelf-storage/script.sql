CREATE TABLE public.dependence(
	id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO public.dependence
(id, name, code)
VALUES(1, 'Sistemas', '115');

CREATE TABLE public.shelf(
	id BIGINT NOT NULL,
    id_dependence INT NOT NULL,
    id_type_shelf INT NOT NULL,
    id_furniture INT NOT NULL,
    number_shelf INT NOT NULL,
    creation_date date,
    PRIMARY KEY (id)
);


CREATE TABLE public.type_shelf(
	id BIGINT NOT NULL,
    number_type_shelf INT NOT NULL,
    depth INT NOT NULL,
    height INT NOT NULL,
    width INT NOT NULL,
    creation_date date,
    PRIMARY KEY (id)
);
