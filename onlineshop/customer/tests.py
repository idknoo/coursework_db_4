from django.test import TestCase
from .models import Customer


class TestCustomerModel(TestCase):
    def set_up(self):
        self.customer = Customer.objects.create_user(
            username='akbar',
            first_name='akbar',
            last_name='akbari',
            phone='+9123856956',
            email='akkbar@gmail.com',
            password='svd432d5b1gq23w54ld',
        )

    def test_is_created(self):
        self.assertEqual(self.customer.last_name, 'akbari')
