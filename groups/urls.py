from django.conf.urls import url
from . import views

app_name = 'groups'
urlpatterns = [
    # /profile/discipline-name/groups/
    url(
        r'^profile/(?P<slug>[\w_-]+)/groups/$',
        views.ListGroupView.as_view(),
        name='list'
    ),
    # /profile/discipline-name/groups/add/
    url(
        r'^profile/(?P<slug>[\w_-]+)/groups/add/$',
        views.CreateGroupView.as_view(),
        name='create'
    ),
    # /profile/discipline-name/groups/1/edit/
    url(
        r'^profile/(?P<slug>[\w_-]+)/groups/(?P<pk>[0-9]+)/edit/$',
        views.UpdateGroupView.as_view(),
        name='update'
    ),
    # /profile/discipline-name/
    url(
        r'^profile/(?P<slug>[\w_-]+)/groups/(?P<pk>[0-9]+)/delete/$',
        views.DeleteGroupView.as_view(),
        name='delete'
    ),
]
