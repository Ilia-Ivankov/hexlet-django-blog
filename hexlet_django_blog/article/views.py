from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from .models import Article
from .forms import ArticleForm


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            messages.success(request, "Статья успешно сохранена")
            form.save()
            return redirect("articles_index_view")
        else:
            messages.warning(request, "Есть ошибки, проверьте")
            return render(request, "articles/create.html", {"form": form})


class ArticleUpdateView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        form = ArticleForm(instance=article)
        return render(request, "articles/update.html", {"form": form, "article": article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            messages.success(request, "Статья успешно обновлена")
            form.save()
            return redirect("article", id=article.id)
        else:
            messages.warning(request, "Есть ошибки, проверьте")
            return render(request, "articles/update.html", {"form": form, "article": article})


class ArticleDeleteView(View):
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        article.delete()
        messages.success(request, "Статья успешно удалена")
        return redirect("article_index_view")
