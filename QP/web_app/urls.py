from django.conf.urls import patterns, url

urlpatterns = patterns('web_app.views',
	url(r'^accueil$', 'home'),
	url(r'^index$', 'index'),
	url(r'^about$', 'sources'),
)