
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url="/accounts/login/")),
    path('chat/', include("r_chat.urls")),
    path('chat/', RedirectView.as_view(url="/chat/home/")),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
    path("__reload__/", include("django_browser_reload.urls")),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
