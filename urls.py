from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
    # path('', views.product_list(), name='product_list'),
    # path('/<category_slug>', views.product_list(), name='product_list_by_category'),
    # path('/<product_id>', views.product_detail(), name='product_detail'),
    # url(r'test/', views.product_list,name='product_list'), #just test --> http://127.0.0.1:8000/admin/test/
    # url(r'test2/(?P<product_id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,name='product_detail'), 
    # #just test --> http://127.0.0.1:8000/admin/test2/1/slug1/
    ]