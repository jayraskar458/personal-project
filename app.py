from flask import Flask,render_template,jsonify
app= Flask(__name__)

JOBS=[
    {
        "ID":1,
        "TITLE":'Data Analyst',
        "LOCATION":'Mumbai',
        "SALARY":'Rs20,00,000'
    },
    {
        "ID":2,
        "TITLE":'Data Scientist',
        "LOCATION":'Remote',
        "SALARY":'Rs30,000,00'
    },
    {
        "ID":3,
        "TITLE":'SDE',
        "LOCATION":'Goa',
        "SALARY":'Rs40,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def getJobsAPI():
     return jsonify(JOBS);

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
