from django.test import TestCase
from .forms import Itemform

# Create your tests here.


class TestItemform(TestCase):

    def test_item_name_required(self):
        form = Itemform({'name':  " "})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.error.keys())
        self.assertEqual(forms.error['name'][0], 'This field is required')
        