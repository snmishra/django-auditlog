from django.db import migrations, models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0007_object_pk_type.py"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="additional_data",
            field=JSONField(null=True, verbose_name="additional data", blank=True),
        ),
    ]
