from django.conf.urls import url

from quinnrose.views import Error404
from community.views import ListPage, PostPage, NewPostPage

urlpatterns = [
    url(r'^$', ListPage.as_view(), name='community'),
    url(r'^/new$', NewPostPage.as_view(), name='new'),
    url(r'^/post/(?P<entry_id>.+)$', PostPage.as_view(), name='post'),
    url(r'^/about$', Error404.as_view(), name='about'),
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

