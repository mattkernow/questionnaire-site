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


def questionnaire(request, questionnaire_id):
    """
    Returns a questionnaire page
    :param request: request object
    :param questionnaire_id: Primary key of questionnaire requested
    :return: rendered template
    """
    id_as_int = int(questionnaire_id)
    filter_questionnaire = Questionnaire.objects.get(pk=id_as_int)
    questionnaire_dict = {'questionnaire': filter_questionnaire}
    return render(request, 'questionnaire.html', context=questionnaire_dict)
