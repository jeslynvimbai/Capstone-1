from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'band'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('band-members/', views.band_members, name='band_members'),
    path('events/', views.events, name='events'),
    path('accounts/', views.user_profile, name='user_profile'),  
      # Login and Logout URLs
    path('login/', LoginView.as_view(template_name='band/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Signup URL
    path('signup/', views.signup, name='signup'),
]


