""" imports """

from profiles.models import UserProfile
from .models import Wishlist


def wishlist_list_items(request):
    """ wishlist items """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        wishlist_content = Wishlist.objects.filter(user=user)
        for item in wishlist_content:
            list_to_display.append(item.product)
    else:
        list_to_display = []
    return {
        'wishlist_items': list_to_display,
    }
