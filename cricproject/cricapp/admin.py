from django.contrib import admin
from cricapp.models import player
class playerAdmin(admin.ModelAdmin):
    '''
        Admin View for player
    '''
    list_display = ('id','name','jersy_num','address','department',)
   

admin.site.register(player, playerAdmin)
		
# Register your models here.
