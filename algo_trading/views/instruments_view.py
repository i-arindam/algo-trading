# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from ..models.instruments import Instrument

from ..forms.instruments.add_instrument_form import AddInstrumentForm


@require_http_methods(["GET"])
def instrument_by_pk(request, pk: int):
    """Show an `Instrument` instance identified by its primary key: `pk`"""

    instrument = get_object_or_404(Instrument, pk=pk)
    return display_instrument(
        request,
        instrument
    )


@require_http_methods(["GET"])
def instrument_by_symbol(request, symbol: str):
    """Show an `Instrument` instance identified by its `symbol`"""

    instrument = Instrument.objects.get_by_symbol(symbol)
    return display_instrument(
        request,
        instrument
    )


def display_instrument(request, instrument: Instrument):
    """Common function to show an `Instrument`"""

    return render(
        request,
        'instruments/show.html',
        {
            'instrument': instrument,
            'daily_data': instrument.daily_data.order_by("-date"),
        },
    )


@require_http_methods(["GET", "POST"])
def add_instruments(request):
    """Add one or more instruments into the system

    Tries to create a new instrument from the form data.

    Internal function for the view, not to be called from outside.
    Processes the symbol through the yfinance API to collect basic info about the stock
    and creates a new Instrument instance from that info
    For the newly created Instrument, downloads all historical data till date and creates
    a record of type `OhlcvDataDaily` for every available date in the historical data with their
    OHLC entries.

    Parameters
    ----------
    request:
        The request object

    Raises
    ------
    Does not raise any error, but shows all failing symbols on the resulting page table
    Also shows the successfully imported symbols on the resulting page table
    """

    symbols_import_summary = {}
    if request.method == 'POST':
        form = AddInstrumentForm(request.POST)

        if form.is_valid():
            symbols = [s.strip() for s in form.cleaned_data['symbol'].split(",")]
            symbols_import_summary = Instrument.objects.import_symbols_from_yf(symbols)

    else:
        form = AddInstrumentForm()

    return render(
        request,
        'instruments/add_instrument.html',
        {
            'form': form,
            'symbols_import_summary': symbols_import_summary
        }
    )


@require_http_methods(["GET"])
def list_instruments(request):
    instruments = Instrument.objects.all()

    return render(
        request,
        'instruments/list_instruments.html',
        {
            'instruments': instruments,
        }
    )
