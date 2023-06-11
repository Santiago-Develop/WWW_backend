-- Country
INSERT INTO app_country(name) VALUES ('Colombia');

--Departments
INSERT INTO app_department (name, country_id) VALUES ('Amazonas', 1);
INSERT INTO app_department (name, country_id) VALUES ('Antioquia', 1);
INSERT INTO app_department (name, country_id) VALUES ('Arauca', 1);
INSERT INTO app_department (name, country_id) VALUES ('Atlantico', 1);
INSERT INTO app_department (name, country_id) VALUES ('Bolivar', 1);
INSERT INTO app_department (name, country_id) VALUES ('Boyaca', 1);
INSERT INTO app_department (name, country_id) VALUES ('Caldas', 1);
INSERT INTO app_department (name, country_id) VALUES ('Caqueta', 1);
INSERT INTO app_department (name, country_id) VALUES ('Casanare', 1);
INSERT INTO app_department (name, country_id) VALUES ('Cauca', 1);
INSERT INTO app_department (name, country_id) VALUES ('Cesar', 1);
INSERT INTO app_department (name, country_id) VALUES ('Choco', 1);
INSERT INTO app_department (name, country_id) VALUES ('Cordoba', 1);
INSERT INTO app_department (name, country_id) VALUES ('Cundinamarca', 1);

INSERT INTO app_department (name, country_id) VALUES ('Guainia', 1);
INSERT INTO app_department (name, country_id) VALUES ('Guaviare', 1);
INSERT INTO app_department (name, country_id) VALUES ('Huila', 1);
INSERT INTO app_department (name, country_id) VALUES ('La Guajira', 1);
INSERT INTO app_department (name, country_id) VALUES ('Magdalena', 1);
INSERT INTO app_department (name, country_id) VALUES ('Meta', 1);
INSERT INTO app_department (name, country_id) VALUES ('Nariño', 1);
INSERT INTO app_department (name, country_id) VALUES ('Norte de Santander', 1);
INSERT INTO app_department (name, country_id) VALUES ('Putumayo', 1);
INSERT INTO app_department (name, country_id) VALUES ('Quindio', 1);
INSERT INTO app_department (name, country_id) VALUES ('Risaralda', 1);
INSERT INTO app_department (name, country_id) VALUES ('San Andres y Providencia', 1);
INSERT INTO app_department (name, country_id) VALUES ('Santander', 1);
INSERT INTO app_department (name, country_id) VALUES ('Sucre', 1);
INSERT INTO app_department (name, country_id) VALUES ('Tolima', 1);
INSERT INTO app_department (name, country_id) VALUES ('Valle del Cauca', 1);
INSERT INTO app_department (name, country_id) VALUES ('Vaupes', 1);
INSERT INTO app_department (name, country_id) VALUES ('Vichada', 1);

--City
INSERT INTO app_city (name, department_id) VALUES ('Leticia', 1);
INSERT INTO app_city (name, department_id) VALUES ('Medellin', 2);
INSERT INTO app_city (name, department_id) VALUES ('Arauca', 3);
INSERT INTO app_city (name, department_id) VALUES ('Barranquilla', 4);
INSERT INTO app_city (name, department_id) VALUES ('Cartagena', 5);
INSERT INTO app_city (name, department_id) VALUES ('Tunja', 6);
INSERT INTO app_city (name, department_id) VALUES ('Manizalez', 7);
INSERT INTO app_city (name, department_id) VALUES ('Florencia', 8);
INSERT INTO app_city (name, department_id) VALUES ('Yopal', 9);
INSERT INTO app_city (name, department_id) VALUES ('Popayan', 10);
INSERT INTO app_city (name, department_id) VALUES ('Valledupar', 11);
INSERT INTO app_city (name, department_id) VALUES ('Quibdo', 12);
INSERT INTO app_city (name, department_id) VALUES ('Monteria', 13);
INSERT INTO app_city (name, department_id) VALUES ('Bogota', 14);
INSERT INTO app_city (name, department_id) VALUES ('Inirida', 15);
INSERT INTO app_city (name, department_id) VALUES ('San Jose del Guaviare', 16);
INSERT INTO app_city (name, department_id) VALUES ('Neiva', 17);
INSERT INTO app_city (name, department_id) VALUES ('Riohacha', 18);
INSERT INTO app_city (name, department_id) VALUES ('Santa Marta', 19);
INSERT INTO app_city (name, department_id) VALUES ('Villavicencio', 20);
INSERT INTO app_city (name, department_id) VALUES ('Pasto', 21);
INSERT INTO app_city (name, department_id) VALUES ('Cucuta', 22);
INSERT INTO app_city (name, department_id) VALUES ('Mocoa', 23);
INSERT INTO app_city (name, department_id) VALUES ('Armenia', 24);
INSERT INTO app_city (name, department_id) VALUES ('Pereira', 25);
INSERT INTO app_city (name, department_id) VALUES ('San Andres', 26);
INSERT INTO app_city (name, department_id) VALUES ('Bucaramanga', 27);
INSERT INTO app_city (name, department_id) VALUES ('Sincelejo', 28);
INSERT INTO app_city (name, department_id) VALUES ('Ibague', 29);
INSERT INTO app_city (name, department_id) VALUES ('Cali', 30);
INSERT INTO app_city (name, department_id) VALUES ('Mitu', 31);
INSERT INTO app_city (name, department_id) VALUES ('Vichada', 32);

--State
INSERT INTO public.app_state(name) VALUES ('Required');
INSERT INTO public.app_state(name) VALUES ('Assigned');
INSERT INTO public.app_state(name) VALUES ('Picked_up');
INSERT INTO public.app_state(name) VALUES ('Delivered');