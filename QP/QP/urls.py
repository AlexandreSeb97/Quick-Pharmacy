from django.conf.urls import patterns, include, url
from web_app import views

urlpatterns = patterns('',
    url(r'^web_app/', include('web_app.urls')),
)

