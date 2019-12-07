from django.db import models

class HeaderSliderContent(models.Model):
    SliderImagesOne = models.ImageField(upload_to='sliders/', blank=True )
    SliderImagesTwo = models.ImageField(upload_to='sliders/', blank=True)
    SliderImagesThree = models.ImageField(upload_to='sliders/', blank=True)
    SliderImagesFour = models.ImageField(upload_to='sliders/', blank=True)
    GetStartedHref = models.CharField(max_length=520, blank=True)
    SliderContentOne = models.CharField(max_length=520, blank=True)
    SliderContentTwo = models.CharField(max_length=520, blank=True)
    SliderContentThree = models.CharField(max_length=520, blank=True)
    SliderContentFour = models.CharField(max_length=520, blank=True)
    SliderContentFive = models.CharField(max_length=520, blank=True)

    def __str__(self):
        return self.SliderContentOne



class Team(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="Teams/")
    details = models.TextField()
    experience = models.TextField()
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name



