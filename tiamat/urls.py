from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtail.images.views.serve import ServeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

    #re_path(r'^graphql', csrf_exempt(GraphQLView.as_view())),
    #re_path(r'^graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True, pretty=True))),
    #re_path(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),

    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Serve static and media files from development server
    urlpatterns = staticfiles_urlpatterns() + urlpatterns
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

    # Add views for testing 404 and 500 templates
    urlpatterns = [
        path('test404/', TemplateView.as_view(template_name='404.html')),
        path('test500/', TemplateView.as_view(template_name='500.html')),
    ] + urlpatterns



