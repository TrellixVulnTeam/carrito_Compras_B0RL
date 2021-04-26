# Generated by Django 3.0.4 on 2021-04-25 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Categoria', '0001_initial'),
        ('Producto', '0002_producto_categoria_producto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria_Producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre_Producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Categoria.Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='producto',
            name='name',
            field=models.CharField(default=5, max_length=150, unique=True, verbose_name='Nombre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
