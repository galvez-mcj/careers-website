from flask import Flask, render_template
from database import load_jobs_from_db


app = Flask(__name__)

#############################################################
# ROUTES
#############################################################

# Index route
@app.route("/")
def index():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs)




if __name__ == "__main__":
    app.run(debug=True)