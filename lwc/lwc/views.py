from django.shortcuts import render

def testpage(request):
	context = {}
 	template = "frontpage.html"
 	return render(request, template, context)