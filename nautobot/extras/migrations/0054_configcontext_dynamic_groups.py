# Generated by Django 3.2.16 on 2023-01-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0053_relationship_required_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="configcontext",
            name="dynamic_groups",
            field=models.ManyToManyField(
                blank=True, related_name="_extras_configcontext_dynamic_groups_+", to="extras.DynamicGroup"
            ),
        ),
    ]
