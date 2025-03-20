from django.contrib import admin
from .models import Usuario, Evento, Escala

class EscalaInline(admin.TabularInline):
    extra = 0
    model = Escala

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        gestor_list_display = ("username", "first_name","last_name", "email","cidade","atuacao","birthday", )
        admin_list_display = ("username", "first_name","last_name", "email","cidade","atuacao","is_staff","birthday",)
        if request.user.is_superuser:
            return admin_list_display
        elif request.user.groups.filter(name="Gestores").exists():
            return gestor_list_display
        else: 
            return super().get_list_display(request)
    
    search_fields = ("username", "cidade", "atuacao",)
    

    #list_filter = ("is_staff", "instrumento",)
    def get_list_filter(self, request):
        gestor_list_filter = ("atuacao",)
        admin_list_filter = ("is_staff","atuacao",)

        if request.user.is_superuser:
            return admin_list_filter
        elif request.user.groups.filter(name="Gestores").exists():
            return gestor_list_filter
        else: 
            return super().get_list_filter(request)


    def get_fieldsets(self, request, obj = None):
        fieldsets = super().get_fieldsets(request, obj)
        if request.user.is_superuser:
            return fieldsets
        
        my_fieldsets = (None, {
            "fields" : ("username", "first_name", "last_name","atuacao", "email", "cidade", "endereco", "is_active", "is_superuser", "is_staff",)
        })
        return (my_fieldsets,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        all_users = super().get_queryset(request)
        simple_users = Usuario.objects.exclude(is_superuser=True)

        if request.user.is_superuser:
            return all_users
        elif request.user.groups.filter(name="Gestores").exists():
            return simple_users
        else: 
            return queryset

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    @admin.display(description="Data")
    def data_formatada(self, obj):
        return obj.data.strftime("%d-%m-%Y",)
    
    @admin.display(description="Participantes")
    def numero_participantes(self, obj):
        return obj.participantes.count()

    inlines = [EscalaInline]
    list_display = ("titulo", "data_formatada", "numero_participantes")
    search_fields = ("titulo",)

#@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ("evento",)

 #   @admin.display(description="Birth decade")
  #  def decade_born_in(self):
   #     decade = self.birthday.year // 10 * 10
    #    return f"{decade}’s"
     
#class PersonAdmin(admin.ModelAdmin):
   # list_display = ["name", "decade_born_in"]

#admin.site.register(Usuario, UsuarioAdmin)
#admin.site.register(Escala, EscalaAdmin)
#admin.site.register(Evento, EventoAdmin)



# Register your models here.
