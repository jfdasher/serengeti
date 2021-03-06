"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from django.views.static import serve
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

@staff_member_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    print ("%s %s" % (path, document_root,));
    return serve(request, path, document_root, show_indexes)



urlpatterns = [
    path('client/', include('client.urls')),
    path('admin/', admin.site.urls),
    path(r'^tinymce/', include('tinymce.urls')),
    path(r'^grappelli/', include('grappelli.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
