from django.contrib import admin
from django.urls import include, path



admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
]
