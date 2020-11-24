from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/Qr_code',blank=True)

    def __str__(self):
        return self.name
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        qrcode_imges= qrcode.make(self.name)
        canvas = Image.new('RGB',(290,290),'white')
        draw= ImageDraw.Draw(canvas)
        canvas.paste(qrcode_imges)
        fname = F'qr_code_{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.image.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(force_insert=False, force_update=False, using=None,
             update_fields=None)
