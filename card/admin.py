from django.contrib import admin
# Register your models here.
from . import models

admin.site.site_title = "校园卡支付管理系统"
admin.site.site_header = "校园卡支付管理系统"
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'sex', 'c_time', 'card', 'name', )  # list
    list_filter = ('username', 'card', 'name',)
    search_fields = ('card',)
    fieldsets = (
        ['信息栏', {
            'fields': ('username', 'password', 'email', 'sex', 'c_time', 'card', 'name', ),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('onlyid',),
        }]
    )
class CardmoneyAdmin(admin.ModelAdmin):
    list_display = ('card', 'rest_money', 'consume_money', 'consume_time', 'username',)  # list
    list_filter = ('card', 'consume_time', 'username',)
    search_fields = ('card',)
    fieldsets = (
        ['信息栏', {
            'fields': ('card', 'rest_money', 'consume_money', 'consume_time', 'username',),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('card',),
        }],
    )
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Cardmoney, CardmoneyAdmin)