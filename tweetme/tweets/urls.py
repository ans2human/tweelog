from django.conf.urls import url

from .views import tweet_list_view,tweet_detail_view, TweetCreateView, TweetUpdateView, TweetDeleteView


urlpatterns = [

	url(r'^$', tweet_list_view, name='list'),
	url(r'^create/$', TweetCreateView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
	url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]