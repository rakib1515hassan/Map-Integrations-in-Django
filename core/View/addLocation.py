from core.models import School
from django.views import generic
from core.forms import SchoolForm

import folium
from django.urls import reverse_lazy
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


class SchoolCreateView(generic.CreateView):
    model = School
    form_class = SchoolForm
    template_name = 'schoolAdd.html'
    success_url = reverse_lazy('school_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initialize the map with center coordinates
        initial_latitude = 23.810331
        initial_longitude = 90.412521
        m = folium.Map(
            location=[initial_latitude, initial_longitude],
            zoom_start=4,
        )

        # Add a JavaScript function to handle map click event
        m.add_child(folium.ClickForMarker(popup="Selected Location"))
        context["map"] = m._repr_html_()
        return context
    
    # def form_invalid(self, form):
    #     field_errors = {field.name: field.errors for field in form}
    #     has_errors = any(field_errors.values())

    #     # print("----------------------")
    #     # print("Error = ", field_errors)
    #     # print("----------------------")

    #     return self.render_to_response(self.get_context_data(
    #         form=form, 
    #         field_errors=field_errors, 
    #         has_errors=has_errors
    #         ))