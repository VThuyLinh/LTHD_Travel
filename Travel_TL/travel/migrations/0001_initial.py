# Generated by Django 5.0.6 on 2024-06-01 04:55

import ckeditor.fields
import cloudinary.models
import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(max_length=300)),
                ('sdt', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=300, null=True)),
                ('vaitro', models.CharField(choices=[('Staff', 'Staff'), ('Customer', 'Customer'), ('Admin', 'Admin')], max_length=30)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 55, 32, 688559))),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('Name_News', models.CharField(max_length=600)),
                ('Content', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Place', models.CharField(max_length=20, unique=True)),
                ('Place_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('DepartureDay', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('License', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500, null=True)),
                ('Path', cloudinary.models.CloudinaryField(max_length=255)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 55, 32, 688559))),
                ('Pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.album')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('Id_Tour', models.CharField(max_length=40)),
                ('Tour_Name', models.CharField(max_length=100)),
                ('Description', ckeditor.fields.RichTextField()),
                ('Days', models.IntegerField()),
                ('Nights', models.IntegerField()),
                ('Active', models.BooleanField(default=True)),
                ('Adult_price', models.FloatField(default=0, null=True)),
                ('Children_price', models.FloatField(default=0, null=True)),
                ('DeparturePlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Place.Tour_set+', to='travel.place')),
                ('DepartureTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.schedule')),
                ('Destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.place')),
                ('vehicle', models.ForeignKey(default='____', null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.transport')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating_Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('NumberOfStart', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travel.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateTimeField(auto_now=True)),
                ('FirstName_BookTour', models.CharField(default='', max_length=20)),
                ('LastName_BookTour', models.CharField(default='', max_length=20)),
                ('Phone_BookTour', models.CharField(default='', max_length=10)),
                ('Email_BookTour', models.CharField(default='', max_length=50)),
                ('Quantity_Adult', models.IntegerField(default=1)),
                ('Quantity_Children', models.IntegerField(default=0)),
                ('State', models.CharField(choices=[('Wait for Paid', 'Waitforpaid'), ('Paid', 'Paid'), ('Complete', 'Complete'), ('Reject', 'Reject')], max_length=50)),
                ('id_tour_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travel.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Tour_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('picture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.image')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='travel.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Avatar', models.ImageField(max_length=1000, upload_to='Travel/%Y/%m/')),
                ('id_Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_User+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('travel.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('DateAdd', models.DateField(auto_now_add=True)),
                ('id_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Staff_User+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('travel.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Like_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travel.news')),
            ],
            options={
                'unique_together': {('news', 'user')},
            },
        ),
        migrations.CreateModel(
            name='CMT_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.news')),
            ],
            options={
                'unique_together': {('news', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Like_Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.tour')),
            ],
            options={
                'unique_together': {('tour', 'user')},
            },
        ),
        migrations.CreateModel(
            name='CMT_Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngày đăng', models.DateTimeField(auto_now_add=True)),
                ('Ngày cập nhật', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travel.tour')),
            ],
            options={
                'unique_together': {('tour', 'user')},
            },
        ),
    ]
