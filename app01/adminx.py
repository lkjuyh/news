import xadmin
from app01.models import *
from xadmin import views


# Register your models here.

class TypeAdmin:
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
    list_filter = ["id", "name"]
    ordering = ["id"]


class ContentAdmin:
    list_display = ["id", "title", "picture"]
    search_fields = ["id", "publish_time", "title", "picture"]
    ordering = ["-publish_time"]


class CommentAdmin:
    list_display = ["id", "content", "user_id", "news_id", "state"]
    search_fields = ["id", "publish_time", "user_id", "news_id"]
    list_editable = ["state"]
    ordering = ["-publish_time"]


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = "后台管理系统"
    site_footer = "底部信息"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(Comment, CommentAdmin)
