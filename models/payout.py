"""
"payouts": [
    {
        "action": "tax_exchange_rates_confirmed",
        "description": "The tax exchange rates for all payout items of the payout have been confirmed. This event will only exist if the payout has atax_currencyand if itstax_currencyis different from itscurrency. It will be created once all fees in the payout are invoiced.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payout_tax_exchange_rates_confirmed",
                "description": "The exchange rates for the taxes (such as VAT) that applied to GoCardless fees deducted from the payout have all been confirmed and will not change."
            }
        ]
    },
    {
        "action": "fx_rate_confirmed",
        "description": "The exchange rate for the payout has been confirmed and will not change.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payout_fx_rate_confirmed",
                "description": "The exchange rate for the payout has been confirmed and will not change. Only sent for FX payouts."
            }
        ]
    },
    {
        "action": "paid",
        "description": "GoCardless has transferred the payout to the creditor's bank account. Thedetails[cause]will always bepayout_paidand thedetails[origin]will begocardless.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payout_paid",
                "description": "GoCardless has transferred the payout to the creditor's bank account. FX payouts will emit this event but will continue to have a pending status until we emit the payout_fx_rate_confirmed event."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class PayoutTaxExchangeRatesConfirmed(BaseModel):
    action: Literal["tax_exchange_rates_confirmed"]
    description: str
    details: PayoutTaxExchangeRatesConfirmedPayoutTaxExchangeRatesConfirmedDetail


class PayoutFxRateConfirmed(BaseModel):
    action: Literal["fx_rate_confirmed"]
    description: str
    details: PayoutFxRateConfirmedPayoutFxRateConfirmedDetail


class PayoutPaid(BaseModel):
    action: Literal["paid"]
    description: str
    details: PayoutPaidPayoutPaidDetail


class PayoutTaxExchangeRatesConfirmedPayoutTaxExchangeRatesConfirmedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payout_tax_exchange_rates_confirmed"]
    description: str


class PayoutFxRateConfirmedPayoutFxRateConfirmedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payout_fx_rate_confirmed"]
    description: str


class PayoutPaidPayoutPaidDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payout_paid"]
    description: str


PayoutType = Annotated[
    Union[
        PayoutTaxExchangeRatesConfirmed,
        PayoutFxRateConfirmed,
        PayoutPaid,
    ],
    Field(..., discriminator="action"),
]

Payout = RootModel[PayoutType]
