from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class UserModel(models.Model):
    PLEC_CHOICES = [
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
    ]

    imie = models.CharField(max_length=25)
    drugie_imie = models.CharField(blank=True, null=True, max_length=25)
    nazwisko = models.CharField(max_length=50)
    haslo = models.CharField(max_length=100)
    pesel = models.CharField(max_length=11, unique=True)
    data_urodzenia = models.DateField()
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    ulica = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=6)
    miasto = models.CharField(max_length=50)
    telefon = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True)
    utworzony = models.DateTimeField(auto_now_add=True)
    

    def hash_password(self, raw_password):
        self.haslo = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.haslo)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
