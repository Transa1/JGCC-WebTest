from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, products, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('product/<str:hashed_id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
