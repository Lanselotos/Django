from django.urls import path, path

from service.views import index, page, about


urlpatterns = [
    path('service/', index),
    path('service/<int:page_num>', page),
    path('about/<int:id>', about, name = 'about'),
]
    