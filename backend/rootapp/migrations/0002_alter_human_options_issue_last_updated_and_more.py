# Generated by Django 4.2.4 on 2023-09-12 06:59

from django.db import migrations, models
import django.db.models.deletion
import guardapp.validators
import residentapp.validators
import rootapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='human',
            options={'verbose_name_plural': 'Human'},
        ),
        migrations.AddField(
            model_name='issue',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='guard',
            name='guard_id',
            field=models.CharField(default='GA-', max_length=10, unique=True, validators=[guardapp.validators.guard_id_validator]),
        ),
        migrations.AlterField(
            model_name='human',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other'), ('unknown', 'unknown')], default='unknown', max_length=7),
        ),
        migrations.AlterField(
            model_name='issue',
            name='details',
            field=models.TextField(verbose_name='Problem detail'),
        ),
        migrations.AlterField(
            model_name='record',
            name='e_type',
            field=models.CharField(choices=[('entry', 'Entry'), ('exit', 'Exit')], default='entry', max_length=5),
        ),
        migrations.AlterField(
            model_name='record',
            name='who',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rootapp.resident'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='resident_id',
            field=models.CharField(default='RS-', max_length=10, unique=True, validators=[residentapp.validators.resident_id_validator]),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='12666053C1A3', max_length=12, unique=True, validators=[rootapp.validators.token_validator]),
        ),
    ]
