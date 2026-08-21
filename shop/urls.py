from django.urls import path
from shop import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
  path('', views.index, name='index'),
  path('banner/', views.banner_view),
  # path('login/', TokenObtainPairView.as_view()),
  path('register/', views.MemberRegisterView.as_view()),
  path('login/', views.MemberLoginView.as_view()),
  path('banner/', views.BannerListView.as_view(), name='banner'),
]
