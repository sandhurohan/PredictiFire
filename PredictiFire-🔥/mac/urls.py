from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),

                  path('signup', views.handleSignUp, name="handleSignUp"),
                  path('login', views.handeLogin, name="handleLogin"),
                  path('logout', views.handelLogout, name="handleLogout"),
    path('', views.index),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
