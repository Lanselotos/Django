from django.urls import path

from service.views import index, page, about, json_show


urlpatterns = [
    path('', index, name = 'service'),
    path('service/<int:page_num>', page),
    path('about/<int:id>', about, name = 'about'),
    path('json', json_show, name='json_show')
]
    