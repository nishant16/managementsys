#comment
from django.conf.urls import url
from rest_framework import routers
from hotels.api.viewsets import HotelView

router = routers.DefaultRouter()

router.register(r'hotels', HotelView, base_name="hotel")
# router.register(r'customer', CustomerView, base_name="customer")
# router.register(r'staff', StaffView, base_name="staff")
#

urlpatterns = router.urls
