from django.db import models


class Data(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  
    initial = models.TextField(db_column='Initial', blank=True, null=True) 
    mostcommonname = models.TextField(db_column='MostCommonName', blank=True, null=True)  
    scientificname = models.TextField(db_column='ScientificName', blank=True, null=True) 
    type = models.TextField(db_column='Type', blank=True, null=True)  
    description = models.TextField(db_column='Description', blank=True, null=True)  
    commonname1 = models.TextField(db_column='CommonName1', blank=True, null=True)  
    commonname2 = models.TextField(db_column='CommonName2', blank=True, null=True)  
    commonname3 = models.TextField(db_column='CommonName3', blank=True, null=True)  
    commonname4 = models.TextField(db_column='CommonName4', blank=True, null=True) 
    leaves1 = models.TextField(db_column='Leaves1', blank=True, null=True)  
    leaves2 = models.TextField(db_column='Leaves2', blank=True, null=True)  
    leaves3 = models.TextField(db_column='Leaves3', blank=True, null=True)  
    leaves4 = models.TextField(db_column='Leaves4', blank=True, null=True)  
    bark1 = models.TextField(db_column='Bark1', blank=True, null=True) 
    bark2 = models.TextField(db_column='Bark2', blank=True, null=True)  
    bark3 = models.TextField(db_column='Bark3', blank=True, null=True)  
    bark4 = models.TextField(db_column='Bark4', blank=True, null=True)  
    flowers1 = models.TextField(db_column='Flowers1', blank=True, null=True)  
    flowers2 = models.TextField(db_column='Flowers2', blank=True, null=True) 
    flowers3 = models.TextField(db_column='Flowers3', blank=True, null=True)  
    flowers4 = models.TextField(db_column='Flowers4', blank=True, null=True)  
    fruits1 = models.TextField(db_column='Fruits1', blank=True, null=True)  
    fruits2 = models.TextField(db_column='Fruits2', blank=True, null=True)  
    fruits3 = models.TextField(db_column='Fruits3', blank=True, null=True)  
    fruits4 = models.TextField(db_column='Fruits4', blank=True, null=True)  
    link1 = models.TextField(db_column='Link1', blank=True, null=True)  
    link2 = models.TextField(db_column='Link2', blank=True, null=True)  
    location = models.TextField(db_column='Location', blank=True, null=True) 
    map = models.TextField(db_column='Map', blank=True, null=True)  

    class Meta:
        db_table = 'Data'
