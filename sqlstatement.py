import os
import pprint
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.environ.get('SQLITE'))
Session = sessionmaker(bind=engine)

def insert_query(query):
   with Session() as conn:
      print(f"------------------- {os.environ.get('SQLITE')} -----------------------")
      result = conn.execute(query)
      conn.commit()
      return result
   

def execute_query(query):
   with Session() as conn:
      result = conn.execute(query)
      return [row._asdict() for row in result.fetchall()]
   
   
def sql_get_data():
   return text("""
               SELECT 
						*
					FROM Focus_questions
               """)   

   
def sql_insert_data():
   return text("""
	INSERT INTO Focus_questions (question, type)
	VALUES 
	('What are three things you''re most passionate about?', 'input'),
	('Which achievements in your life are you most proud of, and why?', 'textarea'),
	('What''s one area in your life where you''d like to see a significant improvement in the next year?', 'textarea'),
	('What skills or qualities do you admire in others that you wish to develop?', 'textarea'),
	('What kind of legacy or impact would you like to leave?', 'textarea'),
	('Imagine your ideal life five years from now—what are you doing, where are you, and who is with you?', 'textarea'),
	('What is one thing you would love to do or achieve if there were no limitations (time, money, or circumstances)?', 'textarea'),
	('When you''re in your “zone,” what are you usually doing, and what does it feel like?', 'textarea'),
	('If you could improve one skill or area of your life that would create a ripple effect in other areas, what would it be?', 'textarea'),
	('What daily habits do you currently have that you feel support or hinder your growth?', 'textarea'),
	('What do you want to be known for in your personal or professional life?', 'textarea'),
	('What past goals have you set that felt exciting but didn''t work out? Why do you think they didn''t work?', 'textarea'),
	('What habits or routines could you start (or stop) that would support this new goal?', 'textarea'),
	('What is one small step you could take today to move closer to this goal?', 'textarea'),
	('How will you measure success along this journey, and what will keep you motivated to push through challenges?', 'textarea');
        """)
   

def insert_data():
   return insert_query(sql_insert_data())


def get_data():
   print(f"GET DATA ------------------- {os.environ.get('SQLITE')} -----------------------")
   return execute_query(sql_get_data())


if __name__ == "__main__":
   pprint.pprint(get_data())