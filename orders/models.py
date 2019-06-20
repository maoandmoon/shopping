from django.db import models
from catalog.models import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    created = models.DateTimeField(_('Created date'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated date'), auto_now=True)
    completed = models.BooleanField(_('Order has been completed'), default=False)
    # customer = models.ForeignKey(CustomerProfile, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order: #{self.id}, ordered by: {self.ordered_by}, ' \
            f'status: {"Order has been completed" if self.completed else "in progress"}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'item: {self.product.name}, quantity: {self.quantity}, cost: {self.get_cost()}'

    def get_cost(self):
        return self.price * self.quantity
