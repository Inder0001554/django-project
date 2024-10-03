from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "inder Admin"
admin.site.site_title = "inder's Admin Portal"
admin.site.index_title = "Welcome to inder's brand"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls'))
]
