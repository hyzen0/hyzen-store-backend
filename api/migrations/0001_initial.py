from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):

    

    def seed_data(apps, schema_editor):
        user = CustomUser(name = "hyzen", email="hail4heisenberg@gmail.com", is_staff=True, is_superuser=True, phone="7465076150", gender="Male")
        user.set_password("imbatman")
        user.save()

    dependencies = []

    operations= [
        migrations.RunPython(seed_data),
    ]
