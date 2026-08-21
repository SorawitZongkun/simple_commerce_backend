import json
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import permissions
from shop.models import Banner, Member
from shop.serializers import MemberCreateSerializer, MemberLoginSerializer, BannerSerializer


from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


def index(request):
  return HttpResponse("Hello world, from shop index")

def banner_view(request):
  data = []
  for banner in Banner.objects.all():
    data.append({
    "id": banner.id,
    "image": request.build_absolute_uri(banner.image.url),
    })
  return HttpResponse(json.dumps(data))

class MemberRegisterView(CreateAPIView):
  queryset = Member.objects.all()
  serializer_class = MemberCreateSerializer
  permission_classes = [permissions.AllowAny]

class MemberLoginView(TokenObtainPairView):
  queryset = User.objects.all()
  serializer_class = MemberLoginSerializer

class BannerListView(ListAPIView):
  queryset = Banner.objects.all()
  serializer_class = BannerSerializer