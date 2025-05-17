from django.shortcuts import render,redirect
from . models import *
from user.models import *
from datetime import datetime
# Create your views here.
def admin_login(request):
    return render(request,"admin_index.html")

# Create your views here.
def admin_home(request):
    return render(request,"admin_home.html")

def admin_view_guide(request):
    guides = TourGuide.objects.all()
    print(guides)
    return render(request,"admin_view_guide.html",{'guides': guides})

def admin_view_user(request):
    user = USER_DB.objects.all()
    return render(request,"admin_view_user.html",{'user': user})

def admin_view_pack(request):
    data = Trip.objects.all()
    print(data)
    return render(request,"admin_view_pack.html",{'data': data})

def admin_login_btn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username=="admin" and   password=="admin"):
            return redirect("admin_home")

    return render(request,"admin_index.html")


def admin_add_guide(request):
    if request.method == 'POST':
        namev = request.POST.get('name')
        passwordv = request.POST.get('password')
        biov =  request.POST.get('bio')
        languagesv =  request.POST.get('languages')
        years_experiencev =  request.POST.get('years_experience')
        contact_numberv =  request.POST.get('contact_number')
        is_availablev = request.POST.get('is_available')
        is_availabled=True
        print(is_availablev)
        if is_availablev=="Available":
            is_availabled=True
        else:is_availabled=False
        try:
            # Create and save user
            user = TourGuide(
                name = namev,
                password = passwordv,
                bio =  biov,
                languages =  languagesv,
                years_experience = years_experiencev,
                contact_number = contact_numberv,
                is_available = is_availabled
            )
            user.save()
            
            return redirect('admin_view_guide')  # Replace with your login URL name
            
        except Exception as e:
            return redirect('admin_view_guide')


    return redirect('admin_view_guide')

def admin_delete_guide(request, id):
    try:
        # Get the guide using objects.get()
        guide = TourGuide.objects.get(id=id)
        
        # Delete the guide
        guide.delete()
        
        # Add success message
    
    except TourGuide.DoesNotExist:
        # Handle case where guide doesn't exist
        # messages.error(request, 'Guide not found!')
        return redirect('admin_view_guide')
    
    except Exception as e:
        # Handle any other exceptions
        # messages.error(request, f'Error deleting guide: {str(e)}')
        return redirect('admin_view_guide')
    
    return redirect('admin_view_guide')

def admin_delete_trip(request, id):
    try:
        # Get the guide using objects.get()
        obj = Trip.objects.get(id=id)
        
        obj.delete()
        
    
    except TourGuide.DoesNotExist:
        # Handle case where guide doesn't exist
        # messages.error(request, 'Guide not found!')
        return redirect('admin_view_pack')
    
    except Exception as e:
        # Handle any other exceptions
        # messages.error(request, f'Error deleting guide: {str(e)}')
        return redirect('admin_view_pack')
    
    return redirect('admin_view_pack')

def admin_delete_user(request, id):
    try:
        # Get the guide using objects.get()
        guide = USER_DB.objects.get(id=id)
        
        # Delete the guide
        guide.delete()
        
        # Add success message
    
    except TourGuide.DoesNotExist:
        # Handle case where guide doesn't exist
        # messages.error(request, 'Guide not found!')
        return redirect('admin_view_user')
    
    except Exception as e:
        # Handle any other exceptions
        # messages.error(request, f'Error deleting guide: {str(e)}')
        return redirect('admin_view_user')
    
    return redirect('admin_view_user')


def admin_add_trip(request):
    if request.method == 'POST' :
        try:
            # Get form data
            name = request.POST.get('name')
            location = request.POST.get('location')
            duration = int(request.POST.get('duration'))
            price = float(request.POST.get('price'))
            discount = float(request.POST.get('discount'))
            capacity = int(request.POST.get('capacity'))
            available_seats = int(request.POST.get('available_seats'))
            difficulty = request.POST.get('difficulty')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            trip_type = request.POST.get('trip_type')
            short_description = request.POST.get('short_description')
            description = request.POST.get('description')
            is_active = True  # Default to active
            
            # Convert string dates to date objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            
            # Handle file upload
            image = request.FILES.get('image')
         
            da = Trip(name = name,
                description = description,
                short_description = short_description,
                location = location,
                trip_type = trip_type,
                duration = duration,
                price = price,
                discount = discount,
                capacity = capacity,
                available_seats = available_seats,
                difficulty = difficulty,
                start_date =start_date,
                end_date = end_date,
                is_active = is_active,
                image = image
             )
            da.save()
            return redirect('admin_view_pack')
        except Exception as e:
            # messages.error(request, f"Error adding trip: {str(e)}")
            return redirect('admin_view_pack')
    
    return redirect('admin_view_pack')