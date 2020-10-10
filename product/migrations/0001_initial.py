# Generated by Django 2.2.4 on 2019-09-09 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
                ('prating', models.IntegerField(default=0)),
                ('pshort_description', models.CharField(default='', max_length=300)),
                ('plong_description', models.CharField(default='', max_length=2000)),
                ('pmanufacturer', models.CharField(default='', max_length=2000)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('pcolor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Color')),
                ('psize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Size')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]