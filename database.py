from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv('SQLALCHEMY_DATABASE_URI')
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


