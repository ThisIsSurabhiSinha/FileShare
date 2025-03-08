from django.db import models
import uuid
import os

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)  

def get_upload_path(instance, filename):
   
    if not instance.folder_id:
        instance.folder.save()  
    return os.path.join(str(instance.folder.uid), filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="files")  
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)  
