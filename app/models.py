from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["name"]

    def __str__(self):
        return self.name

class User(models.Model):

    class DocumentTypes(models.TextChoices):
        NIT = "NIT", _("NIT")
        CC = "CC", _("CC")

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", _("Administrator")
        CUSTOMER = "CUSTOMER", _("Customer")
        MESSAGER = "MESSAGER", _("Messager")

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    documentType = models.CharField(
        choices=DocumentTypes.choices,
        default=DocumentTypes.CC,
    )
    documentNumber = models.CharField(max_length=100, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    urlImg = models.CharField(blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    role = models.CharField(
        choices=Roles.choices,
        default=Roles.CUSTOMER,
    )
    password = models.CharField(default="", blank=False, null=False)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    id_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_customer_office")

    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Engagement(models.Model):
    id = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_customer_engagement")
    id_messager = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Engagement"
        verbose_name_plural = "Engagements"
        ordering = ["id"]

class Service(models.Model):

    class Transports(models.TextChoices):
        CAR = "CAR", _("Car")
        MOTORCYCLE = "MOTORCYCLE", _("Motorcycle")
        TRUCK = "TRUCK", _("truck")

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)
    transport = models.CharField(
        choices=Transports.choices,
        default=Transports.MOTORCYCLE,
    )
    date_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    id_customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_customer_service")
    id_messager = models.ForeignKey(User, on_delete=models.CASCADE)
    id_source_office  = models.ForeignKey(Office, on_delete=models.CASCADE, related_name="id_source_office")
    id_source_destination = models.ForeignKey(Office, on_delete=models.CASCADE, related_name="id_source_destination")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["code"]

    def __str__(self):
        return self.code

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Update(models.Model):
    id = models.AutoField(primary_key=True)
    new_state = models.CharField(max_length=100, blank=False, null=False)
    photo = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    current_date_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["id"]

    def __str__(self):
        return self.id
