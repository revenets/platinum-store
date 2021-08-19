from django.db import models
from django.urls import reverse

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)
    prod_country = models.CharField(max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to="brands/")

    def __str__(self):
        return self.name

    def url(self):
        return reverse("platinum:brand_detail", args=[self.id])

    class Meta:
        ordering = ["name"]


class Oil(models.Model):
    type = models.CharField(max_length=50)
    w_visco = models.IntegerField(default=0)
    s_visco = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    standard = models.ManyToManyField("Standard", related_name="oils")

    def __str__(self):
        return f"{self.brand} {self.w_visco}W-{self.s_visco}"

    def url(self):
        return reverse("platinum:oil_detail", args=[self.id])

    def get_visco(self):
        return f"{self.w_visco}W-{self.s_visco}"

    class Meta:
        ordering = ["brand"]


class Standard(models.Model):
    st_name = models.CharField(max_length=50)
    st_value = models.CharField(max_length=20)

    def __str__(self):
        return str(self.st_name) + " " + str(self.st_value)


class OilInstance(models.Model):
    oil = models.ForeignKey(Oil, on_delete=models.SET_NULL, null=True)
    mark = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    img = models.ImageField(null=True, blank=True, upload_to="oils/")

    def get_discount(self):
        return round(self.price * 0.95, 2)

    class Meta:
        ordering = ["oil"]

    def __str__(self):
        return f"{self.oil} {self.mark} {self.volume}L"


class Cart(models.Model):
    oil = models.ForeignKey(OilInstance, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=0, null=True)
    ORDER_STATUS = (("d", "Done"), ("w", "In work"),)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default="w")

    def get_sum(self):
        return self.amount * self.oil.price

    def get_sum_discount(self):
        return self.amount * self.oil.get_discount()


