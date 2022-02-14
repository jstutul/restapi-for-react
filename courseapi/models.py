from django.db import models


def upload_category_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


def upload_course_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    details = models.TextField()
    image = models.ImageField(upload_to=upload_category_image, blank=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Category Name'


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    details = models.TextField()
    price = models.FloatField(default=100.00)
    image = models.ImageField(upload_to=upload_course_image, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Course Name'
