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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from quinnrose.views import HomePage, ContactFormView, About, Search, Help, SignInFormView, Subscriptions, Subscribe, Privacy, Terms, Error404
from quinnrose.ajax_handlers import session_handler, geonames_handler, pdf_handler

admin.autodiscover()

handler404 ='quinnrose.views.error404'

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^about/?(?P<section>.+)?$', About.as_view(), name='about'),
    url(r'^contact$', ContactFormView.as_view(), name='contact'),
    url(r'^signin/?(?P<subtype>.+)?$', SignInFormView.as_view(), name='signin'),
    url(r'^search/?(?P<subtype>.+)?$', Search.as_view(), name='search'),
    url(r'^subscriptions/?(?P<subtype>.+)?$', Subscriptions.as_view(), name='subscriptions'),
    url(r'^subscribe/?(?P<subtype>.+)?$', Subscribe.as_view(), name='subscribe'),
    url(r'^help/?(?P<section>.+)/(?P<help_app>.+)?$', Help.as_view(), name='help'),
    url(r'^help/?(?P<section>.+)?$', Help.as_view(), {'help_app': None}, name='help'),
    url(r'^privacy$', Privacy.as_view(), name='privacy'),
    url(r'^terms$', Terms.as_view(), name='terms'),
    url(r'^artist', include('artist.urls')),
    url(r'^organization', include('organization.urls')),
    url(r'^community', include('community.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session_post', session_handler, name="session_handler"),
    url(r'^geonames', geonames_handler, name="geonames_handler"),
    url(r'^get_pdf', pdf_handler, name="pdf_handler"),

    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)[0],
    url(r'^.+$', Error404.as_view(), name='404')
]



