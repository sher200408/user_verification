
from django.urls import path

from one.views import PostListViews

urlpatterns = [
    path('one1/', PostListViews.as_view(), name="one"),
]