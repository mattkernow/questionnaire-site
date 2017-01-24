from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Describes a question.
    """
    question_text = models.CharField(max_length=250)
    module = models.ForeignKey(Module)
    choice_one = models.CharField(max_length=50)
    choice_two = models.CharField(max_length=50)
    choice_three = models.CharField(max_length=50)
    choice_four = models.CharField(max_length=50)
    choice_five = models.CharField(max_length=50)
    correct_choice = models.IntegerField()

    def __str__(self):
        return self.question_text


class MapActionModule(models.Model):
    """
    Describes a MapAction module.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    description = models.CharField()


class ModuleSubmission(models.Model):
    """
    Describes a users questionnaire submission.
    """
    submission_date = models.DateTimeField(auto_now_add=True)
    # Score out of 10
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    """
    Describes an answer to a question.
    """
    question = models.ForeignKey(Question)
    module = models.ForeignKey(Module)
    answer_choice = models.IntegerField()
