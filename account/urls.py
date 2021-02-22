from django.urls import path,include

from account.views import SignUpView, UserDetailView, UserUpdateView,password_reset_complete

urlpatterns = [
    path('',include("django.contrib.auth.urls")),
    
    path("SignUp",SignUpView.as_view(),name='Sign Up'),

    path("<int:pk>",UserDetailView.as_view(),name='Details'),

    path('<int:pk>/Update',UserUpdateView.as_view(),name='Update'),

    path('password_reset_complete',password_reset_complete,name='password_reset_complete'),
]