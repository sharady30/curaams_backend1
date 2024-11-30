import json
from django.core.management.base import BaseCommand
from diseases.models import Disease

class Command(BaseCommand):
    help = "Import diseases from a JSON file"

    def handle(self, *args, **kwargs):
        try:
            with open('extended_diseases_data.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    Disease.objects.create(
                        name=item['name'],
                        description=item.get('description', ''),
                        category=item.get('category', ''),
                        symptoms=item.get('symptoms', ''),
                        causes=item.get('causes', ''),
                        precautions=item.get('precautions',''),
                        medicines=item.get('medicines','')
                    )
                self.stdout.write(self.style.SUCCESS('Successfully imported diseases!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing diseases: {str(e)}'))
