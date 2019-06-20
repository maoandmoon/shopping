from django.conf.urls import url
from . import views

app_name = 'customers'

urlpatterns=[
    url(r'^user_register/$', views.user_register, name='user_register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^user_account/', views.user_account, name='user_account'),
]