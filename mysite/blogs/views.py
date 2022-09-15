from django.shortcuts import render
from rest_framework import viewsets
from .models import blogs
from .serializers import blogsSerializer
from user.views import MyAuthentication
# Create your views here.

class blogsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [MyAuthentication, ]
    queryset = blogs.objects.all().order_by('-post_time')
    serializer_class = blogsSerializer
