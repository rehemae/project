from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from  api.serializers import UserSerializer, MyTokenObtainPairSerializer, ProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model
from api.models import Profile

User = get_user_model()

@api_view(['GET'])
def get_auth_apis(request):
    routes = [
        {
            "method": "GET",
            "url": "api/token/",
            "description": "getting tokens for authentication/logging user"
        },
        {
            "method": "GET",
            "url": "api/token/refresh/",
            "description": "getting refresh token for access"
        },
        {
            "method": "POST",
            "url": "api/signup/",
            "description": "register a user"
        },
        {
            "method": "GET",
            "url": "api/questions/",
            "description": "getting all questions"
        },
        {
            "method": "POST",
            "url": "api/create-question/",
            "description": "creating a question"
        },
        {
            "method": "GET",
            "url": "api/question/<int:pk>/",
            "description": "getting a single question"
        },
        {
            "method": "PUT",
            "url": "api/question/<int:pk>/update",
            "description": "updating a single question"
        },
        {
            "method": "DELETE",
            "url": "api/question/<int:pk>/delete",
            "description": "deleting a single question"
        },
        {
            "method": "GET",
            "url": "api/choices",
            "description": "getting all choices"
        },
        {
            "method": "POST",
            "url": "api/question/<int:pk>/choice/",
            "description": "submitting a choice or answer from a given question"
        },
        
    ]

    return Response(routes)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def create_user(request):
    print(request.data)
    username = request.data['username']
    email = request.data['email']
    county = request.data['county']
    association = request.data['association']
    password1 = request.data['password1']
    password2 = request.data['password2']
    if password1 == password2:
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        user_profile = Profile.objects.get(user=user)
        user_profile.user = user
        user_profile.county = county
        user_profile.association = association
        user_profile.save()
    else:
        return Response("password do not match")
    return Response("registred")
    