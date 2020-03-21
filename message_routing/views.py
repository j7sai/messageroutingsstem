from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F,Q,Value,CharField
from rest_framework.generics import *

ERROR_FORMAT = {
    "message":"",
    "param":""
}

@api_view(['GET', 'POST'])
def gatewayview(request,id=''):
    if request.method == 'GET':
        try:
            if id!='':
                gateway = Gateway.objects.get(pk=id)
                serializer = GatewaySerializer(gateway)
                data = serializer.data
                listAddress = IPaddress.objects.filter(
                    Q(gatewayId=serializer.data.get('id', None)
                      )).values_list("address", flat=True)
                data["ip_addressess"] = listAddress
            else:
                gateway = Gateway.objects.all()
                serializer = GatewaySerializer(gateway,many=True)
                data = serializer.data
        except Gateway.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(data)

    if request.method == 'POST':
        gateway_data = request.data
        serializer = GatewaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouterView(RetrieveAPIView,CreateAPIView):
    lookup_field = "id"
    serializer_class = RouterGatewaySerializer
    queryset = Router.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data= serializer.data
        gateway = serializer.data.get('gateway', None)
        listAddress = IPaddress.objects.filter(
            Q(gatewayId=gateway["id"]
              )).values_list("address",flat=True)
        gateway["ip_addressess"] = listAddress
        data["gateway"]=gateway
        return Response(data)

class RouterSearchView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Router.objects.all()
    serializer_class = RouterGatewaySerializer

    def get_queryset(self):
        routerId = self.kwargs[self.lookup_field]
        search_query = Router.objects.annotate(
            search_router=Value(routerId,output_field=CharField())
        ).filter(
            Q(search_router__istartswith=F("prefix"))
        ).last()
        return search_query

    def get_object(self):
        queryset = self.get_queryset()
        return queryset
