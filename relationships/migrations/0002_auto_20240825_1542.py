# Generated by Django 2.0.13 on 2024-08-25 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='site',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='relationships', to='sites.Site', verbose_name='site'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='relationships.RelationshipStatus', verbose_name='status'),
        ),
    ]
