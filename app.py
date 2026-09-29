from flask import Flask, render_template, request

app = Flask(__name__)

students = {
    "Yasser Zriouh": {
        "age": 15,
        "class": "TCSF-1",
        "grade": 12
    },
    "Sanoubari Mohamed": {
        "age": 17,
        "class": "TCSF-1",
        "grade": 15
    },
    "Anas Dali": {
        "age": 5,
        "class": "TCSF-1",
        "grade": 10
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    student = None
    name = ""

    if request.method == "POST":
        name = request.form["name"]
        student = students.get(name)

    return render_template(
        "index.html",
        student=student,
        name=name
    )

app.run(debug=True)