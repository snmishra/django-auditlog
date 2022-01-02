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
        ("auditlog", "0003_logentry_remote_addr"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="additional_data",
            field=JSONField(null=True, blank=True),
        ),
    ]
