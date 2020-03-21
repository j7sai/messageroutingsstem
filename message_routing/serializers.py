from rest_framework import serializers
from .models import *

class GatewaySerializer(serializers.ModelSerializer):
    ip_addresses = serializers.ListField(write_only=True)
    class Meta:
        model = Gateway
        fields = ("id","name","ip_addresses")
    def create(self, validated_data):
        ipaddresses = validated_data.pop("ip_addresses")
        gateway = Gateway.objects.create(**validated_data)
        for ip in ipaddresses:
            IPaddress.objects.create(gatewayId=gateway,address=ip)
        return gateway

class RouterGatewaySerializer(serializers.ModelSerializer):
    gateway = GatewaySerializer(read_only=True)
    gateway_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Router
        fields = ("id","gateway_id","gateway","prefix")