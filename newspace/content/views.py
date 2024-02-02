from django.shortcuts import render, get_object_or_404
from content.models import Content 
from django.contrib.auth.decorators import login_required

# add conditional to check if its the right user 
@login_required
def serve_content(request, id):

    content = get_object_or_404(
        Content, 
        id=id,
    )

    context = {
        "page_name": "Content",
        "content" : content,
    }

    return render(request, "content.html", context)


def index(request):

    return render(request, "index.html")


def about(request):

    return render(request, "about.html")

