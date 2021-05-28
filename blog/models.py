from django.db import models

# Create your models here.


class Lesson(models.Model):

    CATEGORIES = [
        (1, 'podstawówka klasy 1-4'),
        (2, 'podstawówka klasy 5-8'),
        (3, 'liceum poziom podstawowy'),
        (4, 'liceum poziom rozszerzony')
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, blank=False, unique=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=False)
    categories = models.PositiveSmallIntegerField(blank=False, choices=CATEGORIES, default=CATEGORIES[0][0])

    def __str__(self):
        return "{}({}) - {}".format(self.title, self.date, self.categories)
