from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Disease

def get_diseases(request):
    diseases = Disease.objects.all().values()
    return JsonResponse(list(diseases), safe=False)

@csrf_exempt
def upload_json(request):
    if request.method == "POST":
        file = request.FILES['file']
        data = json.load(file)
        for item in data:
            Disease.objects.create(
                name=item['name'],
                description=item['description'],
                category=item['category'],
                symptoms=item['symptoms'],
                causes=item['causes'],
                precautions=item['precautions'],
                medicines=item['medicines']
            )
        return JsonResponse({"message": "Data uploaded successfully!"})

def get_disease_detail(request, disease_id):
    try:
        disease = Disease.objects.filter(id=disease_id).values().first()
        return JsonResponse(disease, safe=False)
    except Disease.DoesNotExist:
        return JsonResponse({"error": "Disease not found"}, status=404)
