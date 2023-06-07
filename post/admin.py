from django.contrib import admin
from .models import Article, Category, Podcast, Event, Comment, Image, Journal


@admin.action(description="published selected items")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


@admin.action(description="drafted selected items")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")


@admin.action(description="accepted selected items")
def make_accept(modeladmin, request, queryset):
    queryset.update(status="a")


@admin.action(description="make waiting selected items")
def make_waiting(modeladmin, request, queryset):
    queryset.update(status="w")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'author', 'status', 'created_at', 'updated_at', 'count')
    prepopulated_fields = {'slug': ('en_title',)}
    list_filter = ('status',)
    raw_id_fields = ('comment',)
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'status', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('en_title',)}
    list_filter = ('status',)
    raw_id_fields = ('comment',)
    actions = [make_published, make_draft]


admin.site.register(Podcast, PodcastAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'in_menu')
    prepopulated_fields = {'slug': ('en_name',)}


admin.site.register(Category, CategoryAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_active', 'user_count')
    prepopulated_fields = {'slug': ('en_title',)}

    def user_count(self, obj):
        return obj.user_count()

    def user_list(self, obj):
        return obj.user_list()

    readonly_fields = ('user_count', 'user_list')
    raw_id_fields = ('users',)
    fieldsets = [
        ('description', {'fields': ('title', 'en_title', 'slug'), },),
        ('event', {'fields': ('image', 'content', 'date', 'expire_time', 'is_active', 'time', 'place', 'provider', 'max_user')}),
        ('users', {"classes": ["collapse"], 'fields': ('users', 'user_count', 'user_list')}),
    ]


admin.site.register(Event, EventAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'post_type', 'post_slug')
    list_filter = ('status', 'post_type')
    actions = [make_accept, make_waiting]


admin.site.register(Comment, CommentAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_preview',)


admin.site.register(Image, ImageAdmin)


class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'src')


admin.site.register(Journal, JournalAdmin)
