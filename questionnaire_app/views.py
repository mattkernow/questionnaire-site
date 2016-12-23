from django.shortcuts import render


def index(request):
    """
    Return the home page
    :param request: request object
    :return: rendered template
    """
    return render(request, 'index.html')
