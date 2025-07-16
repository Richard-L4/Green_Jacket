from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # type: ignore


class Category(models.Model):
    """
    Represents a category of items, with optional parent categories
    to allow hierarchical organization (e.g., subcategories).
    """

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the user-friendly version of the category name,
        or the raw name if no friendly name is set.
        """
        return self.friendly_name or self.name


class Item(models.Model):
    """
    Represents an item in the shop.
    Each item may belong to a category and can include a Cloudinary image.
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class SavedItem(models.Model):
    """
    Represents an item saved for later by a user.
    Users cannot save the same item more than once.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='saved_items'
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='saved_by_users'
    )
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')
        verbose_name = 'Saved Item'
        verbose_name_plural = 'Saved Items'

    def __str__(self):
        return f"{self.user.username} saved {self.item.name}"


class Review(models.Model):
    """
    Represents a written review for anvitem by a user.
    Each user can leave only one review per item.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='reviews'
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f"Review by {self.user.username} on {self.item.name}"
