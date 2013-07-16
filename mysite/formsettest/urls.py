from django.conf.urls import patterns, url

from formsettest import views

urlpatterns = patterns('',
                       url(r'^$', views.manage_articles,
                           name='manage_articles')
                       )
