from django.conf.urls import include, url
from django.contrib import admin
from clock import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'countdown.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home_page, name='home')

]
