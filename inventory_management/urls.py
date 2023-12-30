from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = "inventory_management"

urlpatterns = [
    path("",homepage,name="homepage"),
    path("addProduct",addProduct,name="addProduct"),
    path("getProducts",getAllProducts,name="getAllProducts")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,                       # This is important for media like photos and videos
                          document_root=settings.MEDIA_ROOT)
