CREATE DATABASE company_dbase;

USE company_dbase;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    city VARCHAR(50)
);

INSERT INTO employees
(emp_name, department, salary, city)
VALUES
('Atharva', 'Data Science', 45000, 'Pune'),
('Aakanksha', 'Data Analytics', 50000, 'Mumbai'),
('Rahul', 'Data Engineering', 60000, 'Kolhapur'),
('Priya', 'AI/ML', 55000, 'Bangalore');

SELECT * FROM employees;