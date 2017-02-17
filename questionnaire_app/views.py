from django.shortcuts import render
from questionnaire_app.models import MapActionModule, ModuleSubmission, Question
from questionnaire_app.forms import QuestionAnswerForm
import random


def index(request):
    """
    Return the home page
    :param request: request object
    :return: rendered template
    """
    modules = MapActionModule.objects.filter().order_by('id')
    submissions = ModuleSubmission.objects.filter(user=request.user).order_by('module', '-submission_date').distinct('module')
    return render(request, 'index.html', {'modules': modules, 'submissions': submissions})


def take_module_test(request, module_id):
    """
    Returns a questionnaire page
    :param request: request object
    :param questionnaire_id: Primary key of questionnaire requested
    :return: rendered template
    """
    ma_module = MapActionModule.objects.get(pk=module_id)
    questions = Question.objects.filter(module__id=module_id)

    # Get 10 random questions
    if questions.count() > 10:
        for x in range(10):
            questions = random.sample(list(questions), 10)

    question_answer_form = QuestionAnswerForm(question_id=2)

    context_dict = {'ma_module': ma_module,
                    'questions': questions,
                    'question_form': question_answer_form}
    return render(request, 'ma_module.html', context=context_dict)
