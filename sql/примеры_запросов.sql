SELECT * FROM Student ORDER BY surname DESC, name DESC;
SELECT * FROM Student WHERE Class.specialization = 'Программирование' JOIN Class ON Class.ID = Student.class_ID;
SELECT * FROM Student WHERE surname LIKE '%ов%';
SELECT * FROM Student WHERE class_ID NOT IN ('10.3', '10.4');
SELECT COUNT(*) FROM Subject;
SELECT COUNT(*) FROM Subject WHERE duration in (30, 60);
SELECT COUNT(*) FROM Teacher WHERE qualification = '3';
SELECT COUNT(Class.specialization) FROM student JOIN Class ON Class.ID = Student.group_ID;
SELECT Student.surname, Student.name FROM Student WHERE Teacher.name = 'Марина' AND Teacher.surname = 'Ерещенко' 
    JOIN Class ON Class.ID = Student.class_ID JOIN Teacher ON Teacher.ID = Class.teacher_ID;
SELECT * FROM Student WHERE Mark.value in (4, 5) AND Subject.name = 'Информатика' JOIN Student_mark ON Student_mark.student_ID = Student.ID 
    JOIN Mark ON Mark.ID = Student_mark.mark_ID JOIN Subject ON Subject.ID = Student_mark.subject_ID;
