from django.db import models
import uuid
from core.helper import (
    PathAndRename, 
)


class Borang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    signature = models.FileField(null=True,blank=True, max_length=500, upload_to=PathAndRename('/borang'))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
   
 
