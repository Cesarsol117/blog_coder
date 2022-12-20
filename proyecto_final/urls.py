from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
# Desde aca empieza
from usuarios.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path

    # ------------------usuari0----------------------
    path('usuarios/', include("usuarios.urls")),
    # path('', inicio, name = "inicio"),
    

]

# Path of media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
