from django.http import HttpResponse

def index(request):
    return HttpResponse('Скоро здесь будут инструкции')

def question(request):
    return HttpResponse('Скоро здесь будут ответы на частые вопросы')