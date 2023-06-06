from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image
from rest_framework import status

@api_view(['DELETE'])
def image_detail(request, image_id):
    print('salut')
    try:
        image = Image.objects.all().get(image_id = image_id)
    except Image.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    image.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)

