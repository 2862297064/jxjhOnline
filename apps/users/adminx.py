import xadmin
from xadmin import views
from xadmin.models import Log,Permission
from .models import *
from apps.operation.models import *
from apps.organization.models import *
from apps.course.models import *

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '即学即会IT课后台管理页面'
    site_footer = 'Powered By Bruce - 2020'
    # 收起菜单
    menu_style = "accordion"
    def get_site_menu(self):
        return (
            {'title': '课程管理', 'menus': (
                {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
            )},
            {'title': '机构管理', 'menus': (
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
            )},
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
            )},

            {'title': '系统管理', 'menus': (
                {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)


#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)