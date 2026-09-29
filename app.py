from flask import Flask, render_template, request, jsonify

app = Flask(name)

# قاعدة بيانات التلاميذ
STUDENTS_DATA = {
    "yasser zriouh": {
        "name": "Yasser Zriouh",
        "age": 15,
        "class": "TCSF-1",
        "grade": 12
    },
    "sanoubari mohamed": {
        "name": "Sanoubari Mohamed",
        "age": 17,
        "class": "TCSF-1",
        "grade": 15
    },
    "anas dali": {
        "name": "Anas Dali",
        "age": 15,
        "class": "TCSF-1",
        "grade": 10
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_student', methods=['POST'])
def get_student():
    data = request.get_json()
    student_name = data.get('name', '').strip().lower()
    
    if student_name in STUDENTS_DATA:
        return jsonify({"success": True, "student": STUDENTS_DATA[student_name]})
    else:
        return jsonify({"success": False, "message": "Student not found"})

if name == 'main':
    app.run(debug=True)