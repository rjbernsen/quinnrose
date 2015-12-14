from django.conf.urls import url

from organization.views import OrganizationPage

urlpatterns = [
    url(r'^/(?P<organization_id>.+)?$', OrganizationPage.as_view(), name='organization'),
#     url(r'^about/?(?P<section>.+)?$', About.as_view(), name='about'),
#     url(r'^contact$', ContactFormView.as_view(), name='contact'),
#     url(r'^signin/?(?P<subtype>.+)?$', SignInFormView.as_view(), name='signin'),
#     url(r'^subscriptions/?(?P<subtype>.+)?$', Subscriptions.as_view(), name='subscriptions'),
#     url(r'^help/?(?P<section>.+)?$', Help.as_view(), name='help'),
#     url(r'^privacy$', Privacy.as_view(), name='privacy'),
#     url(r'^terms$', Terms.as_view(), name='terms'),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^artists/', include('artists.urls')),
#     url(r'^.+$', Error404.as_view(), name='404'),
]

