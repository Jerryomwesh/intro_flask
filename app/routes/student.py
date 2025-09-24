from flask import Blueprint,jsonify,request
from ..models import Student 
from ..db import db

#create student bluprint
student_bp=Blueprint("student",__name__,url_prefix="/student")


@student_bp.route("/add",methods=["GET"])
def singlee_student():
    print("Single student")
    return "Single student"

#adding a student to our db
#routes and controller logic
@student_bp.route("/add/json",methods=["POST"])
def add_user_json():
    print("Add user was hit")
    data=request.get_json() #Body to json as python dic

    name=data.get("name")
    email=data.get("email")

    if not name or not email:
        return jsonify ({"error":"Name and email are required"}),400
    
    #check for existing email
    exists=Student.query.filter_by(email=email).first()
    if exists:
        return jsonify({"error":"Email already exists"}),400
    
    new_student=Student(name=name,email=email)
    # new_student.save() #save to db
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "message":"Student added successfully",
        "student":{
            "id":new_student.id,
            "name":new_student.name,
            "email":new_student.email,
            "created_at":new_student.created_at.isoformat()
            }
        }),201


    # print("Received Data",data)
    # # Read the request
    # return "Adding a student",200

@student_bp.route("/add/form",methods=["POST"])
def add_user_form():
    print("Add user was hit")
    return "Adding a student",200

@student_bp.route("/edit",methods=["PUT"])
def edit_student():
    print("Add user was hit")
    return "Edit a student"

@student_bp.route("/list",methods=["GET"])
def list_users():
    # print("List Students")
    # return "List All students"

    students=Student.query.all()

    print(students)

    student_list=[]

    for student in students:
        student_list.append({
            "id":student.id,
            "name":student.name,
            "email":student.email,
            "created_at":student.created_at.isoformat()
        })

    return jsonify(student_list),200


#getting a single student 
@student_bp.route("/single/<int:id>",methods=["GET"])
def single_student(id):

    student=Student.query.filter_by(id=id).first()

    if not student:
        return jsonify({"message":f"Student with id {student_id} not found"}),404
    
    return jsonify({
        "id":student.id,
        "name":student.name,
        "email":student.email,
        "created_at":student.created_at.isoformat()
    }),200



#editing a student  
@student_bp.route("/edit/<int:id>",methods=["PUT"])
def edit_student_id(id):

    student=Student.query.filter_by(id=id).first()

    if not student:
        return jsonify({"message":f"Student with id {id} not found"}),404
    
    data=request.get_json() #Body to json as python dic

    name=data.get("name")
    email=data.get("email")

    if not name or not email:
        return jsonify ({"error":"Name and email are required"}),400
    
    #check for existing email
    exists=Student.query.filter_by(email=email).first()
    if exists and exists.id != id:
        return jsonify({"error":"Email already exists"}),400
    
    student.name=name
    student.email=email

    db.session.commit()

    return jsonify({
        "message":"Student updated successfully",
        "student":{
            "id":student.id,
            "name":student.name,
            "email":student.email,
            "created_at":student.created_at.isoformat()
            }
        }),200    