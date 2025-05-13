# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RawConso(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    type_vehicule = models.TextField(db_column='Type_vehicule', blank=True, null=True)  # Field name made lowercase.
    immat = models.TextField(blank=True, null=True)
    score_heure = models.FloatField(db_column='Score_Heure', blank=True, null=True)  # Field name made lowercase.
    vitesse = models.BigIntegerField(db_column='Vitesse', blank=True, null=True)  # Field name made lowercase.
    frein_brusques = models.BigIntegerField(db_column='Frein_brusques', blank=True, null=True)  # Field name made lowercase.
    acc_brusques = models.BigIntegerField(db_column='Acc_brusques', blank=True, null=True)  # Field name made lowercase.
    virages_brusques = models.BigIntegerField(db_column='Virages_brusques', blank=True, null=True)  # Field name made lowercase.
    surregime = models.BigIntegerField(db_column='Surregime', blank=True, null=True)  # Field name made lowercase.
    total_points = models.BigIntegerField(db_column='Total_points', blank=True, null=True)  # Field name made lowercase.
    temps = models.TextField(db_column='Temps', blank=True, null=True)  # Field name made lowercase.
    distance = models.FloatField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.
    conso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_conso'


class RawEntretiens(models.Model):
    year = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    immat = models.TextField(blank=True, null=True)
    kms = models.FloatField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    cat = models.TextField(blank=True, null=True)
    operation = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_entretiens'


class RawImmat(models.Model):
    immat = models.TextField(blank=True, null=True)
    type_vehicule = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_immat'
