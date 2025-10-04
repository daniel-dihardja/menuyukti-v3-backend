from django.db import models


class Analytics(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    min_order_items = models.IntegerField()
    max_order_items = models.IntegerField()
    avg_order_items = models.FloatField()
    min_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_order_price = models.DecimalField(max_digits=10, decimal_places=2)
    avg_order_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    analytics = models.ForeignKey(
        Analytics, on_delete=models.CASCADE, related_name="orders"
    )
    order_time = models.DateTimeField()

    def __str__(self):
        return f"Order {self.id} at {self.order_time}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"


class Cogs(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="cogs")
    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, related_name="cogs"
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=5, decimal_places=2)  # percentage
    we = models.CharField(max_length=255)

    def __str__(self):
        return f"COGS for {self.order_item.name} (Cost: {self.cost}, Margin: {self.margin})"


class MatrixItem(models.Model):
    CATEGORY_CHOICES = [
        ("STAR", "Star"),
        ("PLOW_HORSE", "Plow Horse"),
        ("PUZZLE", "Puzzle"),
        ("DUDS", "Duds"),
    ]

    analytics = models.ForeignKey(
        Analytics, on_delete=models.CASCADE, related_name="matrix_items"
    )
    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, related_name="matrix_items"
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order_item.name} ({self.category}, Qty: {self.quantity})"
