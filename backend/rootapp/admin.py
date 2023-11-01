from django.contrib import admin
from .models import Human, Block, Resident, Guard, TempToken, Guest, Record, Issue, Bill

admin.site.register(Block)
admin.site.register(Resident)
admin.site.register(Guest)
admin.site.register(Record)
admin.site.register(Issue)
admin.site.register(Bill)


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Typical issues', {'fields': ['user', 'nid_or_br', 'contact', 'date_of_birth']}),
        ('Physical Issues', {'fields': ['gender']}),
        ('Other', {'fields': ['photo']})
    ]


@admin.register(Guard)
class GuardAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'human':
            kwargs['queryset'] = Human.objects.filter(gender='male')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TempToken)
class TokenAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = ['token']
