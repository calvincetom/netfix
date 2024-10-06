"""Imports for django ORM scema mapping."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    Attributes:
        is_company (bool): A boolean flag indicating whether the user is a company.
        is_customer (bool): A boolean flag indicating whether the user is a customer.
        email (str): The email field for the user, which is required to be unique.
    """
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.CharField(max_length=100, unique=True)


class Customer(models.Model):
    """
    Customer model.
    
    Currently empty but can be extended with attributes and relationships
    relevant to customers in future developments.
    """

class Company(models.Model):
    """
    Company model representing companies in the system.
    
    Attributes:
        user (User): A one-to-one relationship to the User model, where each company 
                     is associated with exactly one user.
        field (str): A field describing the company's area of expertise, with a 
                     predefined set of choices.
        rating (int): The company's rating, with a default value of 0, validated to 
                      be between 0 and 5.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(
        max_length=70,
        choices=(
            ('Air Conditioner', 'Air Conditioner'),
            ('All in One', 'All in One'),
            ('Carpentry', 'Carpentry'),
            ('Electricity', 'Electricity'),
            ('Gardening', 'Gardening'),
            ('Home Machines', 'Home Machines'),
            ('House Keeping', 'House Keeping'),
            ('Interior Design', 'Interior Design'),
            ('Locks', 'Locks'),
            ('Painting', 'Painting'),
            ('Plumbing', 'Plumbing'),
            ('Water Heaters', 'Water Heaters')
        ),
        blank=False, null=False
    )
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        """
        String representation of the Company model, displaying the user ID and username.
        
        Returns:
            str: The user ID and username in the format 'id - username'.
        """
        return f'{self.user.id} - {self.user.username}'  # pylint: disable=E1101
