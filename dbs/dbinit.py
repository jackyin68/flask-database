from dbcreate import Student,Teacher,Course,Grade,StudentCourse
from dbop import rows_add

student_01 = Student(name="周星驰", gender="男", phone="1382101xxx")
student_02 = Student(name="张曼玉", gender="女", phone="1523321xxx")
students = [student_01, student_02]
rows_add(students)

teacher_01 = Teacher(name="王老师", gender="男", phone="1372101xxx")
teacher_02 = Teacher(name="唐老师", gender="女", phone="1362101xxx")
teacher_03 = Teacher(name="吴老师", gender="女", phone="1582101xxx")
teacher_04 = Teacher(name="曹老师", gender="女", phone="1352101xxx")
teacher_05 = Teacher(name="陆老师", gender="女", phone="1332101xxx")
teachers = [teacher_01, teacher_02,teacher_03,teacher_04,teacher_05]
rows_add(teachers)

grade_01 = Grade(course_id=1, student_id=1, grade=95)
grade_02 = Grade(course_id=2, student_id=1, grade=85)
grades = [grade_01, grade_02]
rows_add(grades)

course_01 = Course(name="物理", teacher_id=1)
course_02 = Course(name="数学", teacher_id=2)
course_03 = Course(name="化学", teacher_id=3)
course_04 = Course(name="语文", teacher_id=4)
course_05 = Course(name="英语", teacher_id=5)
courses = [course_01, course_02, course_03, course_04, course_05]
rows_add(courses)

student_course_01 = StudentCourse(student_id=1,course_id=1)
student_course_02 = StudentCourse(student_id=1,course_id=2)
student_course_03 = StudentCourse(student_id=2,course_id=1)
student_course_04 = StudentCourse(student_id=2,course_id=3)
student_course_05 = StudentCourse(student_id=2,course_id=5)
student_courses = [student_course_01,student_course_02,student_course_03,student_course_04,student_course_05]
rows_add(student_courses)