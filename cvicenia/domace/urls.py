from django.urls import path
from . import views

urlpatterns = [
    path("domace/", views.domace, name="domace"),
    path('vizitka/', views.du2_, name = "du2_"),
]