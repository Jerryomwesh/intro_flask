from flask import Blueprint, request, jsonify

#create student blueprint
student_bp = Blueprint ("student", __name__)


#routes and controller logic
@student_bp.route ("/student/add", methods = ["POST"])
def add_user():
    print ("Add user was hit")
    return "Adding a user"


@student_bp.route ("/student", methods = ["GET"])
def list_user():
    print ("List Students")
    return "List All students"
