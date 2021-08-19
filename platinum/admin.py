from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Oil)
admin.site.register(Standard)
admin.site.register(OilInstance)
admin.site.register(Cart)