from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def db_config(app):
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root123@127.0.0.1:3306/test"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "../dbs/test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "KEY"
    return app


app = Flask(__name__)
app = db_config(app)
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum("男", "女"), nullable=False)
    phone = db.Column(db.String(11))
    grades = db.relationship("Grade", backref="student")
    courses = db.relationship("Course", secondary="student_course", backref="students")

    def __repr__(self):
        return 'Student %s %s' % (self.id, self.name)


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum("男", "女"))
    phone = db.Column(db.String(11))
    courses = db.relationship("Course", backref="teacher")

    def __repr__(self):
        return 'Teacher %s %s' % (self.id, self.name)


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    grades = db.relationship("Grade", backref="course")

    def __repr__(self):
        return 'Course %s %s' % (self.id, self.name)


class Grade(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(3), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    def __repr__(self):
        return 'Grade %s %s' % (self.id, self.name)


class StudentCourse(db.Model):
    __tablename__ = "student_course"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    def __repr__(self):
        return 'StudentCourse %d %d' % (self.student_id, self.course_id)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
