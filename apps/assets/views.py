from rest_framework import viewsets
from rest_framework import mixins

from .serializers import ServerInfoSerializer
# Create your views here.


class ServerInfoViewSet(viewsets.ModelViewSet):
    """
    list:
        获取服务器列表
    create:
        创建新的服务器
    delete:
        删除服务器
    """

    queryset = ServerInfoSerializer()
    serializer_class = ServerInfoSerializer