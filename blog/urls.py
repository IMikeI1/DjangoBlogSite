from django.urls import path
from blog.views import index, about, add_post, read_post, delete_post, update_post


app_name = 'blog'
urlpatterns = [
    # path('about/contacts', about, name='about'),
    path('about/', about, name='about'), #Более специфические маршруты выше, чем более общие
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/<slug:slug>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
]