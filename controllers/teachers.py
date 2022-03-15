

from flask import Blueprint, redirect, render_template, request

from forms.addTeacherForm import AddTeacherForm
from models import Teacher, db


teachers_blueprint = Blueprint("teachers_blueprint", __name__)

@teachers_blueprint.route("/teachers", methods=["get", "post"])
def teachers():
    teachers = db.session.query(Teacher).all()

    


    return render_template("teachers.html",
    teachers = teachers)


add_teachers_blueprint = Blueprint("add_teachers_blueprint", __name__)

@add_teachers_blueprint.route("/teachers/add", methods=["get", "post"])
def add_teachers():
    addTeacherFormData = AddTeacherForm()
    if request.method == "POST":
        if addTeacherFormData.validate_on_submit():
            teacherData = Teacher()
            teacherData.first_name = addTeacherFormData.first_name.data
            teacherData.last_name = addTeacherFormData.last_name.data
            teacherData.birthdate = addTeacherFormData.birthdate.data
            #teacherData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(teacherData)
            db.session.commit()
        
            return redirect("/teachers/add")

        else:
            return render_template("teachers.html", form = addTeacherFormData)

    return render_template("addTeacherForm.html",
    form = addTeacherFormData)