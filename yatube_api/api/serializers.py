import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = (
            "pub_date",
            "author",
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "author",
            "created",
        )


'''class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='following', queryset=User.objects.all())# queryset=User.objects.all())

    def validate(self, data):
        if data['username'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data

    class Meta:
        model = Follow
        fields = "__all__"'''


'''class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    def validate(self, data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        if data[user] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]'''
class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    validators = (UniqueTogetherValidator(
        queryset=Follow.objects.all(),
        fields=['user', 'following']),
    )

    def validate(self, data):
        if data.get('following') == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow
