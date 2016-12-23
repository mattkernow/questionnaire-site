from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=250)


class Questionnaire(models.Model):
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_open = models.BooleanField()


class QuestionnaireQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class OfferedAnswer(models.Model):
    answer_text = models.CharField(max_length=200)


class QuestionnaireQuestionAnswer(models.Model):
    questionnaire_question = models.ForeignKey(QuestionnaireQuestion, on_delete=models.CASCADE)
    offered_answer = models.ForeignKey(OfferedAnswer, on_delete=models.CASCADE)


class Answer(models.Model):
    questionnaire_question_answer = models.ForeignKey(QuestionnaireQuestionAnswer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
