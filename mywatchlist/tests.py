from django.test import TestCase, Client

class TestUrls(TestCase):
    client = Client()
    def test_html_url(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEquals(response.status_code, 200)