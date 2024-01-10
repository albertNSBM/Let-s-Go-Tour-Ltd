from decimal import Decimal 
import stripe
from django.conf import settings
from django.shortcuts import render, redirect,reverse,\
                             get_object_or_404
from orders.models import Order


# Create the stripe instance 

