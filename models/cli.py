# cli/commands.py

import click
from models.student import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('grade')
def add_student(name, age, grade):
    engine = create_engine('sqlite:///../data/student_db.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    student = Student(name=name, age=age, grade=grade)
    session.add(student)
    session.commit()
    session.close()
    click.echo(f'Student {name} added successfully.')

@cli.command()
def list_students():
    engine = create_engine('sqlite:///../data/student_db.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    students = session.query(Student).all()
    session.close()

    if students:
        click.echo('List of Students:')
        for student in students:
            click.echo(f'- {student.name}, Age: {student.age}, Grade: {student.grade}')
    else:
        click.echo('No students found.')
