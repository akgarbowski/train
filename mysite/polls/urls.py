from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("calvin/<str:message>", views.calvin, name="calvin"),
    # path("add/<int:num1>/<int:num2>", views.calvin, name="calvin"),
]

