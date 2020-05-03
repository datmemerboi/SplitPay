from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import Expense

def newExpenseFn(request):
	return render( request, "new expense.html", {'title': "New Expense"})

@csrf_exempt
def createExpenseFn(request):
	csrfContext = RequestContext(request)
	print( request.method )
	print( request.POST['name'] )
	print( request.POST.getlist('actors[]') )

	eobj = Expense();
	eobj.set_Name( request.POST['name'] )
	ebj.set_Actors( request.POST.getlist('actors[]') )

	if( request.POST.getlist('actors[]') != [] ):
		return HttpResponse('Success')
	else:
		return HttpResponse('Failure')

def allExpenseFn(request):
	return render( request, "all expense.htm.j2")