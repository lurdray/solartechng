from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




    

class Category(models.Model):
    title = models.CharField(max_length=100)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
    

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(default="")
    rating = models.IntegerField(default=0)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)




class Accessories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)



class Chargers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class GridTieInverter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class HighVoltageInverter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class LowVoltageInverter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)



class HighVoltageBattery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


class LowVoltageBattery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
        

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, default="")
    
    price = models.CharField(max_length=100)

    image1 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image2 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image3 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image4 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    image5 = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    data_sheet = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    reviews = models.ManyToManyField(Review, through="ProductReviewConnector")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)




class Cart(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through="CartProductConnector")
    
    LowVoltageBattery = models.ManyToManyField(LowVoltageBattery, through="CartLowVoltageBatteryConnector")
    HighVoltageBattery = models.ManyToManyField(HighVoltageBattery, through="CartHighVoltageBatteryConnector")
    LowVoltageInverter = models.ManyToManyField(LowVoltageInverter, through="CartLowVoltageInverterConnector")
    HighVoltageInverter = models.ManyToManyField(HighVoltageInverter, through="CartHighVoltageInverterConnector")
    GridTieInverter = models.ManyToManyField(GridTieInverter, through="CartGridTieInverterConnector")
    Chargers = models.ManyToManyField(Chargers, through="CartChargersConnector")
    Accessories = models.ManyToManyField(Accessories, through="CartAccessoriesConnector")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

class Order(models.Model):
    cart_id = models.CharField(max_length=100)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.cart_id)
    
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    auth_code = models.CharField(max_length=20, default="null")

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    orders = models.ManyToManyField(Order, through="AppUserOrderConnector")

    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    address = models.TextField(default="")
    delivery_state = models.CharField(max_length=50, default="nowhere")

    streetAddress = models.CharField(max_length=100, default="")
    suite = models.CharField(max_length=100, default="")
    cityAddress = models.CharField(max_length=100, default="")
    order_note = models.CharField(max_length=100, default="")


    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.username)
    
    def total_price(self):
        if self.cart:
            return sum(int(product.price) for product in self.cart.products.all())
        return 0

class Checkout(models.Model):
    title = models.CharField(max_length=100)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
    
class AppUserOrderConnector(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)





class CartLowVoltageBatteryConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	LowVoltageBattery = models.ForeignKey(LowVoltageBattery, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class CartHighVoltageBatteryConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	HighVoltageBattery = models.ForeignKey(HighVoltageBattery, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class CartLowVoltageInverterConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	LowVoltageInverter = models.ForeignKey(LowVoltageInverter, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class CartHighVoltageInverterConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	HighVoltageInverter = models.ForeignKey(HighVoltageInverter, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)



class CartGridTieInverterConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	GridTieInverter = models.ForeignKey(GridTieInverter, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class CartChargersConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	Chargers = models.ForeignKey(Chargers, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class CartAccessoriesConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	Accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)













class CartProductConnector(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ProductImageConnector(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ProductReviewConnector(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

#class AppUserBusinessConnector(models.Model):
#	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
#	business = models.ForeignKey(Business, on_delete=models.CASCADE)
#	pub_date = models.DateTimeField(default=timezone.now)
