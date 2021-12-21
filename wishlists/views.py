from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Wishlist
from .serializer import WishlistSerializer
from .services import create_wishlist, get_wishlists, update_wishlist

# Create your views here.

# انشاء صنف لاستخراج الطلبيات من قاعدة البيانات و اظهارها في قالب الإتشتمل
class WishlistView(viewsets.ModelViewSet):  
    queryset = Wishlist.objects.all()  
    serializer_class = WishlistSerializer


    # تعريف وظيفه لتمرير البيانات اللازمه لإنشاء طلبيه 
    def create(self, request):  
        buyer = self.request.data.get('buyer')  
        items = self.request.data.get('items')  
        store = int(self.request.data.get('store'))

        wishlist = create_wishlist(buyer, items, store)  
        wishlist_data = WishlistSerializer(wishlist, many=False)

        return Response(wishlist_data.data)


    # استخراج الطلبيه
    def get_whishlist(self, request):
        latitude = self.request.query_params.get('lat')
        longitude = self.request.query_params.get('lng')
        options = {}

        for key in ('buyer', 'wishmaster'):
            value = self.request.query_params.get(key)

            if value:
                options[key] = value

        wishlist = get_wishlists(
            float(latitude),
            float(longitude),
            options
        )

        wishlist_data = WishlistSerializer(wishlist, many=True)

        return Response(wishlist_data.data)

    # update wishlists
    def partial_update(self, request, pk):  
        wishlist = update_wishlist(  
            pk=pk,  
            wishmaster=self.request.data.get('wishmaster'),  
            status=self.request.data.get('status')  
        )
        
        wishlist_data = WishlistSerializer(wishlist, many=False)  
        return Response(wishlist_data.data)
