from django.contrib import admin
from questionnaire_app.models import ModuleSubmission, MapActionModule, Question, Answer

admin.site.register(ModuleSubmission)
admin.site.register(MapActionModule)
admin.site.register(Answer)
admin.site.register(Question)
