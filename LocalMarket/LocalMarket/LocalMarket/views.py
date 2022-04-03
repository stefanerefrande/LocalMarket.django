from django.http import HttpResponse


def index(request):
    return HttpResponse("Starting Local Market App")
