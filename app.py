from flask import Flask, render_template
from database import load_jobs_from_db, load_job_from_db
import json

app = Flask(__name__)

#############################################################
# ROUTES
#############################################################

# Index route
@app.route("/")
def index():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id) 
    if not job:
        return render_template('errorPage.html')
    else:
        return render_template('jobPage.html', job=job[0])


if __name__ == "__main__":
    app.run(debug=True)