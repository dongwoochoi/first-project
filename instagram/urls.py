
from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter, MonthConverter, DayConverter




register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'year')
register_converter(DayConverter, 'day')

app_name = 'instagram' #url reverse에서 namespace역할

urlpatterns = [
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('new/', views.post_new, name='post_new'),
    
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    
    #re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    # path('archives/<int:year>/', views.archives_year),
    # path('archives/<year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),

    #re_path(r'(?P<pk>\d+)/$', views.post_detail),
]