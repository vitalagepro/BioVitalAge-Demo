# Generated by Django 5.1.1 on 2024-11-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioVitalAge_Login', '0005_persona_aa_dha_persona_aa_epa_persona_albumin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='EOSI',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='albumina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='albuminemia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='alfa_1',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='alfa_2',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='azotemia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='beta_1',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='beta_2',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='bilirubina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='biological_age',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='calcio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='chetoni',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='cloruri',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='colesterolo_hdl',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='colesterolo_ldl',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='colesterolo_totale',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='creatina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='ferritina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fosfatasi_alcanica',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fosforo',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='gamma',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='gamma_gt',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='glicemia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='glucosio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='home_test',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='insulina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='ir_test',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='leucociti',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='magnesio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='mpv',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='mvc',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='omoicisteina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='pcr',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='pdw',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='peso_specifico',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='ph',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='plt',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='potassio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='proteine',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='proteine_totali',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='rdw_cv',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='rdw_sv',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='sangue',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='sideremia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='sodio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='transaminasi_gop',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='transaminasi_gpt',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='trasferrina',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='trigliceridi',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='urobilinogeno',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='ves',
        ),
        migrations.AddField(
            model_name='persona',
            name='codice_fiscale',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='mcv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='aa_dha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='aa_epa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='albumin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='baso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='bilirubin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cardiovascular_risk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='chronological_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='creatinine',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='d_roms',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ferritin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='glucose',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='hct',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='hgb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='homa_test',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='lymph',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mch',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mchc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='mono',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='neut',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='obri_index',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='osi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='pat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rbc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='uric_acid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='wbc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='eosi',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]