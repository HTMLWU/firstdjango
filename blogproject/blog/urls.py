from django.conf.urls import url
from . import views


app_name = 'blog'  # 视图函数命名空间
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^myapi$', views.my_api, name='myapi'),
    url(r'^mypost$', views.PostAPIView.as_view(), name='mypost'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),

    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.archivesView.as_view(), name='archives'),

    url(r'^category/(?P<pk>[0-9]+)/$',
        views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$',
        views.TagView.as_view(), name='tag'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
# def brinySearch(arr,target):
#     l=0
#     r=arr.length-1
#     while l<=r:
#         mid = (l+r)/2
#         if arr[mid] == target:
#             return mid
#         if arr[mid] < target:
#             l = mid+1
#         else:
#             r = mid-1
#     return -1
