from __future__ import annotations

from typing import Annotated, Any, Literal, Union, List

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class RefundFundsReturned(BaseModel):
    """
    The refund has been credited in a payout. Thedetails[cause]will berefund_funds_returnedand thedetails[origin]will begocardless.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["refunds"]
    action: Literal["funds_returned"]
    description: str
    details: RefundFundsReturnedRefundFundsReturnedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class RefundFailed(BaseModel):
    """
    The refund did not reach your customer the funds will be returned to you. Thedetails[cause]will berefund_failedand thedetails[origin]will begocardless.It is important to note that the ‘failed' and ‘refund_settled' events are not associated. A refund can fail even after it's been settled. If a refund fails GoCardless has attempted to refund the customer and has already deducted the applicable funds from one of your payouts. The refund has then subsequently failed to reach the customer. If this occurs the funds will be returned to you.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["refunds"]
    action: Literal["failed"]
    description: str
    details: RefundFailedRefundFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class RefundPaid(BaseModel):
    """
    The refund has been paid to your customer. Thedetails[cause]will berefund_paidand thedetails[origin]will begocardless.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["refunds"]
    action: Literal["paid"]
    description: str
    details: RefundPaidRefundPaidDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class RefundCreated(BaseModel):
    """
    A refund has been created. Thedetails[cause]will bepayment_refundedand thedetails[origin]will beapi.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["refunds"]
    action: Literal["created"]
    description: str
    details: List[
        Annotated[
            Union[
                RefundCreatedPaymentRefundedDetail,
                RefundCreatedRefundCreatedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class RefundRefundSettled(BaseModel):
    """
    The refund has been deducted from a payout. Thedetails[cause]will berefund_settledand thedetails[origin]will begocardless.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["refunds"]
    action: Literal["refund_settled"]
    description: str
    details: RefundRefundSettledRefundSettledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class RefundFundsReturnedRefundFundsReturnedDetail(BaseModel):
    """
    The funds for the refund have been returned to you.
    """

    origin: Literal["gocardless"]
    cause: Literal["refund_funds_returned"]
    description: str


class RefundFailedRefundFailedDetail(BaseModel):
    """
    The refund did not reach your customer the funds will be returned to you.
    """

    origin: Literal["gocardless"]
    cause: Literal["refund_failed"]
    description: str


class RefundPaidRefundPaidDetail(BaseModel):
    """
    The refund has been paid to your customer.
    """

    origin: Literal["gocardless"]
    cause: Literal["refund_paid"]
    description: str


class RefundCreatedPaymentRefundedDetail(BaseModel):
    """
    The refund has been created and will be submitted in the next batch.
    """

    origin: Literal["api"]
    cause: Literal["payment_refunded"]
    description: str


class RefundCreatedRefundCreatedDetail(BaseModel):
    """
    The refund has been created and will be submitted in the next batch.
    """

    origin: Literal["api"]
    cause: Literal["refund_created"]
    description: str


class RefundRefundSettledRefundSettledDetail(BaseModel):
    """
    The refund has been deducted from a payout.
    """

    origin: Literal["gocardless"]
    cause: Literal["refund_settled"]
    description: str


RefundType = Annotated[
    Union[
        RefundFundsReturned,
        RefundFailed,
        RefundPaid,
        RefundCreated,
        RefundRefundSettled,
    ],
    Field(..., discriminator="action"),
]

Refund = RootModel[RefundType]
