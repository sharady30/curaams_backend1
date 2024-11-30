from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    symptoms = models.TextField()
    causes = models.TextField()
    precautions = models.TextField()
    medicines = models.TextField()
