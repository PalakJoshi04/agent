# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('landmark', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('foreign_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('media_name', models.CharField(max_length=20)),
                ('media_path', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tagent8.Media')),
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tagent8.ContactInfo')),
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=100)),
                ('experence', models.IntegerField()),
                ('agent_notes', models.TextField()),
            ],
            bases=('tagent8.contactinfo', 'tagent8.media'),
        ),
        migrations.AddField(
            model_name='location',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagent8.Agent'),
        ),
        migrations.AddField(
            model_name='address',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagent8.Agent'),
        ),
    ]