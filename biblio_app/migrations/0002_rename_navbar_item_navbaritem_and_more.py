# Generated by Django 4.1.2 on 2024-07-08 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='navbar_item',
            new_name='navbaritem',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='nombre_aut',
            new_name='nombreaut',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre_cat',
            new_name='nombrecat',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='anio_pub',
            new_name='aniopub',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='titulo_lib',
            new_name='titulolib',
        ),
        migrations.RenameField(
            model_name='navbaritem',
            old_name='titulo_nav',
            new_name='titulonav',
        ),
    ]