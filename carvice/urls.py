from django.contrib import admin
from django.urls import include, path

app_name = 'app'


urlpatterns = [
    path('',include('app.urls')),
    path('admin/', admin.site.urls),
]
