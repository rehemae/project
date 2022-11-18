from rest_framework import serializers

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Choice, Question, ForumComment, Forum, ForumVote
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already exists")
        return lower_email
    
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password':{'write-only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        
        

        return token


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question',)

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id','choice',)
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('id','username', 'title', 'text','created')
        extra_kwargs = {
                    'username': {'read_only': True},
                }


class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = ('id','forum', 'username', 'comment', 'created')
        extra_kwargs = {
                    'username': {'read_only': True},
                    'forum':{'read_only':True},
                    'id':{'read_only':True},
                    'created':{'read_only':True},
                }

class ForumVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumVote
        fields = ('id','forum', 'username', 'up_vote', 'down_vote')
        extra_kwargs = {
                    'username': {'read_only': True},
                    'forum':{'read_only':True},
                    'id':{'read_only':True}
                }

















