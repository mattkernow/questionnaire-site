from django.shortcuts import render
from questionnaire_app.models import Questionnaire


def index(request):
    """
    Return the home page
    :param request: request object
    :return: rendered template
    """
    filter_questionnaires = Questionnaire.objects.filter(is_open=True).order_by('end_date')
    questionnaires = {'questionnaires': filter_questionnaires}
    return render(request, 'index.html', context=questionnaires)
