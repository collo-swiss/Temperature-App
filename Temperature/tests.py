from django.test import TestCase
from .models import TempData

class TempTestCase(TestCase):
    def setUp(self):
        TempData.objects.create(temp="15.5", date_time="2017-04-03 08:12 [:52[.842000]][TZ]")
        TempData.objects.create(temp="24.6", date_time="2017-05-03 06:05 [:52[.842000]][TZ]")
        
    def test_Days_Temp(self):
        monday = TempData.objects.get(date_time="2017-04-03 08:12 [:52[.842000]][TZ]")
        wednesday = TempData.objects.get(date_time="2017-05-03 06:05 [:52[.842000]][TZ]")
        self.assertEqual(monday.temp, 'The temperature on monday was: "15.5"')
        self.assertEqual(wednesday.temp,'The temperature on wednesday was: "24.6"')