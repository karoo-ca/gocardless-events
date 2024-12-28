"""
"creditors": [
    {
        "action": "account_auto_frozen",
        "description": "This creditor account has been automatically frozen and had restrictions applied.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "account_auto_frozen",
                "description": "This creditor account has been automatically frozen and had restrictions applied."
            }
        ]
    },
    {
        "action": "updated",
        "description": "Something has changed about this creditor. The property that has changed will be included in the event details. Currently this webhook is sent forlogo_urlverification_statusmandate_imports_enabledcustom_payment_pages_enabledandmerchant_responsible_for_notifications.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "creditor_updated",
                "description": "This creditor has been updated."
            }
        ]
    },
    {
        "action": "account_auto_frozen_reverted",
        "description": "This creditor accounts restrictions have been removed.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "account_auto_frozen_reverted",
                "description": "The restrictions on this creditor account have been removed."
            }
        ]
    },
    {
        "action": "bounced_payout",
        "description": "A payout for this creditor has failed. Please contact your bank for more information or retry the payout.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "bounced_payout",
                "description": "A payout for this creditor has failed. Please retry the payout or contact your bank for more information."
            }
        ]
    },
    {
        "action": "new_payout_currency_added",
        "description": "This creditor has added a new payout currency.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "new_payout_currency_added",
                "description": "This creditor has added a new payout currency."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class CreditorAccountAutoFrozen(BaseModel):
    action: Literal["account_auto_frozen"]
    description: str
    details: CreditorAccountAutoFrozenAccountAutoFrozenDetail


class CreditorUpdated(BaseModel):
    action: Literal["updated"]
    description: str
    details: CreditorUpdatedCreditorUpdatedDetail


class CreditorAccountAutoFrozenReverted(BaseModel):
    action: Literal["account_auto_frozen_reverted"]
    description: str
    details: CreditorAccountAutoFrozenRevertedAccountAutoFrozenRevertedDetail


class CreditorBouncedPayout(BaseModel):
    action: Literal["bounced_payout"]
    description: str
    details: CreditorBouncedPayoutBouncedPayoutDetail


class CreditorNewPayoutCurrencyAdded(BaseModel):
    action: Literal["new_payout_currency_added"]
    description: str
    details: CreditorNewPayoutCurrencyAddedNewPayoutCurrencyAddedDetail


class CreditorAccountAutoFrozenAccountAutoFrozenDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["account_auto_frozen"]
    description: str


class CreditorUpdatedCreditorUpdatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["creditor_updated"]
    description: str


class CreditorAccountAutoFrozenRevertedAccountAutoFrozenRevertedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["account_auto_frozen_reverted"]
    description: str


class CreditorBouncedPayoutBouncedPayoutDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["bounced_payout"]
    description: str


class CreditorNewPayoutCurrencyAddedNewPayoutCurrencyAddedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["new_payout_currency_added"]
    description: str


CreditorType = Annotated[
    Union[
        CreditorAccountAutoFrozen,
        CreditorUpdated,
        CreditorAccountAutoFrozenReverted,
        CreditorBouncedPayout,
        CreditorNewPayoutCurrencyAdded,
    ],
    Field(..., discriminator="action"),
]

Creditor = RootModel[CreditorType]
