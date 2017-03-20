from django.contrib import admin

from .models import Movie, Category, Relationship

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields':['title']}),
        ('Description', {'fields':['description']}),
        ('Duration (minutes)', {'fields':['movie_length']}),
        ('Release Date', {'fields':['movie_release_date']}),
        ]

class CategoryAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Type',{'fields':['c_type']}),
        ('Value',{'fields':['value']}),
        ] 

class RelationshipAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Taxonomy',{'fields':['taxonomy']}),
        ('Movie',{'fields':['r_movie']}),
        ] 
    
    
#  list_display = ('title','','','')
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Relationship, RelationshipAdmin)
