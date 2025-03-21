# Generated by Django 5.1.7 on 2025-03-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_delete_person_rename_instrumento_usuario_atuacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fisrt_funcao',
        ),
        migrations.AddField(
            model_name='usuario',
            name='first_funcao',
            field=models.CharField(blank=True, choices=[('1', 'Bateria'), ('2', 'Guitarra'), ('3', 'Vocal'), ('4', 'Teclado'), ('5', 'Baixo'), ('6', 'Violao'), ('7', 'Som'), ('8', 'Projetor'), ('9', 'Fotofilm'), ('10', 'Live'), ('11', 'Total Midia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='atuacao',
            field=models.CharField(blank=True, choices=[('1', 'Louvor'), ('2', 'Midia'), ('3', 'Midia e Louvor')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='secund_funcao',
            field=models.CharField(blank=True, choices=[('1', 'Bateria'), ('2', 'Guitarra'), ('3', 'Vocal'), ('4', 'Teclado'), ('5', 'Baixo'), ('6', 'Violao'), ('7', 'Som'), ('8', 'Projetor'), ('9', 'Fotofilm'), ('10', 'Live'), ('11', 'Total Midia')], max_length=50, null=True),
        ),
    ]
