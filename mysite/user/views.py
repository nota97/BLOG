from asyncio.windows_events import NULL
from email import message
from http.client import HTTP_PORT
from rest_framework import status
from multiprocessing import AuthenticationError
from urllib import response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user
from .serializers import userSerializer
from rest_framework.authentication import BaseAuthentication
import uuid
# Create your views here.


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        q_method = request.META['REQUEST_METHOD'] 
        # GET请求不认证
        if q_method == 'GET':
            return NULL,NULL
        if not token:
            raise AuthenticationError({"code" :1000, "error": "认证失败"})
        user_object = user.objects.filter(token = token).first()
        if not user_object:
            raise AuthenticationError({"code" :1001, "error": "认证失败"})
        return user_object, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class userViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [MyAuthentication, ]
    queryset = user.objects.all()
    serializer_class = userSerializer


class loginView(APIView):
    # 登录认证
    def post(self, request, *args, **kawargs):
        username = request.data.get('user')
        password = request.data.get('password')
        
        user_object = user.objects.filter(user = username, password = password).first()
        if not user_object:
            return Response({"code": 1000, "data":"账号或密码错误"})
        token = str(uuid.uuid4())
        user_object.token = token
        user_object.save()
        return Response({"code": 200, "data": {"user": username, "token": token, "nickname" : user_object.nickname}})


