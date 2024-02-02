from django.shortcuts import render, get_object_or_404
from end_user.models import EndUser
from django.contrib.auth.decorators import login_required

# add conditional to check if its the right user 
@login_required
def customer_index(request):

    end_user = get_object_or_404(
        EndUser,
    )

    content_list = end_user.content.all()

    context = {
        "page_name": "Customer Index",
        "end_user": end_user,
        "content_list": content_list,
    }

    
    return render(request, "customer.html", context)
