from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Badge



@receiver(post_migrate)
def create_default_badges():
        # Create default badges if they don't exist
        for badge_data in [
            {
                'title': 'Gold Badge Title',
                'description': 'Gold Badge Description',
                'image': './badges/badge_gold.jpg',
            },
            {
                'title': 'Silver Badge Title',
                'description': 'Silver Badge Description',
                'image': './badges/badge_silver.jpg',
            },
            {
                'title': 'Bronze Badge Title',
                'description': 'Bronze Badge Description',
                'image': './badges/badge_bronze.jpg',
            },
        ]:
            Badge.objects.get_or_create(badge_data)






