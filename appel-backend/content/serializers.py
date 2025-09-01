from rest_framework import serializers
from .models import Slide

class SlideSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Slide
        fields = ('id','src','alt','caption')

    def get_src(self, obj):
        request = self.context.get('request')
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url
