from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("product", views.ProductView, name="product"),
    path("product-detail/<int:id>", views.ProductDetailView, name="detail"),
    
    path("high-inverters/product-detail/<int:id>", views.ProductDetailViewHighInvertersView, name="high_inverters_detail"),
    path("low-inverters/product-detail/<int:id>", views.ProductDetailViewLowInvertersView, name="low_inverters_detail"),
    path("high-batteries/product-detail/<int:id>", views.ProductDetailViewHighBatteriesView, name="high_batteries_detail"),
    path("low-batteries/product-detail/<int:id>", views.ProductDetailViewLowBatteriesView, name="low_batteries_detail"),
    
    path("terms-and-conditions", views.TermsAndConditions, name="terms-and-conditions"),
    path("cart/products/<str:cart_id>", views.CartView, name="cart"),
    path("checkout", views.CheckoutView, name="checkout"),
    path("checkout/<int:checkout_id>", views.CheckoutDetail, name="checkout_detail"),
    path("contact", views.Contact, name="contact"),

    
    path("grid-tie-inverters/product-detail/<int:id>", views.ProductDetailViewGridTieInvertersView, name="grid_tie_inverters_detail"),
    
    path("accessories/product-detail/<int:id>", views.ProductDetailViewAccessoriesView, name="accessories_detail"),
    path("ev-chargers/product-detail/<int:id>", views.ProductDetailViewChargersView, name="ev_chargers_detail"),

    path("grid-tie-inverters", views.GridTieInvertersView, name="grid_tie_inverters"),
    
    path("accessories", views.AccessoriesView, name="accessories"),
    path("ev-chargers", views.ChargersView, name="ev_chargers"),
    
    
    path("low-voltage-inverters", views.LowInvertersView, name="low_inverters"),
    path("high-voltage-inverters", views.HighInvertersView, name="high_inverters"),
    
    path("low-voltage-batteries", views.LowBatteriesView, name="low_batteries"),
    path("high-voltage-batteries", views.HighBatteriesView, name="high_batteries"),

    path("add-to-cart/<int:product_id>/<str:model>", views.AddToCart, name="add_to_cart"),
    path("remove-from-cart/<int:product_id>/", views.RemoveFromCart, name="remove_from_cart"),


    path("sign-in", views.SignInView, name="sign_in"),
    path("about/", views.About, name="about"),
    path("projects/", views.Projects, name="projects"),
    path("sign-up", views.SignUpView, name="sign_up"),
]