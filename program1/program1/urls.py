from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main2/', include('main2.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
