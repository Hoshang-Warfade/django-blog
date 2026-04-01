from django.contrib import admin
from .models import About, SocialLinks

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if there are no existing About instances
        if About.objects.count() == 0:
            return True
        return False

# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLinks)