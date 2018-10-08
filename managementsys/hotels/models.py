# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self):
        return "%s" % (self.name)

    # def __unicode__(self):
    #     return "%s" % (self.name)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    hotel = models.ManyToManyField(Hotel, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class Staff(models.Model):
    hotel = models.ForeignKey(Hotel, blank=True)
    mobile_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


def hotel_receiver_function(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()


post_save.connect(hotel_receiver_function, sender=Hotel)
