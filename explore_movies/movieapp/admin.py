from django.contrib import admin

from movieapp.models import Malayalam, English, Hindi

# Register your models here.
admin.site.register(Malayalam)
admin.site.register(English)
admin.site.register(Hindi)