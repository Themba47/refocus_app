import os
from dotenv import load_dotenv
from datetime import datetime
import sqlalchemy as db
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, Text
from sqlalchemy.exc import SQLAlchemyError
load_dotenv()

sqlite_file = os.environ.get('SQLITE')

def get_connection():
   print(os.environ.get('SQLITE'))
   try:
      return db.create_engine(sqlite_file, echo=True)
   except SQLAlchemyError as e:
      print("Error while connecting to db: ", e)
      

meta = MetaData()

# address = Table(
# 	'Focus_questions', meta,
# 	Column('id', Integer, primary_key=True),
# 	Column('question', String),
# 	Column('type', String),
# 	Column('update_date', DateTime, default=datetime.now(), onupdate=datetime.now()),
#  	Column('created_date', DateTime, default=datetime.now(), onupdate=datetime.now()),
# )

address = Table(
	'Focus_answers', meta,
	Column('id', Integer, primary_key=True),
	Column('email', String),
	Column('answers', Text),
	Column('update_date', DateTime, default=datetime.now, onupdate=datetime.now),
 	Column('created_date', DateTime, default=datetime.now, onupdate=datetime.now),
)

if __name__ == "__main__":
   if get_connection():
      meta.create_all(get_connection())
