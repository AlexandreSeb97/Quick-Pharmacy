from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'web_app.views.home', name='home'),
)