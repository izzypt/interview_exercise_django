from django.test import TestCase
from django.test import Client
from django.urls import reverse #reverse() is used to generate a URL pattern for a given view function or class (provide the name).
from .models import FindingsModel, ScanModel

class testFindingsList(TestCase):
    # setUp method is executed before each test method runs
    def setUp(self):
        self.url = reverse('findings_list')
        # Client() provides a way to simulate HTTP requests to your Django application. 
        # You can use it to test your views and ensure that they return the expected responses.
        self.client = Client()
        
    def test_findings_list_return_404(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
        
    def test_findings_list_return_200(self):
        # Create a new ScanModel instance
        scan = ScanModel.objects.create(value='example scan value')
        # Create a new FindingsModel instance and add the scan to its scans many-to-many field
        findings = FindingsModel.objects.create(
            target_id='example target id',
            definition_id='example definition id',
            url='http://example.com',
            path='/example/path',
            method='GET'
        )
        findings.scans.add(scan)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        
# Django creates a new database for testing and runs tests within that database. 
# Each test method in Django is atomic and isolated from the others, meaning that the database state is reset before each test method is executed. 
# This is done to ensure that tests run independently of each other and that there are no side effects or interference between tests. 
# Except setUp method which is executed before each test method and is used to set up any necessary data or objects that are required for the tests.
