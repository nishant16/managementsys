# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin

from hotels.models import Hotel, Customer, Staff

admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Staff)

