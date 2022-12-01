from django.test import TestCase
from .forms import Itemform

# Create your tests here.


class TestItemform(TestCase):

    def test_item_name_required(self):
        form = Itemform({'name':  " "})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.error.keys())
        self.assertEqual(forms.error['name'][0], 'This field is required')

    def test_email_field_required(self):
        form = Itemform({'email', " "})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.error.keys())
        self.assertEqual(form.error, [email], 'This field is required')

    def test_date_field_required(self):
        form = Itemform({'date', " "})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.error.keys())
        self.assertEqual(form.error, [date], 'This field is required')

    def test_time_field_required(self):
        form = Itemform({'time', " "})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.error.keys())
        self.assertEqual(form.error, [time], 'This field is required')

    def test_seats_field_not_required(self):
        form = Itemform({'seats', " "})
        self.assertTrue(form.is_valid())
