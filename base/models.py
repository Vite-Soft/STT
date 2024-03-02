from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField('Til', unique=True, max_length=3)
    class Meta:
        ordering = ["language"]
        verbose_name_plural = "Tillar"
    
    def __str__(self):
        return f"{self.language}"


class Type(models.Model):
    type = models.CharField('Til', unique=True, max_length=4)
    class Meta:
        ordering = ["type"]
        verbose_name_plural = "Turi"
    
    def __str__(self):
        return f"{self.type}"
    

class File(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True) 
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True) 
    file = models.FileField('Fayl', upload_to="")
    class Meta:
        ordering = ["file"]
        verbose_name_plural = "Fayllar"

    def __str__(self):
        return f"{self.file}"