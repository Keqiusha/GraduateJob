from django.conf.urls import url
# 添加路由
from . import views
urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url('index/', views.index),
    url('cardtest', views.cardtest),
    url('logout/', views.logout),
]