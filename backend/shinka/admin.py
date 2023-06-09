from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from django.utils.timezone import now
from shinka.models import (Record, Service, ServiceCategory, Appointment, Client, RecordService, ProductsCategory, Product,
                            AppointmentsManager, ServiceGroup, FAQ)

from rangefilter.filters import DateRangeFilterBuilder
from shinka.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Client
    list_display = ('username', 'phone', 'email', 'car_brand', 'car_model')
    list_filter = ('role', )
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'password', 'car_brand', 'car_model')}),
        ('Permissions', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'phone', 'email', 'password1', 'password2', 'car_brand', 'car_model', 'role',
                
            )}
        ),
    )
    search_fields = ('username', 'phone', 'email', 'car_brand', 'car_model')
    ordering = ('username',)

admin.site.register(Client, CustomUserAdmin)


class RecordInline(admin.ModelAdmin):
    list_filter = [('appointment__dt', DateRangeFilterBuilder()), ]
    search_fields = ['client__username', 'client__phone', 'client__email',
                     'client__car_model', 'client__car_brand']

    def get_form(self, request, obj=None, **kwargs):
        form = super(RecordInline, self).get_form(request, obj, **kwargs)
        form.base_fields['appointment'].queryset = Appointment.objects.filter(
            reserved=False, dt__gt=now())
        return form


class AppointmentAdmin(admin.ModelAdmin):
    list_filter = [('dt', DateRangeFilterBuilder()), 'reserved']
    
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ['description', 'group__title']   
    

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'description']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsCategory)
admin.site.register(Record, RecordInline)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AppointmentsManager)
admin.site.register(ServiceGroup)
admin.site.register(FAQ)