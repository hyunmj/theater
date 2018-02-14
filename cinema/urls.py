from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home_page,name='home_page'),
	url(r'^search_page$',views.search_page,name='search_page'),
	url(r'search_page$',views.search_page,name='search_page'),
	url(r'^search_page',views.search_page,name='search_page'),
]