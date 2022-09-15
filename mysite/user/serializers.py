from rest_framework import serializers
from user.models import user


class userSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = user
        fields = "__all__"