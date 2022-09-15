from rest_framework import serializers
from blogs.models import blogs


class blogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = blogs
        fields = "__all__"