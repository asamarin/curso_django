from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from blog.views import PostList, PostDetail, PostCreate, PostEdit, PostDelete
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amazing_blog.views.home', name='home'),
    # url(r'^amazing_blog/', include('amazing_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'post/create$', login_required(PostCreate.as_view()), name='post_create'),
    url(r'post/(?P<pk>\d+)/edit$', login_required(PostEdit.as_view()), name='post_edit'),
    url(r'post/(?P<pk>\d+)/delete$', login_required(PostDelete.as_view()), name='post_delete'),
    url(r'post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^$', PostList.as_view(), name='post_list'),
)
