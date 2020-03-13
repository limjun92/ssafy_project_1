from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token 


app_name="nuneddinemap"

urlpatterns = [
    # path('', views.index),
    path('integrate/', views.integrate, name="integrate"),
    path('search/', views.search),
    path('search/hello', views.hello),
    path('new/',views.new, name="new"),
    path('registdetail/<int:id>/',views.registdetail),
    path('login/', obtain_jwt_token),
    path('signup/', views.signup),

    path('userInfo/<int:id>/',views.userInfo),
    path('mypage/<int:id>/', views.mypage),

    path('place/', views.place),
    path('place/<int:id>/', views.place_detail),
    path('place/<int:id>/comment/', views.comment_get),
    path('comment/', views.comment_post),
    path('place/<int:place_id>/comment/<int:comment_id>/', views.comment_detail),
    path('userreview/', views.userreview_post),
    path('place/<int:id>/keyword/', views.place_keyword),
    path('place/userreview_all/',views.place_userreview_all),
    path('placeImgs/', views.place_detail_imgs),

    # path('placelist/', views.placelist),
    # path('<int:id>/placedetail/', views.placedetail),

    # path('test/', views.test),
    # path('testboard/<int:id>/', views.testboard),

    path('like/', views.like),
    path('createdb/', views.createdb),
]

