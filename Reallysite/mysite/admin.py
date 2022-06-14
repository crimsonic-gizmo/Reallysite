from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User

# Register your models here.
#管理画面の表示を編集
#通常のモデルは簡単にできる
#カスタムユーザモデルの場合は記載が必要

class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {
			'fields':(
				'email',
				'password',
			)
		}),
		(None, {
			'fields':(
				'is_active',
				'is_admin',
			)
		})
	)

	list_display = ('email', 'is_active')
	list_filter = ()
	ordering = ()
	filter_horizontal = ()

# admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)


