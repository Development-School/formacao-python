
from django.http import HttpResponse

from django.http import JsonResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("Hello, world!")

def get(request):
    return JsonResponse({'message': 'Olá mundo!'})
