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
        future_question = Question(question_text='Quen es el mejor Course Director de Platzi?', pub_date=time)
        self.assertIS(future_question.was_published_recently(), False)