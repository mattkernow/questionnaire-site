from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=250)


class Questionnaire(models.Model):
    members = models.ManyToManyField(
        Question,
        through='SurveyQuestion',
        through_fields=('question', 'questionnaire'),
    )
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_open = models.BooleanField()


class SurveyQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
