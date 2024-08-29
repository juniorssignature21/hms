from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('signin/', views.signin, name='signin' ),
    path('signup/', views.sign_up, name='signup' ),
    path('signout/', views.signout, name='signout' )
]
