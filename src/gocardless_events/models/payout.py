from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class PayoutTaxExchangeRatesConfirmed(BaseModel):
    """
    The tax exchange rates for all payout items of the payout have been confirmed. This event will only exist if the payout has atax_currencyand if itstax_currencyis different from itscurrency. It will be created once all fees in the payout are invoiced.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payouts"]
    action: Literal["tax_exchange_rates_confirmed"]
    description: str
    details: PayoutTaxExchangeRatesConfirmedPayoutTaxExchangeRatesConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class PayoutFxRateConfirmed(BaseModel):
    """
    The exchange rate for the payout has been confirmed and will not change.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payouts"]
    action: Literal["fx_rate_confirmed"]
    description: str
    details: PayoutFxRateConfirmedPayoutFxRateConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class PayoutPaid(BaseModel):
    """
    GoCardless has transferred the payout to the creditor's bank account. Thedetails[cause]will always bepayout_paidand thedetails[origin]will begocardless.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payouts"]
    action: Literal["paid"]
    description: str
    details: PayoutPaidPayoutPaidDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class PayoutTaxExchangeRatesConfirmedPayoutTaxExchangeRatesConfirmedDetail(BaseModel):
    """
    The exchange rates for the taxes (such as VAT) that applied to GoCardless fees deducted from the payout have all been confirmed and will not change.
    """

    origin: Literal["gocardless"]
    cause: Literal["payout_tax_exchange_rates_confirmed"]
    description: str


class PayoutFxRateConfirmedPayoutFxRateConfirmedDetail(BaseModel):
    """
    The exchange rate for the payout has been confirmed and will not change. Only sent for FX payouts.
    """

    origin: Literal["gocardless"]
    cause: Literal["payout_fx_rate_confirmed"]
    description: str


class PayoutPaidPayoutPaidDetail(BaseModel):
    """
    GoCardless has transferred the payout to the creditor's bank account. FX payouts will emit this event but will continue to have a pending status until we emit the payout_fx_rate_confirmed event.
    """

    origin: Literal["gocardless"]
    cause: Literal["payout_paid"]
    description: str


PayoutType = Annotated[
    PayoutTaxExchangeRatesConfirmed | PayoutFxRateConfirmed | PayoutPaid,
    Field(..., discriminator="action"),
]

Payout = RootModel[PayoutType]
