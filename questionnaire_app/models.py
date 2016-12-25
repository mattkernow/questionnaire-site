from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Describes a question.
    """
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text


class Questionnaire(models.Model):
    """
    Describes a questionnaire.
    """
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_open = models.BooleanField()

    def __str__(self):
        return self.description


class QuestionnaireQuestion(models.Model):
    """
    Links a question to a questionnaire.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    class Meta:
        """
        A questionnaire must have unique questions.
        """
        unique_together = ['question', 'questionnaire']

    def __str__(self):
        return '{} ({}) - Q: {}'.format(self.questionnaire, self.questionnaire.id, self.question.question_text)


class OfferedAnswer(models.Model):
    """
    Describes an answer to a question.
    """
    answer_text = models.CharField(max_length=200)


class QuestionnaireQuestionAnswer(models.Model):
    """
    Links an answer to a questionnaire question.
    """
    questionnaire_question = models.ForeignKey(QuestionnaireQuestion, on_delete=models.CASCADE)
    offered_answer = models.ForeignKey(OfferedAnswer, on_delete=models.CASCADE)


class Answer(models.Model):
    """
    Links a questionnaire question answer to a user.
    """
    questionnaire_question_answer = models.ForeignKey(QuestionnaireQuestionAnswer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
