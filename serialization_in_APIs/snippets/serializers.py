from rest_framework import serializers
from snippets.models import Snippet , LANGUAGE_CHOICES , STYLE_CHOICES
from django.contrib.auth.models import User
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length = 100 , required = False , allow_blank = True)
#     code = serializers.CharField(style = {'base_template' : 'textarea.html'})
#     linenos = serializers.BooleanField(required = False)
#     language = serializers.ChoiceField(choices = LANGUAGE_CHOICES , default = 'python')
#     style = serializers.ChoiceField(choices = STYLE_CHOICES , default = 'friendly')
#
#     def create(self,validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self , instance , validated_data):
#         instance.title = validated_data.get('title' , instance.title)
#         instance.code = validated_data.get('title' , isntance.code)
#         instance.linenos = validated_data.get('linenos' , instance.linenos)
#         instance.language = validated_data.get('language' , instance.language)
#         instance.style = validated_data.get('style' , instance.style)
#         isntance.save()
#         return instance
#
#     def __str__(self):
#         return self.code


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight' , format = 'html')
    class Meta:
        model = Snippet
        fields = ['url' , 'highlight' , 'id' , 'title' , 'code' , 'owner' , 'linenos' , 'language' , 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many = True , view_name = 'snippet-detail' , read_only = True)

    class Meta:
        model = User
        fields = ['id' , 'username' , 'snippets']