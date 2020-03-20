# Generated by Django 3.0.3 on 2020-03-20 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(null=True)),
                ('task_id', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AsiteOffsetsJob',
            fields=[
                ('job_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aipservice.Job')),
                ('species', models.CharField(choices=[('yeast', 'S. cerevisiae'), ('ecoli', 'E. coli'), ('mouse', 'Mouse'), ('other', 'Other')], max_length=10)),
                ('bam_file', models.FilePathField(path='/files/input')),
                ('annotation_file', models.FilePathField(path='/files/input')),
                ('fasta_file', models.FilePathField(path='/files/input')),
                ('filter_file', models.FilePathField(blank=True, null=True, path='/files/input')),
                ('include', models.BooleanField()),
                ('min_frag', models.IntegerField()),
                ('max_frag', models.IntegerField()),
                ('three_prime', models.BooleanField()),
                ('overlap', models.IntegerField()),
                ('threshold_avg_reads', models.IntegerField()),
                ('threshold_gene_pct', models.IntegerField()),
                ('threshold_start_codon', models.IntegerField()),
                ('alignment_type', models.CharField(max_length=100)),
                ('get_profile', models.BooleanField()),
            ],
            bases=('aipservice.job',),
        ),
        migrations.CreateModel(
            name='AsiteProfilesJob',
            fields=[
                ('job_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aipservice.Job')),
                ('species', models.CharField(choices=[('yeast', 'S. cerevisiae'), ('ecoli', 'E. coli'), ('mouse', 'Mouse'), ('other', 'Other')], max_length=10)),
                ('bam_file', models.FilePathField(path='/files/input')),
                ('annotation_file', models.FilePathField(path='/files/input')),
                ('fasta_file', models.FilePathField(path='/files/input')),
                ('offset_file', models.FilePathField(path='/files/input')),
                ('min_frag', models.IntegerField()),
                ('max_frag', models.IntegerField()),
                ('three_prime', models.BooleanField()),
                ('overlap', models.IntegerField()),
                ('alignment_type', models.CharField(max_length=100)),
            ],
            bases=('aipservice.job',),
        ),
    ]
