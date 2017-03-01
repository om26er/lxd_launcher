from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from pylxd import Client


class ContainerView(APIView):
    def get(self, *args, **kwargs):
        containers = Client().containers.all()
        data = {}
        for container in containers:
            data.update({'name': container.name, 'status': container.status})
        return Response(data=data, status=status.HTTP_200_OK)
