from django.urls import path
from .views import home_view,\
    post_detail_view, \
    about_detail_view,\
    post_contact_view,\
    post_create_view, \
    post_view, \
    register_view, \
    login_view, \
    logout_view

urlpatterns = [
    path("", home_view, name='home_page'),
    path("post-detail/<int:post_id>/",post_detail_view, name='post_detail_page'),
    path("about/", about_detail_view, name='about_page'),
    path("contact/", post_contact_view, name='contact_page'),
    path("post-create/", post_create_view, name= 'post_create_page'),
    path("post/", post_view, name='post_page'),
    path("register/", register_view, name= 'register_page'),
    path("login/", login_view, name= 'login_page'),
    path("logout/", logout_view, name='logout_page')
]