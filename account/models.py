from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import numpy as np
import random
import string

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    pic = models.ImageField(upload_to="profile_pic/", null=True, blank=True)
    friends = models.ManyToManyField('chatapp.Friend', related_name="my_friends", blank=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a profile picture if not provided.
        """
        if not self.pic:  # If profile picture is not provided
            # Use username if name is not provided
            text = self.name if self.name else self.user.username
            image_path = self.generate_profile_pic(text)
            self.pic.name = image_path  # Save the path of generated image as the profile picture
        super().save(*args, **kwargs)

    def generate_profile_pic(self, text):
        """
        Generate a profile picture using PIL and save it.
        """
        rndm_text = ''.join(random.choices(string.ascii_letters, k=7))
        image_path = f"/profile_pic/{text}_{rndm_text}.png"
        font_size = 21
        text = str(text)

        font_design = ImageFont.truetype("static/fonts/Roboto-Black.ttf", font_size)

        # Calculate Hieght Width According FontSize and Text
        text_width, text_height = font_design.getbbox(
            text)[2], font_design.getbbox(text)[3]

        # Create a transparent background image
        image = Image.new("RGBA", (text_width, text_height),(255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Draw the text on the image
        draw.text((0, 0), text, fill=(0, 0, 0), font=font_design)

        # Convert the PIL image to a NumPy array
        image_np = np.array(image)

        # Save the image
        with open(settings.MEDIA_ROOT + image_path, "wb") as f:
            Image.fromarray(image_np).save(f)

        return image_path

    def preview(self):
        return mark_safe(f'''
                <figure class="figure">
                    <img src="{self.pic.url}" class="figure-img img-fluid rounded" alt="Profile Pic" height="100" width="100">
                </figure>
                ''')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class OtpCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.code