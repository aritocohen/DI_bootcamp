-- CREATE TABLE employee (
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(20) NOT NULL,
-- 	last_name VARCHAR(20) NOT NULL,
-- 	birth_date DATE,
-- 	employee_number SMALLINT UNIQUE NOT NULL,
-- 	monthly_salary INTEGER CHECK (monthly_salary > 500),
-- 	currently_working BOOLEAN
-- );

-- SELECT * FROM employee

-- ALTER TABLE employee ALTER COLUMN currently_working SET DEFAULT true;

-- INSERT INTO employee (first_name, last_name, birth_date, employee_number, monthly_salary)
-- VALUES ('John', 'Doe', '1987-05-21', 12345, 1000)

-- INSERT INTO employee (first_name, last_name, birth_date, employee_number, monthly_salary) VALUES
-- 	('Lean', 'Dee', '1987-05-21', 12346, 1000),
-- 	('June', 'Bee', '1977-12-11', 12347, 1000),
-- 	('Tom', 'Doo', '1997-05-13', 12348, 1000);

-- SELECT first_name, last_name, monthly_salary FROM employee WHERE monthly_salary >= 500

-- SELECT first_name, last_name, employee_number FROM employee WHERE birth_date > '1997-01-01'

-- SELECT first_name, last_name, employee_number FROM employee WHERE first_name='Lean' OR last_name='Doe'

-- SELECT id, first_name, last_name, employee_number FROM employee ORDER BY last_name

-- SELECT id, first_name, last_name, employee_number FROM employee LIMIT 1 OFFSET 2

-- SELECT id, first_name, last_name, employee_number FROM employee ORDER BY last_name DESC

-- SELECT id, first_name, last_name, employee_number FROM employee WHERE last_name LIKE '%ee%'


-- EXCERSICE

-- SELECT * FROM employee LIMIT 4

-- SELECT * FROM employee ORDER BY last_name DESC LIMIT 4

-- SELECT * FROM employee WHERE first_name LIKE '%e%'

-- SELECT * FROM employee WHERE currently_working = True
