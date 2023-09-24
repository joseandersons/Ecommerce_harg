from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('clientes.urls')),
    # path('dahsboard/', include('lojas.urls')),
    path('', include('clientes.urls', namespace='clientes')),
    path('dahsboard/', include('lojas.urls', namespace='lojas')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #TODO: REMOVER DEBUG TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)