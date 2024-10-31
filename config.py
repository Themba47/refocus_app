import os
import pprint
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine('sqlite:////home/Thiza/refocus/minidb.sqlite')
Session = sessionmaker(bind=engine)