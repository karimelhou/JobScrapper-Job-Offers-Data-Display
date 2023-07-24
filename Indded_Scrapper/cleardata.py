from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job

# Create an engine and session
engine = create_engine('mysql+pymysql://root:@localhost/indeed_data')
Session = sessionmaker(bind=engine)
session = Session()

# Execute a delete query to remove all records from the 'jobs' table
session.query(Job).delete()

# Commit the session to persist the changes
session.commit()

# Close the session
session.close()
