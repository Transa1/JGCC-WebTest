from django.db import models
from django.contrib.auth.models import User

# Modelo de Producto
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='products/', null=True, blank=True)  # Imagen principal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Modelo para imágenes adicionales de los productos
class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products/extra/')

    def __str__(self):
        return f"Imagen de {self.product.name}"

# Modelo de Carrito de Compras
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"

# Modelo de Items dentro del Carrito
class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

# Modelo de Órdenes (Pedidos)
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Orden {self.id} - {self.user.username}"

# Modelo de Items dentro de una Orden
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio al momento de la compra

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} en orden {self.order.id}"
