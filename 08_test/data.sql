USE calculator;

CREATE TABLE volume_surface_data(
	block_id INT AUTO_INCREMENT PRIMARY KEY,
    block_name VARCHAR(30) NOT NULL,
    float_a FLOAT(10) DEFAULT NULL,
    char_a VARCHAR(10) DEFAULT NULL,
    float_b FLOAT(10) DEFAULT NULL,
    char_b VARCHAR(10) DEFAULT NULL,
    float_c FLOAT(10) DEFAULT NULL,
    char_c VARCHAR(10) DEFAULT NULL,
    date_added TIMESTAMP
);

INSERT INTO volume_surface_data(block_name, float_a, char_a) VALUES('cube', 3.33, '3,33');
INSERT INTO volume_surface_data(block_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('cuboid', 1.33, '1,33', 2.33, '2,33', 1.99, '1,99');
INSERT INTO volume_surface_data(block_name, float_a, char_a, float_b, char_b) VALUES('cylinder', 3.33, '3,33', 7, '7');
INSERT INTO volume_surface_data(block_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('cone', 8, '8', 11, '11', 7.55, '7,55');
INSERT INTO volume_surface_data(block_name, float_a, char_a) VALUES('sphere', 5.55, '5,55');
INSERT INTO volume_surface_data(block_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('prism', 5, '5', 4.33, '4,33', 7.33, '7,33');

SELECT * FROM volume_surface_data;