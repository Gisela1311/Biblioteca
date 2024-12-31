from django.db import models

class Persona(models.Model):
    nombre_opciones = [
        ('', 'Tria una opció'),
        ('1', 'Josep'),
        ('2', 'Gisela'),
    ]
    nombre = models.CharField(verbose_name='Nom', choices=nombre_opciones, default='', max_length=1)

    class Meta:
        abstract = True

    def __str__(self):
        return self.get_nombre_display()

class Propietari(Persona):
    prop_fk = models.SmallAutoField(verbose_name="id propietari", primary_key=True)

class Llibre(models.Model):
    llib_pk = models.SmallAutoField(verbose_name="id llibre", primary_key=True)
    llib_nom = models.CharField(max_length=150, verbose_name="nom del llibre")
    llib_autor = models.CharField(max_length=100, verbose_name="autor del llibre")
    llib_editorial = models.CharField(max_length=100, verbose_name="editorial")
    genere = [
        ('', 'Tria una opció'),
        ('1', 'Assaig'),
        ('2', 'Novel·la'),
        ('3', 'Novel·la policíaca'),
        ('4', 'Novel·la romàntica'),
        ('5', 'Novel·la històrica'),
        ('6', 'Novel·la fantàstica'),
        ('7', 'Filosofia'),
        ('8', 'Mitologia'),
        ('9', 'Poesía'),
        ('10', 'Còmic'),
        ('11', 'Història'),
        ('12', 'Art'),
        ('13', 'Biografia'),
        ('14', 'Teatre')
    ]
    llib_genere = models.CharField(verbose_name="génere literari", choices=genere, max_length=2, blank=True)
    llib_pagines = models.IntegerField(verbose_name='número de pàgines del llibre')
    llib_propietari = models.ForeignKey(Propietari, on_delete=models.CASCADE, verbose_name="propietari del llibre", null=True)
    llib_data_lectura = models.DateField()
    llib_portada = models.ImageField(upload_to='portadas/', verbose_name='Portada del llibre', null=True, blank=True)

    def __str__(self):
        return self.llib_nom

class Lector(Persona):
    lec_fk = models.SmallAutoField(verbose_name='id del lector', primary_key=True)
    llib_nom_fk = models.ForeignKey(Llibre, on_delete=models.CASCADE, verbose_name='llibres llegits')
