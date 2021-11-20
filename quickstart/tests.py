from django.test import TestCase
from .models import Order, Payment, Product
from django.utils import timezone

# Create your tests here.
class PaymentModelTests(TestCase):
    
    def test_payment_is_wrong(self):
        """
        Payment value if different of product value times order quantity        
        """
        now = timezone.now()
        product = Product.objects.create(name='My new product 1', price=10.0)
        order = Order.objects.create(product=product, quantity=1, date_time=now)
        wrong_payment = Payment.objects.create(order=order, paid_value=1)
        self.assertIs(wrong_payment.payment_is_ok == False, True)

    def test_payment_is_ok(self):
        """
        Payment value is equal to product value times order quantity        
        """
        now = timezone.now()
        product = Product.objects.create(name='My new product 2', price=15.0)
        order = Order.objects.create(product=product, quantity=1, date_time=now)
        right_payment = Payment.objects.create(order=order, paid_value=product.price * order.quantity)
        self.assertIs(right_payment.payment_is_ok, True)