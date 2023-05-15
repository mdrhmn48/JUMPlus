use exercise1;

select * from employeeinfo;
CREATE TABLE EmployeePosition  (
    EmpID INT,
    EmpPosition varchar(255),
    DateOfJoining  date,
    Salary INT,
    FOREIGN KEY (EmpID) REFERENCES employeeinfo(EmpID)
);
drop table employeeInfo;
CREATE TABLE employeeInfo (
    EmpID INT PRIMARY KEY,
    EmpPosition VARCHAR(255),
    DateOfJoining DATE,
    Salary DECIMAL(10, 2)
);

CREATE TABLE EmployeeInfo (
    EmpID INT PRIMARY KEY,
    EmpFname VARCHAR(255),
    EmpLname VARCHAR(255),
    Department VARCHAR(255),
    Project VARCHAR(255),
    Address VARCHAR(255),
    DOB DATE,
    Gender ENUM('M', 'F')
);
INSERT INTO EmployeeInfo (EmpID, EmpFname, EmpLname, Department, Project, Address, DOB, Gender)
VALUES
    (1, 'Sanjay', 'Mehra', 'HR', 'P1', 'Hyderabad(HYD)', '1976-12-01', 'M'),
    (2, 'Ananya', 'Mishra', 'Admin', 'P2', 'Delhi(DEL)', '1968-05-02', 'F'),
    (3, 'Rohan', 'Diwan', 'Account', 'P3', 'Mumbai(BOM)', '1980-01-01', 'M'),
    (4, 'Sonia', 'Kulkarni', 'HR', 'P1', 'Hyderabad(HYD)', '1992-05-02', 'F'),
    (5, 'Ankit', 'Kapoor', 'Admin', 'P2', 'Delhi(DEL)', '1994-07-03', 'M');


INSERT INTO EmployeePosition (EmpID, EmpPosition, DateOfJoining, Salary)
VALUES
    (1, 'Manager', '2022-05-01', 500000),
    (2, 'Executive', '2022-05-02', 75000),
    (3, 'Manager', '2022-05-01', 90000),
    (2, 'Lead', '2022-05-02', 85000),
    (1, 'Executive', '2022-05-01', 300000);




