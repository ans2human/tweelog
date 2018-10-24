from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .mixins import FormUserNeededMixin
from .forms import TweetModelForm
from .models import Tweet
# Create your views here.


class TweetCreateView(FormUserNeededMixin,CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = "/tweet/create/"


class TweetUpdateView(LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	success_url = "/tweet/"
	template_name = "tweets/update_view.html"


class TweetDeleteView(DeleteView):
	model = Tweet
	template_name = "tweets/delete_view.html"
	success_url = reverse_lazy("home")


def tweet_detail_view(request, pk=None):
	obje = get_object_or_404(Tweet, pk=pk)
	print(obje)
	print(request.user)
	context = {
		"objc": obje 
	}
	return render(request, 'tweets/detail_view.html', context)




def tweet_list_view(request):
	obj = Tweet.objects.all()
	print(obj)
	print(request.user)
	context = {

		"object": obj
	}
	return render(request, 'tweets/list_view.html', context)

