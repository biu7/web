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

        def restore_object(self, attrs, instance=None):
            if instance:
                instance.title = attrs['title']
                instance.author = attrs['author']
                instance.time = attrs['time']
                instance.content = attrs['content']
                instance.imgsrc = attrs['imgsrc']
                return instance

            return News(**attrs)
class CommentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'