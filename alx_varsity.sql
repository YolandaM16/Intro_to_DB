CREATE IF NOT EXISTS alx_varsity;

-- Create the Student table
CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT
    email VARCHAR(255), 
    FOREIGN KEY (department) REFERENCES ...
);

