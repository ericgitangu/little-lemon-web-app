from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


def home(request):
    """
    Renders the home page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered index.html template.
    """
    return render(request, 'index.html')


def about(request):
    """
    Renders the about page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered about.html template.
    """
    return render(request, 'about.html')


def book(request):
    """
    View function for booking a table.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    """
    This function handles the menu view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the menu data.
    """
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    """
    Display a menu item based on the given primary key (pk).

    Args:
        request: The HTTP request object.
        pk (int, optional): The primary key of the menu item to display.

    Returns:
        A rendered HTML template with the menu item information.

    """
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})
