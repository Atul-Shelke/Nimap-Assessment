from django.urls import path
from .import views
urlpatterns = [
    path('register',views.registerView.as_view(),name='register'),
    path('login',views.loginView.as_view(),name='login')
]
