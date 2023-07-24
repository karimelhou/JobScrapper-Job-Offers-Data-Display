from sqlalchemy import create_engine, Column, String, Date , Integer , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from variables import job_titles, company_names, locations, salaries , dates
import time
from datetime import datetime



Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    company = Column(String(255))
    location = Column(String(255))
    salary = Column(Float)
    date_posted = Column(Date)


engine = create_engine('mysql+pymysql://root:@localhost/indeed_data')


Base.metadata.create_all(engine)


# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Iterate over the scraped data and store each job in the database
for i in range(len(job_titles)):

    # Check if job with the same title and company already exists
    existing_job = session.query(Job).filter_by(title=job_titles[i], company=company_names[i]).first()

    if existing_job:
        print(f"Job already exists: {job_titles[i]} - {company_names[i]}")
        continue  # Skip adding the job to the database

    if salaries[i] == "Salary not found":
        salary = None
    else:
        try:
            salary = float(salaries[i].replace(',', ''))
        except ValueError:
            print(f"Invalid salary value: {salaries[i]}")
            salary = None

    if dates[i] == "Date not found":
        date_posted = None
    else:
        try:
            date_posted = datetime.strptime(dates[i], '%Y-%m-%d').date()
        except ValueError:
            print(f"Invalid date value: {dates[i]}")
            date_posted = None

    job = Job(
        title=job_titles[i],
        company=company_names[i],
        location=locations[i],
        salary=salary,
        date_posted=date_posted
    )
    session.add(job)


# Commit the session to save the changes
session.commit()

# Close the session
session.close()

# ...


