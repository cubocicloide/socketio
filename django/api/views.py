from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes((AllowAny,))
def hello(request):
    return Response({ 'message': 'hello world' }, status=status.HTTP_200_OK)
