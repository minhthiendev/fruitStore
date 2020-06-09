

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'T Organic fruit'
admin.site.site_title = 'Organic fruit admin'
admin.site.site_url = 'http://localhost:8000/'
admin.site.index_title = 'Organic fruit administration'
admin.empty_value_display = '**Empty**'


urlpatterns = [
    path('', include('pages.urls')),
    path('', include('Fruits.urls')),
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
