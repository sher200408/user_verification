# from django o'zini import qilinganlar
from django.contrib import admin

# from fayilar olingalar uchun
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Fixed 'auther' typo and converted to recommended tuple format "auther" xatosi tuzatildi va tavsiya etilgan tuple formatiga o'tkazildi
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    # Standard filtering and searching Standart filtrlash va qidiruv
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')

    # Corrected: date_hierarchy MUST be a string Tuzatildi: date_hierarchy satr bo'lishi shart
    date_hierarchy = 'publish'

    # Corrected: prepopulated_fields should use a tuple for the source field Tuzatildi: prepopulated_fields manba maydoni uchun juftlikdan foydalanishi kerak
    prepopulated_fields = {'slug': ('title',)}

    # Advanced UI options kengaytirilgan interfeys sozlamalari
    raw_id_fields = ('author',)  # Better for performance with many users
    ordering = ('status', 'publish')

### Bu juda xato boldi chunki keyin  versionlar ishlash karak unda ham bolmadim
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title','slug','auther','publish','status']
#     list_filter = ['status','created','publish','author']
#     search_fields = ['title','body']
#     prepopulated_fields = {'slug':('title', )}
#     raw_id_fields = ['author']
#     date_hierarchy = ['publish']
#     ordering = ['status','publish']
