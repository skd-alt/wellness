from django.urls import path

from . import views

urlpatterns = [
    path('general_info', views.general_info, name='general_info'),
    path('exercise', views.exercise, name='exercise'),
    path('self_check', views.self_check, name='self_check'),
    path('fasting', views.fasting, name='fasting'),
    path('sleep', views.sleep, name='sleep'),
    path('food', views.food, name='food'),
    path('skin_care', views.skin_care, name='skin_care'),
    path('back_pain', views.back_pain, name='back_pain'),
    path('back_pain2', views.back_pain2, name='back_pain2'),
    path('female_urinary', views.female_urinary, name='female_urinary'),
    path('female_urinary2', views.female_urinary2, name='female_urinary2'),
    # path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    # path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),

    # path('checkout/', views.checkout, name='checkout'),
]