from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("showOrderStatus/", views.showOrderStatus, name="ShowOrderStatus"),
    path("orderplaced/<int:ordid>", views.orderplaced, name="OrderPlaced"),
    path("signup/", views.HandleSignUp, name="SignUp"),
    path("login/", views.HandleLogin, name="Login"),
    path("logout/", views.HandleLogout, name="Logout"),
    path("notFound/", views.notFound, name="NotFound"),
]

