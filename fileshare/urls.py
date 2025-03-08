from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home.views import HandleFileUpload  ,home , download
urlpatterns = [
    path('handle/', HandleFileUpload.as_view(), name='handle_upload'),  
    path('download/<uid>', download, name='download'),  
    path('admin/', admin.site.urls),
    path('',home , name ='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)