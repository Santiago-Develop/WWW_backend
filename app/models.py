from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, phone=None, username=None, documentType=None, documentNumber=None, urlImg=None, role=None, country=None, department=None, city=None, is_staff=None, is_activate=None, is_superuser=None, last_login=None, date_joined=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.username = username
        user.phone = phone
        user.documentType = documentType
        user.documentNumber = documentNumber
        user.urlImg = urlImg
        user.role = role
        user.country = Country.objects.get(id=country)
        user.department = Department.objects.get(id=department)
        user.city = City.objects.get(id=city)
        user.is_staff = is_staff
        user.is_activate = is_activate
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)

    class DocumentTypes(models.TextChoices):
        NIT = "NIT", _("NIT")
        CC = "CC", _("CC")

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", _("Administrator")
        CUSTOMER = "CUSTOMER", _("Customer")
        MESSENGER = "MESSENGER", _("Messenger")

    documentType = models.CharField(
        choices=DocumentTypes.choices,
        default=DocumentTypes.CC,
        max_length=1000
    )
    documentNumber = models.CharField(
        max_length=100, blank=False, null=False, unique=True)
    phone = models.CharField(blank=False, null=False,
                             unique=True, max_length=100)
    urlImg = models.CharField(blank=False, null=False, max_length=2147483647)
    role = models.CharField(
        choices=Roles.choices,
        max_length=1000
    )
    password = models.CharField(
        default="", blank=False, null=False, max_length=1000)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    def __str__(self):
        return self.username


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(blank=False, null=False,
                             unique=False, max_length=100)
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE,
                                 related_name="id_customer_office", blank=True, null=True)

    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Engagement(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="customer_engagement", null=True)
    messenger = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="messenger_engagement", null=True)

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
    code = models.CharField(max_length=100, blank=True, null=True, unique=True)
    amount = models.IntegerField(blank=True, null=True)
    transport = models.CharField(
        choices=Transports.choices,
        default=Transports.MOTORCYCLE,
        max_length=1000
    )
    date_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    customer = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="customer_service", null=True)
    messenger = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="messenger_service", null=True)
    source_office = models.ForeignKey(
        Office, on_delete=models.CASCADE, related_name="source_office", null=True)
    destination_office = models.ForeignKey(
        Office, on_delete=models.CASCADE, related_name="destination_office", null=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["-date_time"]

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
    photo = models.CharField(max_length=2147483647, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    current_date_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["id"]

    def __str__(self):
        return self.id
