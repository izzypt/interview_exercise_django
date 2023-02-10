from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from findings.models import FindingsModel, ScanModel
import requests
import json

class Command(BaseCommand):
    help = 'Fetch the API findings from the "List Findings" endpoint'
    
    def add_arguments(self, parser):
        parser.add_argument('--target_id', type=str, help='The target ID of the scan', default="Tt2f8EyPSTwq")
    
    def handle(self, *args, **kwargs):
        target_id = kwargs['target_id']
        results = self.make_api_call(target_id)
        self.save_to_db(results)
    
    def make_api_call(self, target_id : str) -> dict:
        url = f"https://api.probely.com/targets/{target_id}/findings/"
        headers  = {
            "Content-Type": "application/json",
            "Authorization": f"JWT {settings.PROBELY_API_KEY}"
        }
        #Make the request and get the response
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise CommandError(f"Was expecting 200 status code from API, instead got {response.status_code}")
        results = response.json().get("results")
        return results
    
    def save_to_db(self, results : dict) -> None:
        for finding in results:
            try:
                finding_id = finding.get("id")
                target_id = finding["target"].get("id")
                definition_id = finding["definition"].get("id")
                scans = finding.get("scans", [])
                url = finding.get("url")
                path = finding.get("path")
                method = finding.get("method")
            except Exception as e:
                raise CommandError(f"Something went wrong while extracting the data from the API response", e)
            try:
                # Create or retrieve the Scan instances
                scan_instances = [ScanModel.objects.get_or_create(value=scan_value)[0] for scan_value in scans]

                # Create or retrieve the Finding instance. get_or_create method returns a tuple of two values: 
                # 1) The instance that matches the query, 
                # 2) True/False. A boolean indicating whether the instance was created or not.
                finding, created = FindingsModel.objects.get_or_create(
                    id=finding_id,
                    target_id=target_id,
                    definition_id=definition_id,
                    url=url,
                    path=path,
                    method=method
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully created finding {finding.id}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Finding ID {finding.id} already in the database"))
                # Update the scans field for the finding for the many to many relationship
                finding.scans.add(*scan_instances)
            except Exception as e:
                raise CommandError(f"Something went wrong while creating or fetching the finding in the database:", e)

