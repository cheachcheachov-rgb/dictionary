from rest_framework import serializers
from .models import Word


class WordSerializer(serializers.ModelSerializer):
    language_display = serializers.CharField(source='get_language_display', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Word
        fields = ['id', 'word', 'translation', 'example', 'language', 'language_display', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None