from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title_white = models.CharField(max_length=255, blank=True)
    title_red = models.CharField(max_length=255, blank=True)
    heading = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    what_do = models.TextField(blank=True)
    Why_Choose_Softvence = models.TextField(blank=True)
    our_misson = models.TextField(blank=True)
    count_01_title = models.CharField(max_length=255, blank=True)
    count_01 = models.IntegerField(default=0)
    count_02_title = models.CharField(max_length=255, blank=True)
    count_02 = models.IntegerField(default=0)
    button_text = models.CharField(max_length=255, blank=True)
    button_url = models.URLField(blank=True)
    team_section_title_1 = models.CharField(max_length=255, blank=True)
    team_section_title_2 = models.CharField(max_length=255, blank=True)
    testimonial_section_title_1 = models.CharField(max_length=255, blank=True)
    testimonial_section_title_2 = models.CharField(max_length=255, blank=True)
    client_section_title_1 = models.CharField(max_length=255, blank=True)
    client_section_title_2 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "About Us Content"
    



class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class (e.g., fa-solid fa-code)")

    def __str__(self):
        return self.title



class ContactUs(models.Model):
    Title=models.CharField(max_length=100)
    call_us=models.IntegerField(null=True, blank=True)
    mail=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    map=models.TextField()

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
