from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpRequest


# Create your views here.
def home(request):
		assert isinstance(request, HttpRequest)
		return render(
			request,
			'web_app/index.html',
			context_instance = RequestContext(request,
			{
				'title': 'accueil',
			})
		)

def view_Rx(request, id_Pharmacy):
	text= "You asked for this Pharmacy:"
	return HttpResponse(text)

def list_Rx(request, district):
	text="You asked for all Pharmacies in this area: {0}.".format(area)
	return HttpResponse(text)

def sources(request):
	return render_to_response('index.html')

def results(request):
	assert isinstance(request, HttpRequest)
	return render(request, 'web_app/index.html', context)