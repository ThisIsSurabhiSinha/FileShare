from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home.views import HandleFileUpload  ,home , download
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
urlpatterns = [
    path('handle/', HandleFileUpload.as_view(), name='handle_upload'),  
    path('download/<uid>', download, name='download'),  
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('',home , name ='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
