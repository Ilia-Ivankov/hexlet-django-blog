from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from .apps import ArticleConfig
from django.views import View
from django.views.generic.base import TemplateView


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        tags = kwargs.get("tags")
        article_id = kwargs.get("article_id")

        if tags and article_id:
            text = f"Статья номер {article_id}. Тег {tags}"

        return render(request, "articles/article.html", context={"text": text})


class ArticleIndexView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        app_name = ArticleConfig.name.split(".")[-1]
        context["app_name"] = app_name
        return context
