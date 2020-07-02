from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Payment, Question, Choice, Statistic, Answered


class PaymentAdmin(admin.ModelAdmin):
    pass

class StatisticInLine(admin.TabularInline):
    model = Statistic


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'phone_number',)
    fieldsets = [
        ('User ingormation', {
            'fields': ['username', 'phone_number']}),
    ]
    inlines = [StatisticInLine]

class AnsweredAdmin(admin.ModelAdmin):
    list_display = ('question', 'answered_user','answered_time')
    search_fields = ['user']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Statistic)
admin.site.register(Answered,AnsweredAdmin)