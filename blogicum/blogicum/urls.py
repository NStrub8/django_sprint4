"""
blogicum URL Configuration

The `urlpatterns` list routes URLs to views.
For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

handler403 = 'pages.views.csrf_failure'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        include(('blog.urls', 'blog'), namespace='blog')
    ),
    path(
        'pages/',
        include(('pages.urls', 'pages'), namespace='pages')
    ),
    path(
        'auth/',
        include('django.contrib.auth.urls')
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
