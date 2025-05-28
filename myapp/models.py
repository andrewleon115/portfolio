from django.db import models

# Create your models here.
# 3. About Model
class About(models.Model):
    

    bio = models.TextField()
    role = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.role or "About Entry"
    

class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True, null=True)

    logo = models.ImageField(upload_to='experience_logos/')

    def __str__(self):
        return f"{self.company_name} ({self.start_year} - {self.end_year})"
    

# models.py

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"{self.project.title} Image"

class ClientLogo(models.Model):
    project = models.ForeignKey(Project, related_name='client_logos', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='client_logos/')

    def __str__(self):
        return f"{self.project.title} Client Logo"




class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    projects_completed = models.PositiveIntegerField()
    
    icon = models.FileField(upload_to='skill_icons/', blank=True, null=True)



    def __str__(self):
        return self.name


class Profile(models.Model):
    resume = models.FileField(upload_to='resumes/')



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    date_posted = models.DateField()
    

    def __str__(self):
        return self.title

class BlogReply(models.Model):
    blog = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Reply by {self.name} "

class Education(models.Model):
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.degree} at {self.university} ({self.start_year} - {self.end_year})"

