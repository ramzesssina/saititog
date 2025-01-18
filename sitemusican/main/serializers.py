import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Musician

'''class MusicianModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content'''

class MusicianSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Musician
        fields = "__all__"


'''def encode():
    model = MusicianModel('Vitya Ak', 'Content: Vitya Ak')
    model_sr = MusicianSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"Vitya Ak","content":"Content: Vitya Ak"}')
    data = JSONParser().parse(stream)
    serializer = MusicianSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)'''