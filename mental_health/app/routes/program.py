from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for, make_response
import jwt

program_ = Blueprint('program', __name__)

@program_.route('/program')
def program():
    myToken = request.cookies.get("mytoken")
    SECRET_KEY = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(myToken, SECRET_KEY, algorithms=["HS256"])
        user_info = current_app.db.users.find_one({"username": payload["id"]})
        return render_template('dashboard/program.html', user_info=user_info)
    except jwt.ExpiredSignatureError:from flask import Flask, request, render_template, current_app, Blueprint, jsonify, redirect, url_for, make_response
import jwt

program_ = Blueprint('program', __name__)

@program_.route('/program')
def program():
    myToken = request.cookies.get("mytoken")
    SECRET_KEY = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(myToken, SECRET_KEY, algorithms=["HS256"])
        user_info = current_app.db.users.find_one({"username": payload["id"]})
        return render_template('dashboard/program.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("auth.login"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("auth.login"))
        return redirect(url_for("home.menu"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("home.menu"))
    
@program_.route('/save-status-screening',  methods=["POST"])
def save_status_screening():
    username = request.form['username']
    scoreScreening = request.form['resultText']
    doc = {       
        "username": username, 
          "scoreScreening": scoreScreening                                            
    }
    exists = bool(current_app.db.status_screening.find_one({"username": username}))
    if exists:
        return jsonify(
            {
                "exists": exists,
                "result": "Sudah Pernah Screening",
            }
        )
    else:
        current_app.db.status_screening.insert_one(doc)
        return jsonify(
            {
                "exists": exists,
                "result": "Success",
            }
        )