from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from . import Int_max
from django.db.models import manager
from django.db.models.base import Model

from tenants.models import Tenant


class Manager(models.Model):
    Abuja = 'Abuja'
    Abia = 'Abia'
    Adamawa = 'Adamawa'
    Akwa_Ibom = 'Akwa Ibom'
    Anambra = 'Anambra'
    Bauchi = 'Bauchi'
    Bayelsa = 'Bayelsa'
    Benue = 'Benue'
    Borno = 'Borno'
    Cross_River = 'Cross River'
    Delta = 'Delta'
    Ebonyi = 'Ebonyi'
    Edo = 'Edo'
    Ekiti = 'Ekiti'
    Enugu = 'Enugu'
    Gombe = 'Gombe'
    Imo = 'Imo'
    Jigawa = 'Jigawa'
    Kaduna = 'Kaduna'
    Kano = 'Kano'
    Katsina = 'Katsina'
    Kebbi = 'Kebbi'
    Kogi = 'Kogi'
    Kwara = 'Kwara'
    Lagos = 'Lagos'
    Nasarawa = 'Nasarawa'
    Niger = 'Niger'
    Ogun = 'Ogun'
    Ondo = 'Ondo'
    Osun = 'Osun'
    Oyo = 'Ibadan'
    Plateau = 'Plateau'
    Rivers = 'Rivers'
    Sokoto = 'Sokoto'
    Taraba = 'Taraba'
    Yobe = 'Yobe'
    Zamfara = 'Zamfara'

    state = [
        (Abuja, 'Abuja'),
        (Abia, 'Abia'),
        (Adamawa, 'Adamawa'),
        (Akwa_Ibom, 'Akwa Ibom'),
        (Anambra, 'Anambra'),
        (Bauchi, 'Bauchi'),
        (Bayelsa, 'Bayelsa'),
        (Benue,	'Benue'),
        (Borno, 'Borno'),
        (Cross_River, 'Cross River'),
        (Delta, 'Delta'),
        (Ebonyi, 'Ebonyi'),
        (Edo, 'Edo'),
        (Ekiti, 'Ekiti'),
        (Enugu, 'Enugu'),
        (Gombe, 'Gombe'),
        (Imo, 'Imo'),
        (Jigawa, 'Jigawa'),
        (Kaduna, 'Kaduna'),
        (Kano, 'Kano'),
        (Katsina, 'Katsina'),
        (Kebbi, 'Kebbi'),
        (Kogi, 'Kogi'),
        (Kwara, 'Kwara'),
        (Lagos, 'Lagos'),
        (Nasarawa, 'Nasarawa'),
        (Niger, 'Niger'),
        (Ogun, 'Ogun'),
        (Ondo, 'Ondo'),
        (Osun, 'Osun'),
        (Oyo, 'Ibadan'),
        (Plateau, 'Plateau'),
        (Rivers, 'Rivers'),
        (Sokoto, 'Sokoto'),
        (Taraba, 'Taraba'),
        (Yobe, 'Yobe'),
        (Zamfara, 'Zamfara')
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Building Manager")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = ""
    occupation = models.CharField(max_length=250)
    manager_sex = models.CharField(
        max_length=30, choices=state, default=Lagos, verbose_name='State')
    phone = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=300)
    manager_state = models.CharField(
        max_length=30, choices=state, default=Lagos, verbose_name='State')
    address = models.TextField(max_length=600)
    manager_website = models.CharField(max_length=250, null=True, blank=True)
    manager_rating = ArrayField(
        models.IntegerField(), size=50, null=True, blank=True)

    def __str__(self):
        return self.last_name


class Property(models.Model):
    Abuja = 'Abuja'
    Abia = 'Abia'
    Adamawa = 'Adamawa'
    Akwa_Ibom = 'Akwa Ibom'
    Anambra = 'Anambra'
    Bauchi = 'Bauchi'
    Bayelsa = 'Bayelsa'
    Benue = 'Benue'
    Borno = 'Borno'
    Cross_River = 'Cross River'
    Delta = 'Delta'
    Ebonyi = 'Ebonyi'
    Edo = 'Edo'
    Ekiti = 'Ekiti'
    Enugu = 'Enugu'
    Gombe = 'Gombe'
    Imo = 'Imo'
    Jigawa = 'Jigawa'
    Kaduna = 'Kaduna'
    Kano = 'Kano'
    Katsina = 'Katsina'
    Kebbi = 'Kebbi'
    Kogi = 'Kogi'
    Kwara = 'Kwara'
    Lagos = 'Lagos'
    Nasarawa = 'Nasarawa'
    Niger = 'Niger'
    Ogun = 'Ogun'
    Ondo = 'Ondo'
    Osun = 'Osun'
    Oyo = 'Ibadan'
    Plateau = 'Plateau'
    Rivers = 'Rivers'
    Sokoto = 'Sokoto'
    Taraba = 'Taraba'
    Yobe = 'Yobe'
    Zamfara = 'Zamfara'

    state = [
        (Abuja, 'Abuja'),
        (Abia, 'Abia'),
        (Adamawa, 'Adamawa'),
        (Akwa_Ibom, 'Akwa Ibom'),
        (Anambra, 'Anambra'),
        (Bauchi, 'Bauchi'),
        (Bayelsa, 'Bayelsa'),
        (Benue,	'Benue'),
        (Borno, 'Borno'),
        (Cross_River, 'Cross River'),
        (Delta, 'Delta'),
        (Ebonyi, 'Ebonyi'),
        (Edo, 'Edo'),
        (Ekiti, 'Ekiti'),
        (Enugu, 'Enugu'),
        (Gombe, 'Gombe'),
        (Imo, 'Imo'),
        (Jigawa, 'Jigawa'),
        (Kaduna, 'Kaduna'),
        (Kano, 'Kano'),
        (Katsina, 'Katsina'),
        (Kebbi, 'Kebbi'),
        (Kogi, 'Kogi'),
        (Kwara, 'Kwara'),
        (Lagos, 'Lagos'),
        (Nasarawa, 'Nasarawa'),
        (Niger, 'Niger'),
        (Ogun, 'Ogun'),
        (Ondo, 'Ondo'),
        (Osun, 'Osun'),
        (Oyo, 'Ibadan'),
        (Plateau, 'Plateau'),
        (Rivers, 'Rivers'),
        (Sokoto, 'Sokoto'),
        (Taraba, 'Taraba'),
        (Yobe, 'Yobe'),
        (Zamfara, 'Zamfara')
    ]
    # defining property type
    Shops = "Shops"
    Block_of_Flats = "Block_of_Flats"
    Land = "Land"
    Semi_Detached_Bungalow = "Semi_Detached_Bungalow"
    Detached_Bungalow = "Detached_Bungalow"
    Semi_Detached_Duplex = "Semi_Detached_Duplex"
    Detached_Duplex = "Detached_Duplex"
    Warehouse = "Warehouse"
    Commercial_Properties = "Commercial_Properties"
    property_type = [
        (Shops, "Shops"),
        (Block_of_Flats, "Block_of_Flats"),
        (Land, "Land"),
        (Semi_Detached_Bungalow, "Semi_Detached_Bungalow"),
        (Detached_Bungalow, "Detached_Bungalow"),
        (Semi_Detached_Duplex, "Semi_Detached_Duplex"),
        (Detached_Duplex, "Detached_Duplex"),
        (Warehouse, "Warehouse"),
        (Commercial_Properties, "Commercial_Properties")
    ]

    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    property_type = models.CharField(
        max_length=40, choices=property_type, default=Block_of_Flats)
    photos = ""
    property_state = models.CharField(
        max_length=30, choices=state, default=Lagos, verbose_name='State')
    address = models.TextField(max_length=600)
    vacancy = Int_max.IntegerRangeField(
        min_value=1, max_value=20, verbose_name='Number Available')
    property_rating = ArrayField(
        models.IntegerField(), size=50, null=True, blank=True)
    property_description = models.TextField(max_length=600)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"B{self.manager}"


class PropertyReview(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=True, blank=True)
    author_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
    review_text = models.TextField(max_length=500)
    cost = models.IntegerField()
    rating = Int_max.IntegerRangeField(
        min_value=1, max_value=5, verbose_name='Property Rating:')
    date_added = models.DateField(
        auto_now_add=True, verbose_name="Property Review Date")

    def __str__(self):
        return self.author_name


class ManagerReview(models.Model):
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, null=True, blank=True)
    author_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
    review_text = models.TextField(max_length=500)
    rating = Int_max.IntegerRangeField(
        min_value=1, max_value=5, verbose_name='Manager Rating:')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author_name
