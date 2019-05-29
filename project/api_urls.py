from django.urls import path,include
from rest_framework import routers
from .api_views import *
#router=routers.DefaultRouter()
#router.register('',UserViewSet)

urlpatterns=[
    path('',UserListApiView.as_view(),name='user-list-api'),
    path('<int:pk>/',UserDetailApiView.as_view(),name='user-detail-api'),
    path('<int:pk>/edit',UserUpdateApiView.as_view(),name='user-update-api'),
    path('<int:pk>/delete',UserDeleteApiView.as_view(),name='user-delete-api')
    #path('user',include(router.urls))
]
