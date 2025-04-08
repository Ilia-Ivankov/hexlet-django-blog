from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

def about(request):
    return render(request, "about.html")
