from django.shortcuts import render
from questionnaire_app.models import MapActionModule, ModuleSubmission


def index(request):
    """
    Return the home page
    :param request: request object
    :return: rendered template
    """
    modules = MapActionModule.objects.filter().order_by('id')
    submissions = ModuleSubmission.objects.filter(user=request.user).order_by('module', '-submission_date').distinct('module')
    return render(request, 'index.html', {'modules': modules, 'submissions': submissions})


# def questionnaire(request, questionnaire_id):
#     """
#     Returns a questionnaire page
#     :param request: request object
#     :param questionnaire_id: Primary key of questionnaire requested
#     :return: rendered template
#     """
#     id_as_int = int(questionnaire_id)
#     filter_questionnaire = Questionnaire.objects.get(pk=id_as_int)
#     questionnaire_dict = {'questionnaire': filter_questionnaire}
#     return render(request, 'questionnaire.html', context=questionnaire_dict)
