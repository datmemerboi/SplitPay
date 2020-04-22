from django.shortcuts import render

# Create your views here.
def newExpenseFn(request):
	return render( request, "new expense.html", {'title': "New Expense"})