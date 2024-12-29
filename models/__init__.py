from typing import Annotated

from pydantic import Field, RootModel

from models.billing_request import BillingRequest
from models.creditor import Creditor
from models.export import Export
from models.instalment_schedule import InstalmentSchedule
from models.mandate import Mandate
from models.payer_authorization import PayerAuthorization
from models.payment import Payment
from models.payout import Payout
from models.refund import Refund
from models.scheme_identifier import SchemeIdentifier
from models.subscription import Subscription

EventType = Annotated[
    SchemeIdentifier
    | PayerAuthorization
    | Payment
    | Creditor
    | Mandate
    | Subscription
    | BillingRequest
    | Export
    | InstalmentSchedule
    | Refund
    | Payout,
    Field(..., discriminator="resource_type"),
]

Event = RootModel[EventType]

__all__ = [
    "BillingRequest",
    "Creditor",
    "Event",
    "Export",
    "InstalmentSchedule",
    "Mandate",
    "PayerAuthorization",
    "Payment",
    "Payout",
    "Refund",
    "SchemeIdentifier",
    "Subscription",
]
