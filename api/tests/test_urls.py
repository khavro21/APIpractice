from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        path = reverse('GetOnePet', kwargs={'pk': 1})
        assert resolve(path).view_name == 'GetOnePet'

    def test_petlist_url(self):
        path = reverse('pet-list')
        assert resolve(path).view_name == 'pet-list'



