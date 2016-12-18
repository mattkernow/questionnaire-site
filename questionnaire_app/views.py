from django.template.loader import get_template
from django.template import Template
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    template = get_template('login.html')
    return HttpResponse(template.render({}))
