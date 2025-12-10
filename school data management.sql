
CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(15),
    PRIMARY KEY (student_id)
);

INSERT INTO students (student_id, first_name, last_name, email, phone_number)
VALUES 
    (1, 'Jonathan', 'Gilbert', 'jonathan.gilbert@winthrop.edu', '7575746746'),
    (2, 'Jane', 'Smith', 'jane.smith@winthrop.edu', '64758574793'),
    (3, 'Candice', 'Jones', 'candice.jones@winthrop.edu', '3647363728'),
    (4, 'Ronald', 'McDonald', 'ronald.mcdonald@winthrop.edu', '3746378498'),
    (5, 'Mike', 'Johnson', 'mike.johnson@winthrop.edu', '3647584637');

CREATE TABLE courses (
    course_id INT NOT NULL AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (course_id)
);

INSERT INTO courses (course_id, course_name)
VALUES
    (101,'Introduction to Mathematics'),
    (102,'Introduction to Science'),
    (103, 'Accounting'),
    (104, 'Database Processing'),
    (105, 'Biology');

CREATE TABLE grades (
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

INSERT INTO grades (student_id, course_id, grade) 
VALUES
    (1, 102, 'A'),
    (2, 101, 'C'),
    (3, 102, 'A'),
    (1, 103, 'D'),
    (3, 104, 'A'),
    (4, 105, 'B'),
    (5, 101, 'C');







