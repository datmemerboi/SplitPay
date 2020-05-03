from django.urls import path
from . import views

urlpatterns = [
	path('new/', views.newExpenseFn, name="new expense"),
	path('create/', views.createExpenseFn, name="create expense"),
	path('all/', views.allExpenseFn, name="all expenses"),
]