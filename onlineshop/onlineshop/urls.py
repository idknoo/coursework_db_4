
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('product.urls', 'product')),
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('customer/', include('customer.urls', 'customer')),
    path('order/', include('order.urls', 'order'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
