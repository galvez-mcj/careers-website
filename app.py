from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Manila, Philippines',
        'salary': '25,000'
    },
    {
        'id': 2,
        'title': 'Associate Software Engineer',
        'location': 'Remote',
        'salary': '28,000'
    },
    {
        'id': 3,
        'title': 'Front-end Engineer',
        'location': 'NCR, Philippines'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'location': 'Makati, Philippines',
        'salary': '28,700'
    },
    {
        'id': 5,
        'title': 'Backend Developer',
        'location': 'Philippines',
        'salary': '26,500'
    }
]


@app.route("/")
def index():
    jobs = JOBS
    return render_template('index.html', jobs=jobs)



if __name__ == "__main__":
    app.run(debug=True)