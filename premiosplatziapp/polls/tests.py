import datetime


from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

# Modelos
# Vistas

class QuestionModelTest(TestCase): 

    def test_was_published_recently_with_future_questions(self):
        """"was_published_recently returns False for questions whose pub_datew in inthe future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question =  Question(question_text="¿Quien es el mejor Course Direct de Platzi?",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
                                   
    def test_was_published_recently_with_past_questions(self):
        """was_published_recently() must return Flase for questions whose pub_date is more than 1 day in the past"""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text="¿Quien es el mejor Course Direct de Platzi?",pub_date=time)
        self.assertIs(past_question.was_published_recently(),False)
        
    def test_was_published_recently_with_present_questions(self):
        """was_published_recently() must return True for questions whose pub_date is actual"""
        time = timezone.now()
        present_question = Question(question_text="¿Quien es el mejor Course Direct de Platzi?",pub_date=time)
        self.assertIs(present_question.was_published_recently(),True)                                