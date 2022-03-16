-- migrate:up
INSERT INTO publication (id, name) VALUES
(100,'Oracle'),
(200,'Spark'),
(300,'Python'),
(400,'Cloudera');

INSERT INTO book (title, author, avg_rating, format, image, num_pages, pub_id) VALUES
('Hakers','Douglas Peter', 3.9, 'ePub', 'broom-145379.svg', 133, 100),
('El Quijote', 'Dawn Brown', 4.1, 'Hardcover', 'cat-150306.svg', 250, 100),
('El Perfume', 'Patrick Suskind', 4.6, 'ebook', 'dog-950106.svg', 350, 200),
('Dracula', 'Bram Stoker', 5.8, 'ebook', 'pg-750206.svg', 350, 200),
('Rebelion en la Granja', 'George Orwell', 2.4, 'ePub', 'gh-150234.svg', 120, 300),
('Casi el Paraiso', 'John Spota', 6.2, 'ePub', 'cs-457831.svg', 180, 300),
('Match Point', 'Rafa Nadal', 2.8, 'Paperback', 'cd-39732.svg', 423, 400);

-- migrate:down
