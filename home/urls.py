from django.conf.urls import url

from home import views

urlpatterns = [
    url(
        r'^$',
        views.home,
        name='home'
    ),
    url(
        r'^api/v1/home/(?P<pk>[0-9]+)$',
        views.get_delete_update_home,
        name='get_delete_update_home'
    ),
    url(
        r'^api/v1/homes/$',
        views.get_post_home,
        name='get_post_home'
    ),
    url(
        r'^api/v1/thing/(?P<pk>[0-9]+)$',
        views.get_delete_update_thing,
        name='get_delete_update_thing'
    ),
    url(
        r'^api/v1/things/(?P<pk>[0-9]+)$',
        views.get_post_things,
        name='get_post_things'
    ),
    url(
        r'^api/v1/types/$',
        views.get_post_type,
        name='get_post_type'
    ),

]
