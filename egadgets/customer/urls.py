from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("home",HomeView.as_view(),name="chome"),
    path("prod/<str:cat>",ProductView.as_view(),name="prod"),
    path("proddet/<int:pid>",ProductDetailView.as_view(),name="det"),
    path("addcart/<int:pid>",addtoCart,name="acart"),
    path("cartlist",CartListView.as_view(),name="clist"),
    path("delcart/<int:did>",CartRemoveView,name="dcart"),
    path("checkout/<int:cid>",CheckoutView.as_view(),name="cout"),
    path("orderlist",OrderListView.as_view(),name="olist"),
    path("cancelorder/<int:oid>",cancelOrder,name="corder"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)