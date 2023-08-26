from django.contrib import admin
# <HINT> Import any new Models here
from .models import Question, Choice
from .models import Course, Lesson, Instructor, Learner


# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline): # StackedInline
    model = Choice
    # extra = 5
    # pass

class QuestionInline(admin.ModelAdmin):
    inlines = [ChoiceInline]
    # pass
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question, QuestionInline)
# admin.site.register(Choice, ChoiceInline)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
