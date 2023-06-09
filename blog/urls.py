from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('api.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('auth/', include('rest_framework.urls')),
                  path('token/', views.obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
