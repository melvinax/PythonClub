

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.migration):
    initial = True
    dependencies = [migration.swappable_dependency(settings.AUTH_USER_MODEL)]

operation = [ migrations.CreateModel(
    name='Event',
    fields=[ ('id', models.AutoField(auto_created))]
)]