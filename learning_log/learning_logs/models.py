from django.db import models

# Create your models here.
class Topik(models.Model):
    """A topic the user is learning about"""
    #text adında bir charfield tanımlıyoruz. bu veri tabanında bir sütun oluşturacak. max karakteri 200
    text =models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


# topik (konular) altında belirli bir girdi girebilmek için Entry isimli model
class Entry(models.Model):
    """something specific learned about a topik"""
    topik =models.ForeignKey(Topik, on_delete=models.CASCADE)
    text =models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."












