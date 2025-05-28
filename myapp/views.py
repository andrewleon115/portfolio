from django.shortcuts import render,get_object_or_404,redirect
from .models import *  # Import the About model
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings





from datetime import datetime

def index(request):
    about = About.objects.first()
    superuser = User.objects.filter(is_superuser=True).first()
    experiences = Experience.objects.all().order_by('-start_year')
    educations = Education.objects.all().order_by('-start_year')
    skill=Skill.objects.all()
    
    
    # ✅ Prefetch related images for each project
    projects = Project.objects.prefetch_related('images').all()
    blogs=BlogPost.objects.all()

    total_years = 0
    current_year = datetime.now().year

    for exp in experiences:
        try:
            start = int(exp.start_year)
            end = int(exp.end_year) if exp.end_year else current_year
            total_years += (end - start)
        except (ValueError, TypeError):
            continue  # skip if invalid data

    return render(request, 'main/port.html', {
        # 'about': about_data,
        'experiences': experiences,
        'total_experience': total_years,
        'project_list': projects,  # ✅ Use this in your template
        'about': about,
        'superuser': superuser,
        'skill' : skill,
        'blogs' : blogs,
        'educations' : educations,
    })




def project_detail(request, pk):
    project = get_object_or_404(Project.objects.prefetch_related('images', 'client_logos'), pk=pk)
    
    return render(request, 'project/project_details.html', {
        'project': project,
    })


def about_page(request):
    about = About.objects.first()
    superuser = User.objects.filter(is_superuser=True).first()
    # ✅ Prefetch related images for each project
    projects = Project.objects.prefetch_related('images').all()
    educations = Education.objects.all().order_by('-start_year')



    experiences = Experience.objects.all().order_by('-start_year')
    total_years = 0
    current_year = datetime.now().year

    for exp in experiences:
        try:
            start = int(exp.start_year)
            end = int(exp.end_year) if exp.end_year else current_year
            total_years += (end - start)
        except (ValueError, TypeError):
            continue  # skip if invalid data
    return render(request, 'about/about.html', {
        'about': about,
        'superuser': superuser,
        'projects_list': projects,
        'experiences': experiences,
        'total_experience': total_years,
        'educations' : educations,
    })



def skill_detail(request):
    mani_skill = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_year')
    total_years = 0
    current_year = datetime.now().year

    for exp in experiences:
        try:
            start = int(exp.start_year)
            end = int(exp.end_year) if exp.end_year else current_year
            total_years += (end - start)
        except (ValueError, TypeError):
            continue  # skip if invalid data
    return render(request, 'skills/skill_detail.html', {'mani_skill': mani_skill,'experiences':experiences, 'total_experience': total_years,})





def resume_view(request):
    profile = Profile.objects.first()
    if profile and profile.resume:
        return FileResponse(profile.resume.open(), content_type='application/pdf')
    raise Http404("Resume not found")

def resume_download(request):
    profile = Profile.objects.first()
    if profile and profile.resume:
        response = FileResponse(profile.resume.open(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response
    raise Http404("Resume not found")



def blog_detail(request):
    blogs = BlogPost.objects.prefetch_related('replies').order_by('-date_posted')

    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        if not blog_id:
            return HttpResponseBadRequest("Please select a blog")

        try:
            blog = BlogPost.objects.get(id=blog_id)
        except BlogPost.DoesNotExist:
            return HttpResponseBadRequest("Selected blog does not exist")

        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        message = request.POST.get('message')

        BlogReply.objects.create(
            blog=blog,
            name=name,
            email=email,
            city=city,
            message=message
        )
        return redirect('blog')

    return render(request, 'blog/blog.html', {
        'blogs': blogs
    })


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Send mail to superuser
            superuser = User.objects.filter(is_superuser=True).first()
            if superuser:
                admin_message = f"""
                New contact submission:

                Name: {name} {l_name}
                Email: {email}
                Phone: {phone}
                Subject: {subject}
                Message: {message}
                """
                send_mail(
                    subject=f"New Contact: {subject}",
                    message=admin_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[superuser.email],
                    fail_silently=False
                )

            # Acknowledgement to user
            user_message = f"""
            Hi {name},

            Thanks for contacting us!

            We’ve received your message:
            "{message}"

            We’ll get back to you as soon as possible.

            Regards,
            G.Ahimas
            """
            send_mail(
                subject='We received your message!' ,
                message=user_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )

            messages.success(request, "Your message has been sent successfully!")

        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(request, "Something went wrong while sending your message. Please try again.")

        return redirect('contact')

    return render(request, 'contact/contact.html')