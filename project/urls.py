from django.urls import path
from .views import *
urlpatterns = [
    path('',user_create,name='create'),
    path('list/', user_list,name='user_list'),
    path('update/<int:id>/',user_update,name='update'),
    path('delete/<int:id>/',user_delete,name='delete'),
    # path('jsonlist',user_list_json,name='user_list_json'),

]