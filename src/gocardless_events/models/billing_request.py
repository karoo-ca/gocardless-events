from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class BillingRequestChooseCurrency(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["choose_currency"]
    details: BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestFulfilled(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["fulfilled"]
    details: BillingRequestFulfilledBillingRequestFulfilledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestBankAuthorisationAuthorised(BaseModel):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_authorised"]
    details: BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestFlowVisited(BaseModel):
    """
    The billing request flow has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_visited"]
    details: BillingRequestFlowVisitedBillingRequestFlowVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestFailed(BaseModel):
    """
    This billing request has failed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["failed"]
    details: BillingRequestFailedBillingRequestFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestCollectBankAccount(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_bank_account"]
    details: BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestPayerDetailsConfirmed(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_details_confirmed"]
    details: (
        BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail
    )
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestCollectAmount(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_amount"]
    details: BillingRequestCollectAmountBillingRequestCollectAmountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestBankAuthorisationExpired(BaseModel):
    """
    A bank authorisation for this billing request has expired.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_expired"]
    details: BillingRequestBankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestFlowExited(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_exited"]
    details: BillingRequestFlowExitedBillingRequestFlowExitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestCollectCustomerDetails(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_customer_details"]
    details: (
        BillingRequestCollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail
    )
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestCreated(BaseModel):
    """
    This billing request has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["created"]
    details: BillingRequestCreatedBillingRequestCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestBankAuthorisationFailed(BaseModel):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_failed"]
    details: (
        BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail
    )
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestPayerGeoBlocked(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_geo_blocked"]
    details: BillingRequestPayerGeoBlockedPayerGeoBlockedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestFlowCreated(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_created"]
    details: BillingRequestFlowCreatedBillingRequestFlowCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestBankAuthorisationDenied(BaseModel):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_denied"]
    details: (
        BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail
    )
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestSelectInstitution(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["select_institution"]
    details: BillingRequestSelectInstitutionBillingRequestSelectInstitutionDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestBankAuthorisationVisited(BaseModel):
    """
    A bank authorisation link for this billing request has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_visited"]
    details: BillingRequestBankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestCancelled(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["cancelled"]
    details: BillingRequestCancelledBillingRequestCancelledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any]
    links: dict[str, Any]


class BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["api", "payer"]
    cause: Literal["billing_request_choose_currency"]
    description: str


class BillingRequestFulfilledBillingRequestFulfilledDetail(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["gocardless", "api"]
    cause: Literal["billing_request_fulfilled"]
    description: str


class BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["payer", "gocardless"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


class BillingRequestFlowVisitedBillingRequestFlowVisitedDetail(BaseModel):
    """
    The billing request flow has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_visited"]
    description: str


class BillingRequestFailedBillingRequestFailedDetail(BaseModel):
    """
    This billing request has failed.
    """

    origin: Literal["gocardless", "api"]
    cause: Literal["billing_request_failed"]
    description: str


class BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["api", "payer"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


class BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail(
    BaseModel
):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["api", "payer"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


class BillingRequestCollectAmountBillingRequestCollectAmountDetail(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_amount"]
    description: str


class BillingRequestBankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has expired.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_expired"]
    description: str


class BillingRequestFlowExitedBillingRequestFlowExitedDetail(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_exited"]
    description: str


class BillingRequestCollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail(
    BaseModel
):
    """
    Customer details have been collected for this billing request.
    """

    origin: Literal["api", "payer"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


class BillingRequestCreatedBillingRequestCreatedDetail(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["gocardless", "api", "payer"]
    cause: Literal["billing_request_created"]
    description: str


class BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["payer", "gocardless"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


class BillingRequestPayerGeoBlockedPayerGeoBlockedDetail(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    origin: Literal["payer"]
    cause: Literal["payer_geo_blocked"]
    description: str


class BillingRequestFlowCreatedBillingRequestFlowCreatedDetail(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["gocardless", "api", "payer"]
    cause: Literal["billing_request_flow_created"]
    description: str


class BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["payer", "gocardless"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


class BillingRequestSelectInstitutionBillingRequestSelectInstitutionDetail(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_select_institution"]
    description: str


class BillingRequestBankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail(
    BaseModel
):
    """
    A bank authorisation link for this billing request has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_visited"]
    description: str


class BillingRequestCancelledBillingRequestCancelledDetail(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    origin: Literal["gocardless", "api"]
    cause: Literal["billing_request_cancelled"]
    description: str


BillingRequestType = Annotated[
    BillingRequestChooseCurrency
    | BillingRequestFulfilled
    | BillingRequestBankAuthorisationAuthorised
    | BillingRequestFlowVisited
    | BillingRequestFailed
    | BillingRequestCollectBankAccount
    | BillingRequestPayerDetailsConfirmed
    | BillingRequestCollectAmount
    | BillingRequestBankAuthorisationExpired
    | BillingRequestFlowExited
    | BillingRequestCollectCustomerDetails
    | BillingRequestCreated
    | BillingRequestBankAuthorisationFailed
    | BillingRequestPayerGeoBlocked
    | BillingRequestFlowCreated
    | BillingRequestBankAuthorisationDenied
    | BillingRequestSelectInstitution
    | BillingRequestBankAuthorisationVisited
    | BillingRequestCancelled,
    Field(..., discriminator="action"),
]

BillingRequest = RootModel[BillingRequestType]
