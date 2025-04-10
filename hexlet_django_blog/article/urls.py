from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("<int:id>/", views.ArticleView.as_view(), name="article"),
    path("", views.IndexView.as_view(), name="articles_index_view"),
    path("create/", views.ArticleFormCreateView.as_view(), name="articles_create"),
    path("<int:id>/update/", views.ArticleUpdateView.as_view(), name="article_update"),
    path("<int:id>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),
]
