# Generated by Django 4.1.7 on 2023-04-29 12:25

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user'), ('superuser', 'superuser')], default='user', max_length=9, verbose_name='Роль')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('car_brand', models.CharField(max_length=200, verbose_name='Марка автомобиля')),
                ('car_model', models.CharField(max_length=200, verbose_name='Модель автомобиля')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(unique=True, verbose_name='Дата приёма')),
                ('reserved', models.BooleanField(default=False, verbose_name='Зарезервировано клиентом')),
            ],
            options={
                'verbose_name': 'Назначение',
                'verbose_name_plural': 'Назначения',
                'ordering': ['dt'],
            },
        ),
        migrations.CreateModel(
            name='AppointmentsManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Описание')),
                ('interval', models.IntegerField(default=30, verbose_name='Интервал между назначениями')),
                ('start_time', models.TimeField(default=datetime.time(9, 0), verbose_name='Время начала работы')),
                ('finish_time', models.TimeField(default=datetime.time(21, 0), verbose_name='Время конца работы')),
                ('start_dt', models.DateField(verbose_name='Дата c которой создаем назначения')),
                ('finish_dt', models.DateField(verbose_name='Дата по которую создаем назначения включительно')),
            ],
            options={
                'verbose_name': 'Управление назначениями',
                'verbose_name_plural': 'Управление назначениями',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ComplexServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания услуги')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complex_services', to='shinata.category')),
            ],
            options={
                'verbose_name': 'Комплексная услуга',
                'verbose_name_plural': 'Комплексные услуги',
            },
        ),
        migrations.CreateModel(
            name='ComplexServicesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.complexservices')),
            ],
            options={
                'verbose_name': 'Комплексная услуга',
                'verbose_name_plural': 'Комплексные услуги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Итоговая стоимость заказа')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название категории товара')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('expired', models.BooleanField(default=False)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='shinata.appointment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to=settings.AUTH_USER_MODEL)),
                ('complex_services', models.ManyToManyField(through='shinata.ComplexServicesRecord', to='shinata.complexservices')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания услуги')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='shinata.category')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='RecordService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.record')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.service')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='services',
            field=models.ManyToManyField(through='shinata.RecordService', to='shinata.service'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200, verbose_name='Название товара')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='shinata/', verbose_name='Изображение товара')),
                ('in_stock', models.IntegerField(default=0, verbose_name='В наличии')),
                ('order_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shinata.productscategory')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products_category', to='shinata.productscategory')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, verbose_name='Количество товара в заказе')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена строки заказа')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orederitems', to='shinata.order')),
            ],
        ),
        migrations.CreateModel(
            name='ComplexServicesService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.complexservices')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.service')),
            ],
        ),
        migrations.AddField(
            model_name='complexservicesrecord',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shinata.record'),
        ),
        migrations.AddField(
            model_name='complexservices',
            name='services',
            field=models.ManyToManyField(through='shinata.ComplexServicesService', to='shinata.service'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='shinata.appointmentsmanager'),
        ),
    ]
