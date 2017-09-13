from django.conf.urls import url
from appAnywhere import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^lista/$', views.HomePageView_lists.as_view()),
]
