from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/sales/', include("apps.sales.urls") )
]


admin.site.site_header = "Savanah Admin"
admin.site.site_title = "Savanah Admin Portal"
admin.site.index_title = "Welcome to the Savanah Portal"