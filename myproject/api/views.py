from django.shortcuts import render
from django.http import JsonResponse
from django.template.context_processors import request


# Create your views here.
def ping(request):
    return  JsonResponse({'message': 'pong'})
def Sum_numbers(request):
    try:
        a = int(request.GET.get("a", 0))
        b = int(request.GET.get("b", 0))
        result = a+b
    except ValueError:
        return JsonResponse({'error': "Invalid input"},status=400)
    return JsonResponse({"result":result})


