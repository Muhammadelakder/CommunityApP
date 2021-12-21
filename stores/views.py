from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .services import get_nearby_stores_within
from .models import Store
from .serializers import NearbyStoreSerializer

# Create your views here.

# انشاء صنف للعثور علي المتجار القريبه من المستخدم
class StoreView(viewsets.ModelViewSet):

    # استخراج المتاجر المخزنه في قاعدة البيانات
    queryset = Store.objects.all()

    serializer_class = NearbyStoreSerializer

    def list(self, request):
        # تحديد احاداثيات مكان المستخدم باستعمال 
        latitude= self.request.query_params.get('lat')
        longitude = self.request.query_params.get('lng')
        
        radius = 30 # كيلومتر
        number_of_stores_to_return = 100

        stores = get_nearby_stores_within(
            latitude=float(latitude),
            longitude=float(longitude),
            km=radius,
            limit=number_of_stores_to_return
        )

        stores_data = NearbyStoreSerializer(stores, many=True)
        return Response(stores_data.data)
