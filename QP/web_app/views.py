from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
def home(request):
	asseert isinstance(request, HttpRequest)
	return render(
		request,
		'wep_app/index.html',
		context_instance = RequestContext(request,
		{
			title: 'Home',
		})
	)
def resultats(request):
	text="""<!DOCTYPE html>
		 <html>
		 <head>
			<meta charset="utf-8"/>
			<title> Resultats de la recherche</title>
			<link rel="stylesheet" type="text/css" href="base.css" />
		 </head>
		 <body>
			<h1 id="one"> QuickPharma </h1>
			<p><Dans cette page vous retrouverez les resultats de votre recherche</p>
		</body>
		</html>"""
	return HttpResponse(text)