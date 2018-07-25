from django.contrib import admin

# Register your models here.

from .models import Grades, Students

#注册
class StudentsInfo(admin.TabularInline):  #或者(admin.StackedInline)
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk', "gname", 'gdate', 'ggirlnum','gboynum','idDelete']   # 显示字段
    list_filter = ['gname']                                                    # 过滤字段
    search_fields = ['gname']                                                  # 搜索字段
    list_per_page = 5                                                          # 分页

    #添加丶修改页属性
    #fields = ['ggirlnum', 'gboynum','gname', 'gdate', 'idDelete']             # 规定属性的先后顺序
    fieldsets = [
         ("num", {"fields" : ['ggirlnum', 'gboynum']}),
         ("base", {"fields" : ['gname', 'gdate', 'idDelete']}),
     ]                                                                         # 给属性分组
admin.site.register(Grades, GradesAdmin)

@admin.register(Students)   #等同于①
class StudentsAdmin(admin.ModelAdmin):

    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"

    def Delete(self):
        if self.isDelete:
            return "是"
        else:
            return "否"
    Delete.short_description =  "是否删除"

    list_display = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', Delete]
    list_per_page = 10

    #执行动作的位置
    actions_on_top = False
    actions_on_button = True

#① admin.site.register(Students, StudentsAdmin)

