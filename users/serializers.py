from django.contrib.auth.models import User
from rest_framework import serializers
# from posts.models import MessageByChat
from accounts.models import Users,BookstoreSeller, MessageByChat


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Users.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=Users.objects.all())

    class Meta:
        model = MessageByChat
        fields = ['sender', 'receiver', 'message', 'timestamp']
