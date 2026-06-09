from django.http import HttpResponse


def first(request):
    return HttpResponse('<h1>My first django</h1>')
def second(request):
    return HttpResponse('<h2>second<h2/>')