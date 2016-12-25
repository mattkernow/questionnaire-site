from django.contrib import admin
from questionnaire_app.models import Questionnaire, QuestionnaireQuestion, Question


class QuestionnaireQuestionInline(admin.TabularInline):
    model = QuestionnaireQuestion


class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [QuestionnaireQuestionInline]

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question)
