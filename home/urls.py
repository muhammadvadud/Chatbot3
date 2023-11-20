from django.urls import path
from .views import HomePageView, ChatbotView,ProfilebotView,RegisterbotView

app_name='home'
urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('chat/', ChatbotView.as_view(), name="chat"),
    path('profile/', ProfilebotView.as_view(), name="profile"),
    path('register/', RegisterbotView.as_view(), name="register"),

]
