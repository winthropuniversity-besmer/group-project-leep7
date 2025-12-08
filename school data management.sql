
CREATE TABLE Students (
    student_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(15),
    PRIMARY KEY (student_id)
);

INSERT INTO Students (first_name, last_name, email, phone_number)
VALUES 
    ('Johnny', 'Grant', 'johnny.grant@example.com', '7575746746'),
    ('Jane', 'Smith', 'jane.smith@example.com', '64758574793'),
    ('Candice', 'Jones', 'candice.jones@example.com', '3647363728'),
    ('Art', 'Donald', 'art.donald@example.com', '3746378498'),
    ('Mike', 'Johnson', 'mike.johnson@example.com', '3647584637');

CREATE TABLE Courses (
    course_id INT NOT NULL AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (course_id)
);

INSERT INTO Courses (course_id, course_name)
VALUES
    (101,'Introduction to Mathematics'),
    (102,'Introduction to Science'),
    (103, 'Accounting'),
    (104, 'Database Processing'),
    (105, 'Biology');

CREATE TABLE Grades (
    grade_id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade CHAR(2) NOT NULL,
    PRIMARY KEY(grade_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE 
);

INSERT INTO Grades (student_id, course_id, grade) 
VALUES
    (1, 102, 'A'),
    (1, 101, 'C'),
    (1, 103, 'D'),
    (1, 104, 'A'),
    (2, 105, 'B');




