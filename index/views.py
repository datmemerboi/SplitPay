from django.shortcuts import render

def indexFn(request):
	return render( request, "index.html", {'title':"Index"} )