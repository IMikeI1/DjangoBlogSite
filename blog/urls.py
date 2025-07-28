from django.urls import path
from blog.views import (index, about, add_post, read_post,
                        delete_post, update_post, user_posts,
                        user_info, search_post, filter_post, favorites_list, add_to_favorites, 
                        remove_from_favorites, page_not_found, forbidden, server_error,
                        health_dog, eat_dog, leash, cant_shout, feedback)
from .views import trigger_404, trigger_403, trigger_500


app_name = 'blog'
urlpatterns = [
    path('search/', search_post, name='search_post'),
    path('filter/', filter_post, name='filter_post'),
    # path('about/contacts', about, name='about'),
    path('about/', about, name='about'), #Более специфические маршруты выше, чем более общие
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/user/info/<int:user_id>/', user_info, name='user_info'),
    path('post/user/<int:user_id>/', user_posts, name='user_posts'),
    path('post/<slug:slug>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/add_favorite/', add_to_favorites, name='add_to_favorites'),
    path('post/<slug:slug>/remove_favorite/', remove_from_favorites, name='remove_from_favorites'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('favorites/', favorites_list, name='favorites_list'),
    #path('test-404/', trigger_404, name='test_404'),
    #path('test-403/', trigger_403, name='test_403'),
    #path('test-500/', trigger_500, name='test_500'),
    path('health_dog/', health_dog, name='health_dog'),
    path('cant_shout/', cant_shout, name='cant_shout'),
    path('eat_dog/', eat_dog, name='eat_dog'),
    path('feedback/', feedback, name='feedback'),
    path('leash/', leash, name='leash'),
    path('', index, name='index'),

    path('404', page_not_found, name='404'),
    path('403', forbidden, name='403'),
    path('500', server_error, name='500'),

]