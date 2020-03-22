CREATE DATABASE calculator;
USE calculator;

DROP TABLE IF EXISTS fields_circuits_data

CREATE TABLE fields_circuits_data(
	figure_id INT AUTO_INCREMENT PRIMARY KEY,
    figure_name VARCHAR(30) NOT NULL,
    float_a FLOAT(10) DEFAULT NULL,
    char_a VARCHAR(10) DEFAULT NULL,
    float_b FLOAT(10) DEFAULT NULL,
    char_b VARCHAR(10) DEFAULT NULL,
    float_c FLOAT(10) DEFAULT NULL,
    char_c VARCHAR(10) DEFAULT NULL,
    float_d FLOAT(10) DEFAULT NULL,
    char_d VARCHAR(10) DEFAULT NULL,
    date_added TIMESTAMP
);

INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b) VALUES('circle', 5, '5', 10, '10');
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b, float_c, char_c, float_d, char_d) VALUES('triangle', 10, '10', 8.55, '8,55', 11, '11', 0.8335, '0,8335');
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('rectangular triangle', 10, '10', 11.11, '11,11', 14.95, '14,95')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a) VALUES('square', 4.23, '4,23')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b) VALUES('rectangle', 4.29, '4,29', 6.39, '6,39')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b) VALUES('rhombus', 4.33, '4,33', 3.43, '3,43')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('parallelogram', 5.55, '5,55', 6.66, '6,66', 6.66, '6,66')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b, float_c, char_c) VALUES('trapeze', 7.77, '7,77', 4, '4', 7.77, '7,77')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a) VALUES('hexagon', 3.23, '3,23')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b) VALUES('polygon', 11, '11', 5.55, '5,55')
INSERT INTO fields_circuits_data(figure_name, float_a, char_a, float_b, char_b) VALUES('pythagorean theorem', 4.33, '4.33', 6.45, '6,45')

SELECT * FROM fields_circuits_data;