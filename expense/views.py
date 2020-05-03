from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import Expense
import json

def newExpenseFn(request):
	return render( request, "new expense.html", {'title': "New Expense"})

@csrf_exempt
def createExpenseFn(request):
	csrfContext = RequestContext(request)
	eobj = Expense();
	eobj.set_name( request.POST['name'] )
	eobj.set_actors( request.POST.getlist('actors[]') )
	eobj.save()
	print( Expense.objects.all() )

	if( request.POST.getlist('actors[]') != [] ):
		return HttpResponse('Success')
	else:
		return HttpResponse('Failure')

def allExpenseFn(request):
	allExpense = []
	for i in Expense.objects.all():
		di = { 'name':i.name, 'actors':json.loads(i.actors), 'dateTime':i.dateTime }
		allExpense.append( di )
	return render( request, "all expense.htm.j2", { 'allExpense':allExpense })