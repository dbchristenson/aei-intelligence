from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class IMAGE(models.Model):
    """
    This model is used to store embedded image files and their data.
    It uses a GenericForeignKey to allow any model instance to be referenced.
    This is useful for storing images that are related to other models
    in a generic way.
    """

    # These two fields are used to store the reference to any model instance
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    # This is the actual generic relation. It uses the above two fields.
    content_object = GenericForeignKey("content_type", "object_id")

    file = models.FileField(upload_to="image_files/")
    context = models.CharField(max_length=2000)  # context of the image

    def __str__(self):
        return self.file.name


class PDF(models.Model):
    """This model is used to store the pdf files and their data."""

    file = models.FileField(upload_to="pdf_files/")
    name = models.CharField(max_length=255)  # name of the file
    date = models.DateTimeField(auto_now_add=False)  # date written/published

    def __str__(self):
        return self.file.name


class PPTX(models.Model):
    """This model is used to store the pptx files and their data."""

    file = models.FileField(upload_to="pptx_files/")
    name = models.CharField(max_length=255)  # name of the file
    context = models.CharField(max_length=2000)  # context of the presentation

    def __str__(self):
        return self.file.name


class SLIDE(models.Model):
    """This model is used to store the slide images and their text."""

    pptx = models.ForeignKey(PPTX, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="slide_images/")
    text = models.TextField()  # text of the slide
    context = models.CharField(max_length=2000)  # context of the slide


class EXCEL(models.Model):
    """This model is used to store the excel files and their data."""

    def __str__(self):
        return self


class WORD(models.Model):
    """This model is used to store the word files and their text."""

    file = models.FileField(upload_to="word_files/")
    name = models.CharField(max_length=255)  # name of the file
    text = models.TextField()  # text of the document

    def __str__(self):
        return self
