from django import template
from portretten.models import Basisgegevens

register = template.Library()


@register.inclusion_tag('portretten/tooltip.html')
def get_tooltip(object_id):
    object = Basisgegevens.objects.get(id=object_id)
    tooltip = {
        'Persoon': object.persoon,
        'Alternatieve naam': object.alt_naam,
        'Bijnaam': object.bijnaam,
        'Titel': object.titel,
        'Beroep specifiek': object.beroep_specifiek,
        'Geboren': object.geboortedatum,
        'Overleden': object.sterfdatum,
        'Kunstenaar': object.kunstenaar,
        'Inventarisnummer': object.nummer,
    }
    return { 'tooltip': tooltip }


@register.inclusion_tag('portretten/modal_description.html')
def get_description(object_id):
    object = Basisgegevens.objects.get(id=object_id)
    description = {
        'Persoon': object.persoon,
    }
    return { 'description': description }
