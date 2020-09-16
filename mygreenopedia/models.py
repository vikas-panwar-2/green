# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Data(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    initial = models.TextField(db_column='Initial', blank=True, null=True)  # Field name made lowercase.
    mostcommonname = models.TextField(db_column='MostCommonName', blank=True, null=True)  # Field name made lowercase.
    scientificname = models.TextField(db_column='ScientificName', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    commonname1 = models.TextField(db_column='CommonName1', blank=True, null=True)  # Field name made lowercase.
    commonname2 = models.TextField(db_column='CommonName2', blank=True, null=True)  # Field name made lowercase.
    commonname3 = models.TextField(db_column='CommonName3', blank=True, null=True)  # Field name made lowercase.
    commonname4 = models.TextField(db_column='CommonName4', blank=True, null=True)  # Field name made lowercase.
    leaves1 = models.TextField(db_column='Leaves1', blank=True, null=True)  # Field name made lowercase.
    leaves2 = models.TextField(db_column='Leaves2', blank=True, null=True)  # Field name made lowercase.
    leaves3 = models.TextField(db_column='Leaves3', blank=True, null=True)  # Field name made lowercase.
    leaves4 = models.TextField(db_column='Leaves4', blank=True, null=True)  # Field name made lowercase.
    bark1 = models.TextField(db_column='Bark1', blank=True, null=True)  # Field name made lowercase.
    bark2 = models.TextField(db_column='Bark2', blank=True, null=True)  # Field name made lowercase.
    bark3 = models.TextField(db_column='Bark3', blank=True, null=True)  # Field name made lowercase.
    bark4 = models.TextField(db_column='Bark4', blank=True, null=True)  # Field name made lowercase.
    flowers1 = models.TextField(db_column='Flowers1', blank=True, null=True)  # Field name made lowercase.
    flowers2 = models.TextField(db_column='Flowers2', blank=True, null=True)  # Field name made lowercase.
    flowers3 = models.TextField(db_column='Flowers3', blank=True, null=True)  # Field name made lowercase.
    flowers4 = models.TextField(db_column='Flowers4', blank=True, null=True)  # Field name made lowercase.
    fruits1 = models.TextField(db_column='Fruits1', blank=True, null=True)  # Field name made lowercase.
    fruits2 = models.TextField(db_column='Fruits2', blank=True, null=True)  # Field name made lowercase.
    fruits3 = models.TextField(db_column='Fruits3', blank=True, null=True)  # Field name made lowercase.
    fruits4 = models.TextField(db_column='Fruits4', blank=True, null=True)  # Field name made lowercase.
    link1 = models.TextField(db_column='Link1', blank=True, null=True)  # Field name made lowercase.
    link2 = models.TextField(db_column='Link2', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    map = models.TextField(db_column='Map', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Data'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TreeTree(models.Model):
    initial = models.CharField(db_column='Initial', max_length=2)  # Field name made lowercase.
    mostcommonname = models.CharField(db_column='MostCommonName', max_length=50)  # Field name made lowercase.
    scientificname = models.CharField(db_column='ScientificName', max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    commonname1 = models.CharField(db_column='CommonName1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commonname2 = models.CharField(db_column='CommonName2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commonname3 = models.CharField(db_column='CommonName3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commonname4 = models.CharField(db_column='CommonName4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaves1 = models.CharField(db_column='Leaves1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaves2 = models.CharField(db_column='Leaves2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaves3 = models.CharField(db_column='Leaves3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaves4 = models.CharField(db_column='Leaves4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fruits1 = models.CharField(db_column='Fruits1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fruits2 = models.CharField(db_column='Fruits2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fruits3 = models.CharField(db_column='Fruits3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fruits4 = models.CharField(db_column='Fruits4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link1 = models.CharField(db_column='Link1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link2 = models.CharField(db_column='Link2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
    map = models.CharField(db_column='Map', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tree_tree'
