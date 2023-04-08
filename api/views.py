from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def home(req: WSGIRequest):
    return JsonResponse({"info": req.path})
