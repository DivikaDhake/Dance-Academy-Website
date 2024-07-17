# students/migrations/0002_add_gender_field.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='style',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='student',
            name='state',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='noemail@example.com'),
        ),
    ]
