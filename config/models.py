# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comments(models.Model):
    comments_id = models.IntegerField(primary_key=True)
    comment_date = models.DateField()
    comment_contents = models.CharField(max_length=100)
    comment_like = models.IntegerField()
    post = models.ForeignKey('Post', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class HealthInfo(models.Model):
    health_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_info'


class Ingredient(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class Nutraceuticals(models.Model):
    nutraceuticals_id = models.IntegerField(primary_key=True)
    nutraceuticals_name = models.CharField(max_length=100)
    nutraceuticals_categroy = models.CharField(max_length=1)
    nutraceuticals_rating = models.IntegerField()
    nutraceuticals_effects = models.CharField(max_length=100)
    nutraceuticals_side_effects = models.CharField(max_length=100)
    nutraceuticals_company = models.CharField(max_length=100)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nutraceuticals'


class OnelineReview(models.Model):
    online_review_id = models.IntegerField(primary_key=True)
    review_rating = models.IntegerField()
    review_contents = models.CharField(max_length=500)
    nutraceuticals = models.ForeignKey(Nutraceuticals, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oneline_review'


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_date = models.DateField()
    post_title = models.CharField(max_length=100)
    post_contents = models.CharField(max_length=100)
    post_like = models.IntegerField()
    post_category = models.CharField(max_length=9)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_login_id = models.CharField(max_length=100)
    user_loing_password = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_weight = models.FloatField(blank=True, null=True)
    user_height = models.FloatField(blank=True, null=True)
    user_nickname = models.CharField(max_length=100)
    user_sex = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'


class UserNutraceuticals(models.Model):
    user_nutraceuticals_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    nutraceuticals = models.ForeignKey(Nutraceuticals, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_nutraceuticals'


class UserReview(models.Model):
    user_review_id = models.IntegerField(primary_key=True)
    review_rating = models.IntegerField()
    review_contents = models.CharField(max_length=500)
    user = models.ForeignKey(User, models.DO_NOTHING)
    nutraceuticals = models.ForeignKey(Nutraceuticals, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_review'
