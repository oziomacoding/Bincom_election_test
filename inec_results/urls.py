from django.urls import path
from . import views
from .views import PollingUnitResultsView, SummedLGAResultsView, NewPollingUnitResultsView



urlpatterns = [
    path("polling-unit-results/<int:polling_unit_uniqueid>/", PollingUnitResultsView.as_view(), name="polling_unit_results"),
    path("lga-summed-results/<int:lga_id>/", SummedLGAResultsView.as_view(), name="lga_summed_results"),
    path("new-polling-unit-results/", NewPollingUnitResultsView.as_view(), name="new_polling_unit_results"),

]

# ]