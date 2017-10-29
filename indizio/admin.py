from django.contrib import admin
from .models import Indizio, Scelta

# class SceltaConIndizio(admin.StackedInline):
# 	model = Scelta
# 	extra = 3

# class IndizioAdmin(admin.ModelAdmin):
# 	inlines = [SceltaConIndizio]

admin.site.register(Indizio)
admin.site.register(Scelta)

