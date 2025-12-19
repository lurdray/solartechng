from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from django.shortcuts import redirect
from django.urls import reverse

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt

from main.models import *

import requests
from main.models import AppUser
from django.shortcuts import redirect





def IndexView(request):
    #import time
    #time.sleep(120)

    
    if request.method == "POST":
        pass

    else:

        top_rated_products = Product.objects.all().order_by('pub_date')[:6]
        on_sale_products = Product.objects.all().order_by('pub_date')[:6]
        featured_products = Product.objects.all().order_by('pub_date')[:6]

        sliding_products = Product.objects.all().order_by('pub_date')[:8]

        trending_products1 = Product.objects.all().order_by('pub_date')[:3]
        trending_products2 = Product.objects.all().order_by('pub_date')[3:6]
        trending_products3 = Product.objects.all().order_by('pub_date')[6:9]

        best_seller_products1 = Product.objects.all().order_by('pub_date')[:3]
        best_seller_products2 = Product.objects.all().order_by('pub_date')[3:6]
        best_seller_products3 = Product.objects.all().order_by('pub_date')[6:9]
        best_seller_products4 = Product.objects.all().order_by('pub_date')[:3]

        top_categories_month = Product.objects.all().order_by('pub_date')[:4]
        recommended_products = Product.objects.all().order_by('pub_date')[:4]
        
        low_voltage_battery = LowVoltageBattery.objects.all().order_by('pub_date')[:4]
        high_voltage_battery = HighVoltageBattery.objects.all().order_by('pub_date')[:4]
        low_voltage_inverter = LowVoltageInverter.objects.all().order_by('pub_date')[:4]
        high_voltage_inverter = HighVoltageInverter.objects.all().order_by('pub_date')[:4]

        context = {
            "low_voltage_battery": low_voltage_battery,
            "high_voltage_battery": high_voltage_battery,
            "low_voltage_inverter": low_voltage_inverter,
            "high_voltage_inverter": high_voltage_inverter,
            
            "top_rated_products": top_rated_products,
            "on_sale_products": on_sale_products,
            "featured_products": featured_products,

            "trending_products1": trending_products1,
            "trending_products2": trending_products2,
            "trending_products3": trending_products3,

            "top_categories_month": top_categories_month,
            "recommended_products": recommended_products,
            "sliding_products": sliding_products,

            "best_seller_products1": best_seller_products1,
            "best_seller_products2": best_seller_products2,
            "best_seller_products3": best_seller_products3,
            "best_seller_products4": best_seller_products4,

        }


        return render(request, "main/index.html", context)
        
def ProductView(request):

    if request.method == "POST":
        pass

    else:
        products = Product.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/product.html", context)
    
def ProductDetailView(request, id):
    if request.method == "POST":
        pass

    else:
        product = Product.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "Product"}
        return render(request, "main/product-detail.html", context)
    
def TermsAndConditions(request):
    
    
    if request.method == "POST":
        pass

    else:
        context = {}
        return render(request, "main/product-detail2.html", context)
    
def CartView(request, cart_id):
    try:
        app_user = AppUser.objects.get(user__id=request.user.id)
    except:
        app_user = None
        
    if app_user:
        cart = app_user.cart
        
    else:
        if cart_id == "None":
            cart = Cart.objects.create(title="Cart for None user")
            cart.save()
        
        else:
            cart = Cart.objects.get(id=cart_id)
    
    if request.method == "POST":
        pass

    else:
        context = {"app_user": app_user, "cart": cart}
        return render(request, "main/cart.html", context)

def CheckoutView(request):
    try:
        app_user = AppUser.objects.get(user__id=request.user.id)
    except:
        messages.info(request, "Please login to your account")
        return redirect(reverse("main:index"))

    if request.method == "POST":
        
        
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        streetAddress = request.POST.get("streetAddress")
        suite = request.POST.get("suite")
        cityAddress = request.POST.get("cityAddress")
        order_note = request.POST.get("order_note")

        user = app_user.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        app_user.streetAddress = streetAddress
        app_user.suite = suite
        app_user.cityAddress = cityAddress
        app_user.order_note = order_note
        app_user.save()

        checkout = Checkout.objects.create(title="Checkout id", cart=app_user.cart, app_user=app_user)
        checkout.save()

        from urllib.parse import quote

        checkout_link = f"http://solartech-ng.com/checkout/{checkout.id}"
        message = f"Here is my checkout link {checkout_link}"
        encoded_message = quote(message)

        external_url = f"https://wa.me/2349020202010?text={encoded_message}"


        # Build the external URL with the checkout ID
        #external_url = f"https://wa.me/2349020202010?text=Here%20is%20my%20checkout%20link%20http%3A%2F%2F127.0.0.1%3A8000%2Fcheckout%2F{checkout.id}"
        
        return redirect(external_url)
    else:
        context = {"app_user": app_user}
        return render(request, "main/checkout.html", context)






def CheckoutDetail(request, checkout_id):

    checkout = Checkout.objects.get(id=checkout_id)
    if request.method == "POST":
        pass

    else:
        context = {"checkout": checkout, "app_user": checkout.app_user}
        return render(request, "main/checkout_detail.html", context)
    


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime


def send_mail(email, first_name, last_name, phone_number, zip_code, message):
    subject = "New Message from %s" % last_name
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    # Render the HTML template with context
    context = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'zip_code': zip_code,
        'message': message,
        
    }
    html_content = render_to_string('main/mail.html', context)

    # Create the email
    email_message = EmailMultiAlternatives(subject, "", from_email, recipient_list)
    email_message.attach_alternative(html_content, "text/html")  # Attach the HTML content

    # Send the email
    email_message.send(fail_silently=False)




def Contact(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        zip_code = request.POST.get("zip_code")
        message = request.POST.get("message")
        
        send_mail("odiagaraymondray@gmail.com", first_name, last_name, phone_number, zip_code, message)
        send_mail("info@solartechng.com", first_name, last_name, phone_number, zip_code, message)
        
        
        messages.info(request, "Your message has been sent, you will receive a response from us soon.")
        return redirect(reverse("main:index"))
        
        

    else:
        context = {}
        return render(request, "main/contact.html", context)
    



def SignInView(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("main:index"))

        else:
            messages.error(request, "Invalid email or password")
            return redirect(reverse("main:index"))




def SignUpView(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("email")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Both passwords must be the same")
            return redirect(reverse("main:sign_up"))
        
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Email address already used.")

            return redirect(reverse("main:sign_up"))
        
        except:
            pass
        
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
        user.save()

        app_user = AppUser.objects.create(user=user)
        app_user.save()

        login(request, user)

        messages.info(request, "Your account has been created.")
        return redirect(reverse("main:index"))
    
    else:
        context = {}
        return render(request, "main/sign_up.html", context)
    






def AddToCart(request, product_id, model=None):
    try:
        app_user = AppUser.objects.get(user__id=request.user.id)
    except:
        app_user = None
        pass
        #messages.info(request, "Please login to your account")
        #return redirect(reverse("main:index"))
    
    if app_user:
        if app_user.cart == None:
            cart = Cart.objects.create(title="Cart for %s" % app_user.user.username)
            cart.save()
    
            app_user.cart = cart
            app_user.save()
            
    else:
        cart = Cart.objects.create(title="Cart for None User")
        cart.save()

    if app_user:
        cart = app_user.cart
        
    
    if model:
        from django.apps import apps
        Product = apps.get_model('main', model)
    
        product = Product.objects.get(id=product_id)

    if product in cart.products.all():
        messages.error(request, "Added to cart")
        return redirect(reverse("main:cart", args=[cart.id]))

    else:
        if model == "LowVoltageBattery":
            cp = CartLowVoltageBatteryConnector(cart=cart, LowVoltageBattery=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
            
        elif model == "HighVoltageBattery":
            cp = CartHighVoltageBatteryConnector(cart=cart, HighVoltageBattery=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
        
        elif model == "LowVoltageInverter":
            cp = CartLowVoltageInverterConnector(cart=cart, LowVoltageInverter=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
            
        elif model == "HighVoltageInverter":
            cp = CartHighVoltageInverterConnector(cart=cart, HighVoltageInverter=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
        
        elif model == "GridTieInverter":
            cp = CartGridTieInverterConnector(cart=cart, GridTieInverter=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
            
        elif model == "Chargers":
            cp = CartChargersConnector(cart=cart, Chargers=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
            
        elif model == "Accessories":
            cp = CartAccessoriesConnector(cart=cart, Accessories=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))
            
        elif model == "Product":
            cp = CartProductConnector(cart=cart, product=product)
            cp.save()
    
            messages.error(request, "Added to cart")
            return redirect(reverse("main:cart", args=[cart.id]))

            
            
            




def RemoveFromCart(request, product_id):
    try:
        app_user = AppUser.objects.get(user__id=request.user.id)
    except:
        messages.info(request, "Please login to your account")
        return redirect(reverse("main:index"))

    cart = app_user.cart
    product = Product.objects.get(id=product_id)

    cart.products.remove(product)

    messages.error(request, "Removed from cart")
    return redirect(reverse("main:cart", args=[cart.id]))

def About(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        context = {}
        return render(request, "main/about.html", context)
        
def Projects(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        context = {}
        return render(request, "main/projects.html", context)
        
 
 

def GridTieInvertersView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = GridTieInverter.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/grid_tie_inverter.html", context)
        
      


def ChargersView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = Chargers.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/chargers.html", context)
        
  
  
def AccessoriesView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = Chargers.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/accessories.html", context)
       
       
         
def ProductDetailViewGridTieInvertersView(request, id):
    if request.method == "POST":
        pass

    else:
        product = GridTieInverter.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "GridTieInverter"}
        return render(request, "main/product-detail.html", context)
     
   
def ProductDetailViewChargersView(request, id):
    if request.method == "POST":
        pass

    else:
        product = Charger.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "Charger"}
        return render(request, "main/product-detail.html", context)
        
  
  
def ProductDetailViewAccessoriesView(request, id):
    if request.method == "POST":
        pass

    else:
        product = Accessories.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "Accessories"}
        return render(request, "main/product-detail.html", context)
        
        
              
def LowInvertersView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = LowVoltageInverter.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/low_inverters.html", context)
        
        

def HighInvertersView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = HighVoltageInverter.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/high_inverters.html", context)
        
        

        
def LowBatteriesView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = LowVoltageBattery.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/low_batteries.html", context)
        
        

def HighBatteriesView(request):
    
    
    
    if request.method == "POST":
        pass

    else:
        products = HighVoltageBattery.objects.all().order_by('pub_date')
        context = {"products": products}
        return render(request, "main/high_batteries.html", context)
        

def ProductDetailViewHighBatteriesView(request, id):
    if request.method == "POST":
        pass

    else:
        product = HighVoltageBattery.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "HighVoltageBattery"}
        return render(request, "main/product-detail.html", context)
   
   
def ProductDetailViewLowBatteriesView(request, id):
    if request.method == "POST":
        pass

    else:
        product = LowVoltageBattery.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "LowVoltageBattery"}
        return render(request, "main/product-detail.html", context)
     
     
   
def ProductDetailViewHighInvertersView(request, id):
    if request.method == "POST":
        pass

    else:
        product = HighVoltageInverter.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "HighVoltageInverter"}
        return render(request, "main/product-detail.html", context)
     
     
def ProductDetailViewLowInvertersView(request, id):
    if request.method == "POST":
        pass

    else:
        product = LowVoltageInverter.objects.get(id=id)
        product_images = [].append(product.image1)
        context = {"product": product, "product_images": product_images, "model": "LowVoltageInverter"}
        return render(request, "main/product-detail.html", context)
     