import tweepy

from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView, PasswordResetView
from allauth.account.views import SignupView
from allauth.account.forms import LoginForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from django.conf import settings

#from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
#from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
#from rest_auth.registration.views import SocialLoginView

#class FacebookLogin(SocialLoginView):
 #   adapter_class = FacebookOAuth2Adapter
#class TwitterLogin(SocialLoginView):
 #   adapter_class = TwitterOAuthAdapter

class Home(TemplateView):
    template_name = 'home.html'
class HomeView(TemplateView):
    template_name = 'home.html'

class MySignupView(SignupView):
    template_name = 'signup.html'

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

class CustomSignupView(SignupView):
    # here we add some context to the already existing context
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomSignupView,
                        self).get_context_data(**kwargs)
        context['login_form'] = LoginForm()  # add form to context
        return context


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



class PostViews(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data["tweet_post"])
            auth = tweepy.OAuthHandler(
            settings.API_KEY,settings.API_SECRET
            )
            auth.set_access_token(
            settings.ACCESS_TOKEN,
            settings.ACCESS_TOKEN_SECRET
            )
            api = tweepy.API(auth)
            data2 =api.update_status(serializer.data["tweet_post"] )
            print(data2)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   
          
      
            