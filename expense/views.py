from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect

def newExpenseFn(request):
	return render( request, "new expense.html", {'title': "New Expense"})

@csrf_exempt
def createExpenseFn(request):
	csrfContext = RequestContext(request)
	print( request.method )
	print( request.POST['name'])
	print( request.POST.getlist('actors') )
	return HttpResponse('Success')