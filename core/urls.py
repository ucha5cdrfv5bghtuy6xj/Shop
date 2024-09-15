from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import signin, signout, signup, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path("signin/", signin, name='signin'),
    path("signout/", signout, name='signout'),
    path("profile/", profile, name='profile'),
    path("", include("shop.urls")),
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)