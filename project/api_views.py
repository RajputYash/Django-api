from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .serializers import UserSerializer,UserUpdateSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import UserData
from .pagination import UserLimitOffSetPagination,UsrPageNumberPagination

class UserListApiView(ListAPIView):
    queryset=UserData.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['first_name','last_name']
    pagination_class = UserLimitOffSetPagination
    pagination_class=UsrPageNumberPagination


class UserDetailApiView(RetrieveAPIView):
    queryset=UserData.objects.all()
    serializer_class = UserSerializer

class UserUpdateApiView(UpdateAPIView):
    queryset=UserData.objects.all()
    serializer_class = UserUpdateSerializer

class UserDeleteApiView(DestroyAPIView):
    queryset=UserData.objects.all()
    serializer_class = UserSerializer