from django.shortcuts import render,redirect

from .models import JobApplication 
from .models import JobListing

def index(request):
    return render(request, 'index.html')

def job_listings(request):
    job_listings = JobListing.objects.all()
    context = {
        'job_listings': job_listings
    }
    return render(request, 'job_listings.html', context)

def apply_job(request, job_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']
        cover_letter = request.POST['cover_letter']

        # Create a new JobApplication object and save it to the database
        job_application = JobApplication.objects.create(
            job_id=job_id,
            name=name,
            email=email,
            resume=resume,
            cover_letter=cover_letter
        )

        # After saving, you can redirect the user to a success page or back to the job listings
        return redirect('job_listings')

    # Get the job details based on job_id (you need to implement this)
    # job = JobListing.objects.get(id=job_id)

    context = {
        # Pass the job details to the template
        # 'job': job,
    }
    return render(request, 'apply_job.html', context)





