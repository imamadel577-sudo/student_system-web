from flask import Flask, render_template, request

app = Flask(name)

# Sample student data
STUDENTS = [
    {"id": "STD-1001", "name": "Adel Imam", "grade": "Grade 10 - A", "gpa": "3.8", "status": "Passed"},
    {"id": "STD-1002", "name": "Fatima Zahra", "grade": "Grade 11 - B", "gpa": "4.0", "status": "Excellent"},
    {"id": "STD-1003", "name": "John Doe", "grade": "Grade 10 - C", "gpa": "2.9", "status": "Active"},
    {"id": "STD-1004", "name": "Sarah Smith", "grade": "Grade 12 - A", "gpa": "3.6", "status": "Passed"}
]

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("query", "").strip()
    results = []
    
    if query:
        # Search by student name or ID
        results = [
            student for student in STUDENTS 
            if query.lower() in student["name"].lower() or query.lower() in student["id"].lower()
        ]

    return render_template("index.html", query=query, results=results)

if name == "main":
    app.run(debug=True)