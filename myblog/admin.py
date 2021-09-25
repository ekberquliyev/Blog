from django.contrib import admin
from myblog.models import NavbarModel, PostImageModel, PostModel, Settings, Footer, AboutModel,PostContactModel
# Register your models here.

admin.site.register(NavbarModel)
admin.site.register(Footer)
admin.site.register(Settings)

admin.site.register(PostModel)
admin.site.register(PostImageModel)

admin.site.register(AboutModel)
admin.site.register(PostContactModel)

