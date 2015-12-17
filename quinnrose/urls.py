"""quinnrose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from quinnrose.views import HomePage, ContactFormView, About, Help, SignInFormView, Subscriptions, Privacy, Terms, Error404

handler404 ='quinnrose.views.error404'

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^about/?(?P<section>.+)?$', About.as_view(), name='about'),
    url(r'^contact$', ContactFormView.as_view(), name='contact'),
    url(r'^signin/?(?P<subtype>.+)?$', SignInFormView.as_view(), name='signin'),
    url(r'^subscriptions/?(?P<subtype>.+)?$', Subscriptions.as_view(), name='subscriptions'),
    url(r'^help/?(?P<section>.+)?$', Help.as_view(), name='help'),
    url(r'^privacy$', Privacy.as_view(), name='privacy'),
    url(r'^terms$', Terms.as_view(), name='terms'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artist', include('artist.urls')),
    url(r'^organization', include('organization.urls')),
    url(r'^community', include('community.urls')),
    url(r'^.+$', Error404.as_view(), name='404'),
]

