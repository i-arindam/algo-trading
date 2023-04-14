from django.db import models
from .instruments import Instrument


class OhlcDataDaily(models.Model):
    # REFACTOR: Create a custom field for `DecimalField`for capturing all price fields from Trading API

    # Deliberately calling the timestamp column by a simplified name `date` as most trading APIs have
    # date as the indicating column
    date = models.DateTimeField("trade time")
    open = models.DecimalField("open price", max_digits=15, decimal_places=5)
    high = models.DecimalField("high price", max_digits=15, decimal_places=5)
    low = models.DecimalField("low price", max_digits=15, decimal_places=5)
    close = models.DecimalField("close price", max_digits=15, decimal_places=5)

    # Set default for now, until we get this from zerodha APIs
    last_price = models.DecimalField("last price", max_digits=15, decimal_places=5, default=0.0)

    # Refers to the instrument to which this daily data set belongs to.
    # Renames the related_name on `instrument` as `daily_data`, resulting in the following methods:
    # ```
    # instrument.daily_data.count(), instrument.daily_data.filter()
    # instrument.daily_data.add()
    # instrument.daily_data.create()
    # instrument.daily_data.remove()
    # instrument.daily_data.clear()
    # instrument.daily_data.set()
    # ```
    instrument = models.ForeignKey(
        Instrument,
        on_delete=models.CASCADE,
        related_name="daily_data",
    )

    class Meta:
        verbose_name = "OhlcDataDaily"
        verbose_name_plural = "OhlcDataDailies"

        indexes = [
            models.Index(fields=['date'], name="ohlcv_daily_date_idx"),
            models.Index(fields=['instrument', 'date'], name="ohlcv_dly_instrument_date_idx"),
        ]

        constraints = [
            # Each day/date-time will have many entries for different instruments, but for each
            # instrument the day/date-time should be unique and referring to the _source of truth_
            # for that timestamp.
            models.UniqueConstraint(
                fields=['instrument', 'date'],
                name="unique_instrument_ohlcv_data_daily_date",
                violation_error_message="Date for instrument already exists, must be unique",
            )
        ]

        get_latest_by = "date"  # should it be -date?, check when we have data

    def __str__(self):
        return str(self.date)

    # TODO: Define custom methods here

    @property
    def date_in_tables(self) -> str:
        """Return date in Month Day, Year format for display in tables

        Parameters
        ----------
        self:
            The object instance

        Returns
        -------
        str
            Date in April 01, 1990 format
        """
        return self.date.strftime("%B %d, %Y")
