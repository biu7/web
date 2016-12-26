from rest_framework import serializers

from news.models import *


class CatagorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'

class NewsSerialize(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CommentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'