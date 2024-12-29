from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class BillingRequestChooseCurrency(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    action: Literal["choose_currency"]
    description: str
    details: BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail


class BillingRequestFulfilled(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    action: Literal["fulfilled"]
    description: str
    details: BillingRequestFulfilledBillingRequestFulfilledDetail


class BillingRequestBankAuthorisationAuthorised(BaseModel):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    action: Literal["bank_authorisation_authorised"]
    description: str
    details: BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail


class BillingRequestFlowVisited(BaseModel):
    """
    The billing request flow has been visited.
    """

    action: Literal["flow_visited"]
    description: str
    details: BillingRequestFlowVisitedBillingRequestFlowVisitedDetail


class BillingRequestFailed(BaseModel):
    """
    This billing request has failed.
    """

    action: Literal["failed"]
    description: str
    details: BillingRequestFailedBillingRequestFailedDetail


class BillingRequestCollectBankAccount(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    action: Literal["collect_bank_account"]
    description: str
    details: BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail


class BillingRequestPayerDetailsConfirmed(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    action: Literal["payer_details_confirmed"]
    description: str
    details: (
        BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail
    )


class BillingRequestCollectAmount(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    action: Literal["collect_amount"]
    description: str
    details: BillingRequestCollectAmountBillingRequestCollectAmountDetail


class BillingRequestBankAuthorisationExpired(BaseModel):
    """
    A bank authorisation for this billing request has expired.
    """

    action: Literal["bank_authorisation_expired"]
    description: str
    details: BillingRequestBankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail


class BillingRequestFlowExited(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    action: Literal["flow_exited"]
    description: str
    details: BillingRequestFlowExitedBillingRequestFlowExitedDetail


class BillingRequestCollectCustomerDetails(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    action: Literal["collect_customer_details"]
    description: str
    details: (
        BillingRequestCollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail
    )


class BillingRequestCreated(BaseModel):
    """
    This billing request has been created.
    """

    action: Literal["created"]
    description: str
    details: BillingRequestCreatedBillingRequestCreatedDetail


class BillingRequestBankAuthorisationFailed(BaseModel):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    action: Literal["bank_authorisation_failed"]
    description: str
    details: (
        BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail
    )


class BillingRequestPayerGeoBlocked(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    action: Literal["payer_geo_blocked"]
    description: str
    details: BillingRequestPayerGeoBlockedPayerGeoBlockedDetail


class BillingRequestFlowCreated(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    action: Literal["flow_created"]
    description: str
    details: BillingRequestFlowCreatedBillingRequestFlowCreatedDetail


class BillingRequestBankAuthorisationDenied(BaseModel):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    action: Literal["bank_authorisation_denied"]
    description: str
    details: (
        BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail
    )


class BillingRequestSelectInstitution(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    action: Literal["select_institution"]
    description: str
    details: BillingRequestSelectInstitutionBillingRequestSelectInstitutionDetail


class BillingRequestBankAuthorisationVisited(BaseModel):
    """
    A bank authorisation link for this billing request has been visited.
    """

    action: Literal["bank_authorisation_visited"]
    description: str
    details: BillingRequestBankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail


class BillingRequestCancelled(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    action: Literal["cancelled"]
    description: str
    details: BillingRequestCancelledBillingRequestCancelledDetail


class BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_choose_currency"]
    description: str


class BillingRequestFulfilledBillingRequestFulfilledDetail(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_fulfilled"]
    description: str


class BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["payer"]
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

    origin: Literal["gocardless"]
    cause: Literal["billing_request_failed"]
    description: str


class BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


class BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail(
    BaseModel
):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["api"]
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

    origin: Literal["api"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


class BillingRequestCreatedBillingRequestCreatedDetail(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_created"]
    description: str


class BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["payer"]
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

    origin: Literal["gocardless"]
    cause: Literal["billing_request_flow_created"]
    description: str


class BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["payer"]
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

    origin: Literal["gocardless"]
    cause: Literal["billing_request_cancelled"]
    description: str


BillingRequestType = Annotated[
    Union[
        BillingRequestChooseCurrency,
        BillingRequestFulfilled,
        BillingRequestBankAuthorisationAuthorised,
        BillingRequestFlowVisited,
        BillingRequestFailed,
        BillingRequestCollectBankAccount,
        BillingRequestPayerDetailsConfirmed,
        BillingRequestCollectAmount,
        BillingRequestBankAuthorisationExpired,
        BillingRequestFlowExited,
        BillingRequestCollectCustomerDetails,
        BillingRequestCreated,
        BillingRequestBankAuthorisationFailed,
        BillingRequestPayerGeoBlocked,
        BillingRequestFlowCreated,
        BillingRequestBankAuthorisationDenied,
        BillingRequestSelectInstitution,
        BillingRequestBankAuthorisationVisited,
        BillingRequestCancelled,
    ],
    Field(..., discriminator="action"),
]

BillingRequest = RootModel[BillingRequestType]
