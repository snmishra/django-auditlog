try:
    from jsonfield.fields import JSONField
except ImportError:
    try:
        from django.db.models import JSONField
    except ImportError:
        from django.contrib.postgres.fields import JSONField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0004_logentry_detailed_object_repr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="additional_data",
            field=JSONField(null=True, verbose_name="additional data", blank=True),
        ),
    ]
