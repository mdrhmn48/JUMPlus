create database exercise2;
use exercise2;

CREATE TABLE IF NOT EXISTS employee_details (
emp_id INT PRIMARY KEY,
full_name VARCHAR(50) NOT NULL,
manager_id INT NOT NULL,
date_of_joining DATE NOT NULL,
city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS employee_salary (
salary_id INT AUTO_INCREMENT PRIMARY KEY,
emp_id INT NOT NULL,
project VARCHAR(50) NOT NULL,
salary INT NOT NULL,
variable INT,
FOREIGN KEY (emp_id) REFERENCES employee_details(emp_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

INSERT INTO employee_details (emp_id, full_name, manager_id,
date_of_joining, city)
VALUES
(121, 'John Snow', 321, '2014-01-31', 'Toronto'),
(321, 'Walter White', 986, '2015-01-31', 'California'),
(421, 'Kuldeep Rana', 876, '2016-11-27', 'New Delhi');


INSERT INTO employee_salary (emp_id, project, salary, variable)
VALUES
(121, 'P1', 8000, 500),
(321, 'P2', 10000, 1000),
(421, 'P1', 12000, 0);

SELECT e.*
FROM employee_details e
LEFT JOIN employee_details m ON e.manager_id = m.emp_id
WHERE e.city = 'California' OR m.emp_id = 321;

SELECT *
FROM employee_details
WHERE full_name LIKE '__hn%';

SELECT ed.emp_id
FROM Employee_details ed
INNER JOIN employee_salary es ON ed.emp_id = es.emp_id;

SELECT SUM(LENGTH(full_name) - LENGTH(REPLACE(full_name, 'n', ''))) AS count_of_n
FROM employee_details;

SELECT full_name
FROM employee_details
INNER JOIN employee_salary ON employee_details.emp_id = employee_salary.emp_id
WHERE salary >= 5000 AND salary <= 10000;

SELECT *
FROM employee_details
INNER JOIN employee_salary ON employee_details.emp_id = employee_salary.emp_id;

SELECT employee_details.full_name, employee_salary.salary
FROM employee_details
LEFT JOIN employee_salary ON employee_details.emp_id = employee_salary.emp_id;

SELECT e1.*
FROM employee_details e1
INNER JOIN employee_details e2 ON e1.emp_id = e2.manager_id;

DELETE FROM employee_details
WHERE emp_id NOT IN (
  SELECT MIN(emp_id)
  FROM employee_details
  GROUP BY full_name, manager_id, date_of_joining, city
);

SELECT salary
FROM employee_salary
ORDER BY salary DESC
LIMIT 2,1;





SELECT DISTINCT salary
FROM employee_salary e1
WHERE 3 = (
  SELECT COUNT(DISTINCT salary)
  FROM employee_salary e2
  WHERE e2.salary > e1.salary
);











INSERT INTO employee_details (emp_id, full_name, manager_id, date_of_joining, city)
VALUES
(521, 'Sarah Lee', 321, '2017-03-15', 'San Francisco'),
(621, 'James Smith', 321, '2018-01-22', 'Los Angeles'),
(721, 'Maria Garcia', 986, '2019-08-10', 'San Diego');

select * from employee_details;
select * from employee_salary;

select *
from employee_details e
#join employee_details m ON e.manager_id= m.emp_id
where e.city = "California" or e.manager_id = 321;

select * 
from employee_details
where full_name like '__hn%';
