from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import ZadanieDomowe

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ZadanieDomowe.views.home', name='home'),
    url(r'^home', 'ZadanieDomowe.views.home', name='home'),
    url(r'^about', 'ZadanieDomowe.views.about', name='about'),
    url(r'^login_user', 'ZadanieDomowe.views.login_user', name='login_user'),
    url(r'^logout_user', 'ZadanieDomowe.views.logout_user', name='logout_user'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^menu/', include('menu.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
     url(r'^%s/(?P<path>.*)$'%ZadanieDomowe.settings.MEDIA_URL.strip('/'),
            'django.views.static.serve', {
                'document_root': ZadanieDomowe.settings.MEDIA_ROOT,
                }),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
