from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    
    # Admin
    path('admin/', admin.site.urls),
    
    # 2.1 Install django rest framework 
    path('api-auth/', include('rest_framework.urls')),
    
    # 2.2
    path('store/', include('store.urls')),
    
]
