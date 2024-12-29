from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class ChooseCurrencyBillingRequestChooseCurrencyApiDetail(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_choose_currency"]
    description: str


class ChooseCurrencyBillingRequestChooseCurrencyPayerDetail(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_choose_currency"]
    description: str


ChooseCurrencyBillingRequestChooseCurrencyDetail = Annotated[
    ChooseCurrencyBillingRequestChooseCurrencyApiDetail
    | ChooseCurrencyBillingRequestChooseCurrencyPayerDetail,
    Field(..., discriminator="origin"),
]


class FulfilledBillingRequestFulfilledGocardlessDetail(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_fulfilled"]
    description: str


class FulfilledBillingRequestFulfilledApiDetail(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_fulfilled"]
    description: str


FulfilledBillingRequestFulfilledDetail = Annotated[
    FulfilledBillingRequestFulfilledGocardlessDetail
    | FulfilledBillingRequestFulfilledApiDetail,
    Field(..., discriminator="origin"),
]


class BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedPayerDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


class BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedGocardlessDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail = Annotated[
    BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedPayerDetail
    | BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedGocardlessDetail,
    Field(..., discriminator="origin"),
]


class FlowVisitedBillingRequestFlowVisitedPayerDetail(BaseModel):
    """
    The billing request flow has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_visited"]
    description: str


FlowVisitedBillingRequestFlowVisitedDetail = (
    FlowVisitedBillingRequestFlowVisitedPayerDetail
)


class FailedBillingRequestFailedGocardlessDetail(BaseModel):
    """
    This billing request has failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_failed"]
    description: str


class FailedBillingRequestFailedApiDetail(BaseModel):
    """
    This billing request has failed.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_failed"]
    description: str


FailedBillingRequestFailedDetail = Annotated[
    FailedBillingRequestFailedGocardlessDetail | FailedBillingRequestFailedApiDetail,
    Field(..., discriminator="origin"),
]


class CollectBankAccountBillingRequestCollectBankAccountApiDetail(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


class CollectBankAccountBillingRequestCollectBankAccountPayerDetail(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


CollectBankAccountBillingRequestCollectBankAccountDetail = Annotated[
    CollectBankAccountBillingRequestCollectBankAccountApiDetail
    | CollectBankAccountBillingRequestCollectBankAccountPayerDetail,
    Field(..., discriminator="origin"),
]


class PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedApiDetail(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


class PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedPayerDetail(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail = Annotated[
    PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedApiDetail
    | PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedPayerDetail,
    Field(..., discriminator="origin"),
]


class CollectAmountBillingRequestCollectAmountPayerDetail(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_amount"]
    description: str


CollectAmountBillingRequestCollectAmountDetail = (
    CollectAmountBillingRequestCollectAmountPayerDetail
)


class BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredPayerDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has expired.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_expired"]
    description: str


BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail = (
    BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredPayerDetail
)


class FlowExitedBillingRequestFlowExitedPayerDetail(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_exited"]
    description: str


FlowExitedBillingRequestFlowExitedDetail = FlowExitedBillingRequestFlowExitedPayerDetail


class CollectCustomerDetailsBillingRequestCollectCustomerDetailsApiDetail(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


class CollectCustomerDetailsBillingRequestCollectCustomerDetailsPayerDetail(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail = Annotated[
    CollectCustomerDetailsBillingRequestCollectCustomerDetailsApiDetail
    | CollectCustomerDetailsBillingRequestCollectCustomerDetailsPayerDetail,
    Field(..., discriminator="origin"),
]


class CreatedBillingRequestCreatedGocardlessDetail(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_created"]
    description: str


class CreatedBillingRequestCreatedApiDetail(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_created"]
    description: str


class CreatedBillingRequestCreatedPayerDetail(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_created"]
    description: str


CreatedBillingRequestCreatedDetail = Annotated[
    CreatedBillingRequestCreatedGocardlessDetail
    | CreatedBillingRequestCreatedApiDetail
    | CreatedBillingRequestCreatedPayerDetail,
    Field(..., discriminator="origin"),
]


class BankAuthorisationFailedBillingRequestBankAuthorisationFailedPayerDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


class BankAuthorisationFailedBillingRequestBankAuthorisationFailedGocardlessDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail = Annotated[
    BankAuthorisationFailedBillingRequestBankAuthorisationFailedPayerDetail
    | BankAuthorisationFailedBillingRequestBankAuthorisationFailedGocardlessDetail,
    Field(..., discriminator="origin"),
]


class PayerGeoBlockedPayerGeoBlockedPayerDetail(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    origin: Literal["payer"]
    cause: Literal["payer_geo_blocked"]
    description: str


PayerGeoBlockedPayerGeoBlockedDetail = PayerGeoBlockedPayerGeoBlockedPayerDetail


class FlowCreatedBillingRequestFlowCreatedGocardlessDetail(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_flow_created"]
    description: str


class FlowCreatedBillingRequestFlowCreatedApiDetail(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_flow_created"]
    description: str


class FlowCreatedBillingRequestFlowCreatedPayerDetail(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_created"]
    description: str


FlowCreatedBillingRequestFlowCreatedDetail = Annotated[
    FlowCreatedBillingRequestFlowCreatedGocardlessDetail
    | FlowCreatedBillingRequestFlowCreatedApiDetail
    | FlowCreatedBillingRequestFlowCreatedPayerDetail,
    Field(..., discriminator="origin"),
]


class BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedPayerDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


class BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedGocardlessDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail = Annotated[
    BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedPayerDetail
    | BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedGocardlessDetail,
    Field(..., discriminator="origin"),
]


class SelectInstitutionBillingRequestSelectInstitutionPayerDetail(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_select_institution"]
    description: str


SelectInstitutionBillingRequestSelectInstitutionDetail = (
    SelectInstitutionBillingRequestSelectInstitutionPayerDetail
)


class BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedPayerDetail(
    BaseModel
):
    """
    A bank authorisation link for this billing request has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_visited"]
    description: str


BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail = (
    BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedPayerDetail
)


class CancelledBillingRequestCancelledGocardlessDetail(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_cancelled"]
    description: str


class CancelledBillingRequestCancelledApiDetail(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_cancelled"]
    description: str


CancelledBillingRequestCancelledDetail = Annotated[
    CancelledBillingRequestCancelledGocardlessDetail
    | CancelledBillingRequestCancelledApiDetail,
    Field(..., discriminator="origin"),
]


class BillingRequestChooseCurrency(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["choose_currency"]
    details: ChooseCurrencyBillingRequestChooseCurrencyDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFulfilled(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["fulfilled"]
    details: FulfilledBillingRequestFulfilledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationAuthorised(BaseModel):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_authorised"]
    details: BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowVisited(BaseModel):
    """
    The billing request flow has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_visited"]
    details: FlowVisitedBillingRequestFlowVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFailed(BaseModel):
    """
    This billing request has failed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["failed"]
    details: FailedBillingRequestFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectBankAccount(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_bank_account"]
    details: CollectBankAccountBillingRequestCollectBankAccountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestPayerDetailsConfirmed(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_details_confirmed"]
    details: PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectAmount(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_amount"]
    details: CollectAmountBillingRequestCollectAmountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationExpired(BaseModel):
    """
    A bank authorisation for this billing request has expired.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_expired"]
    details: BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowExited(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_exited"]
    details: FlowExitedBillingRequestFlowExitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectCustomerDetails(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_customer_details"]
    details: CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCreated(BaseModel):
    """
    This billing request has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["created"]
    details: CreatedBillingRequestCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationFailed(BaseModel):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_failed"]
    details: BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestPayerGeoBlocked(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_geo_blocked"]
    details: PayerGeoBlockedPayerGeoBlockedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowCreated(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_created"]
    details: FlowCreatedBillingRequestFlowCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationDenied(BaseModel):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_denied"]
    details: BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestSelectInstitution(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["select_institution"]
    details: SelectInstitutionBillingRequestSelectInstitutionDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationVisited(BaseModel):
    """
    A bank authorisation link for this billing request has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_visited"]
    details: BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCancelled(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["cancelled"]
    details: CancelledBillingRequestCancelledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


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
