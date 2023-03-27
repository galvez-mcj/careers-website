from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Manila, Philippines',
        'salary': 'Php 25,000 /mo'
    },
    {
        'id': 2,
        'title': 'Associate Software Engineer',
        'location': 'Remote',
        'salary': 'Php 28,000 /mo'
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
        'salary': 'Php 28,700 /mo'
    },
    {
        'id': 5,
        'title': 'Backend Developer',
        'location': 'Philippines',
        'salary': 'Php 26,500 /mo'
    }
]


@app.route("/")
def index():
    jobs = JOBS
    return render_template('index.html', jobs=jobs)



if __name__ == "__main__":
    app.run(debug=True)