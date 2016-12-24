from django.contrib import admin
from questionnaire_app.models import Question, Questionnaire, QuestionnaireQuestion


@admin.register(Question, Questionnaire, QuestionnaireQuestion)
class AuthorAdmin(admin.ModelAdmin):
    """
    Register the question/questionnaire classes with django's admin.
    """
    pass
