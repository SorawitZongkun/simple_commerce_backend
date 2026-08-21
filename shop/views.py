# from django.http import HttpResponse
# def index(request):
#   return HttpResponse("Hello world, from shop index")

import json
from django.http import HttpResponse
from shop.models import Banner

def banner_view(request):
  data = []
  for banner in Banner.objects.all():
    data.append({
    "id": banner.id,
    "image": request.build_absolute_uri(banner.image.url),
    })
  return HttpResponse(json.dumps(data))