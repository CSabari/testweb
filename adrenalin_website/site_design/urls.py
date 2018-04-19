from django.conf.urls import url
from site_design import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
	url(r'^contact/$', views.ContactPageView.as_view()),
]