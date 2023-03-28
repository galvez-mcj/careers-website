from sqlalchemy import create_engine, text
from os import environ

conn_str = environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(conn_str,
                       connect_args={
                            "ssl": {
                                    "ca": "cacert.pem"
                                }
                       })


# Load the database contents
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from jobs"))
        jobs = []
        
        for row in result:
            jobs.append(row._mapping)

        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT * from jobs WHERE id = {id}")
        )

        jobs = []

        for row in result:
            jobs.append(row._mapping)
        
        return jobs
