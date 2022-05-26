from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentCreate.as_view()),
    path('export/', views.export_excel),

]
