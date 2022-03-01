"""SocialAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import SignupView
from SocialMyapp.views import  Home,HomeView
#from SocialMyapp.views import FacebookLogin
#from SocialMyapp.views import TwitterLogin
from django.conf import settings
from django.conf.urls.static import static
from SocialMyapp.views import RegisterAPI
from knox import views as knox_views
from SocialMyapp.views import LoginAPI
from SocialMyapp.views import PostViews


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    #path('rest-auth/', include('rest_auth.urls')),
    path("", Home.as_view(), name="indexes"),
    path("index", HomeView.as_view(), name="home"),
    #path("sociallist/",SignupView.as_view()),
     path('api/register/', RegisterAPI.as_view(), name='register'),
     path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('Post-tweet/', PostViews.as_view())

    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    #path('rest-auth/google/', TwitterLogin.as_view(), name='twitter_login')
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

