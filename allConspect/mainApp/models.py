from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class FormulaConspect(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Formula(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=1000, verbose_name="formulaText")
    isLatex = models.BooleanField(default=False)
    parent = models.ForeignKey(FormulaConspect, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name