from django.db import models


class Cat(models.Model):
    CAT_BREED = [
        ('pe', 'Persa'),
        ('si', 'Siamês'),
        ('ab', 'Abissínio'),
        ('mc', 'Maine Coon'),
        ('sf', 'Esfinge'),
        ('rg', 'Ragdoll'),
        ('bn', 'Bengal'),
        ('br', 'Birmanês'),
        ('dr', 'Devon Rex'),
    ]

    CAT_COLOR = [
        ('pr', 'Preto'),
        ('br', 'Branco'),
        ('ci', 'Cinza'),
        ('ma', 'Malhado'),
        ('ta', 'Tabby'),
        ('ca', 'Carey'),
    ]

    name = models.CharField(max_length=30)
    description = models.TextField()
    breed = models.CharField(max_length=2, choices=CAT_BREED)
    color = models.CharField(max_length=2, choices=CAT_COLOR)

    def get_cat_breed(self):
        return self.CAT_BREED

    def get_cat_color(self):
        return self.CAT_COLOR

    def __str__(self) -> str:
        return str(self.name)
