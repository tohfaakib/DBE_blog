from django.urls import path
from .views import PostListView, post_detail

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:day>/<int:month>/<int:year>/<slug:post>/', post_detail, name='post_detail')
]
