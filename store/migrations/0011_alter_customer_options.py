# Generated by Django 4.1.5 on 2023-02-10 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_alter_orderitem_product"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ["user__first_name", "user__last_name"],
                "permissions": [("view_histroy", "Can view history")],
            },
        ),
    ]
