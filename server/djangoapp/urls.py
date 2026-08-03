from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("dealer/<int:dealer_id>/", views.dealer_detail, name="dealer_detail"),
    path("dealer/<int:dealer_id>/review/", views.post_review, name="post_review"),
    path("dealers/state/<str:state>/", views.dealers_by_state_page, name="dealers_by_state_page"),
    path("djangoapp/login", views.api_login, name="api_login"),
    path("djangoapp/logout", views.api_logout, name="api_logout"),
    path("djangoapp/get_dealers", views.get_dealers, name="get_dealers"),
    path("djangoapp/get_dealers/<str:state>", views.get_dealers_by_state, name="get_dealers_by_state"),
    path("djangoapp/get_dealer/<int:dealer_id>", views.get_dealer_by_id, name="get_dealer_by_id"),
    path("djangoapp/dealer/<int:dealer_id>/reviews", views.get_dealer_reviews, name="get_dealer_reviews"),
    path("djangoapp/get_cars", views.get_cars, name="get_cars"),
    path("djangoapp/analyze", views.analyze_review, name="analyze_review"),
]
