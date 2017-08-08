from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^about/', views.about, name='About'),
    url(r'^$', views.index, name='Index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]
