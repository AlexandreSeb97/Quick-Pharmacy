from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
def home(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'wep_app/index.html',
		context_instance = RequestContext(request,
		{
			'title': 'Home',
			'yeR': datetime.now().year,
		})
	)
