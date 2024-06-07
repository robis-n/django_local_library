
from django.contrib import admin
from django.urls import path

# Use include() to add from the catalog application
from django.urls import include

# Add URL maps to redirect teh base URL to our application
from django.views.generic import RedirectView

# Use static() to add URL mapping to serve static files during development ()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')), # Use include() to add from the catalog application
    path('', RedirectView.as_view(url='catalog/')), # Add URL maps to redirect teh base URL to our application
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Use static() to add URL mapping to serve static files during development ()