"""
"billing_requests": [
    {
        "action": "choose_currency",
        "description": "Currency details have been collected for this billing request.",
        "details": [
            {
                "origin": "api",
                "cause": "billing_request_choose_currency",
                "description": "Currency details have been collected for this billing request."
            },
            {
                "origin": "payer",
                "cause": "billing_request_choose_currency",
                "description": "Currency details have been collected for this billing request."
            }
        ]
    },
    {
        "action": "fulfilled",
        "description": "This billing request has been fulfilled and the resources have been created.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "billing_request_fulfilled",
                "description": "This billing request has been fulfilled and the resources have been created."
            },
            {
                "origin": "api",
                "cause": "billing_request_fulfilled",
                "description": "This billing request has been fulfilled and the resources have been created."
            }
        ]
    },
    {
        "action": "bank_authorisation_authorised",
        "description": "A bank authorisation for this billing request has been authorised by the payer.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_bank_authorisation_authorised",
                "description": "A bank authorisation for this billing request has been authorised by the payer."
            },
            {
                "origin": "gocardless",
                "cause": "billing_request_bank_authorisation_authorised",
                "description": "A bank authorisation for this billing request has been authorised by the payer."
            }
        ]
    },
    {
        "action": "flow_visited",
        "description": "The billing request flow has been visited.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_flow_visited",
                "description": "The billing request flow has been visited."
            }
        ]
    },
    {
        "action": "failed",
        "description": "This billing request has failed.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "billing_request_failed",
                "description": "This billing request has failed."
            },
            {
                "origin": "api",
                "cause": "billing_request_failed",
                "description": "This billing request has failed."
            }
        ]
    },
    {
        "action": "collect_bank_account",
        "description": "Bank account details have been collected for this billing request.",
        "details": [
            {
                "origin": "api",
                "cause": "billing_request_collect_bank_account",
                "description": "Bank account details have been collected for this billing request."
            },
            {
                "origin": "payer",
                "cause": "billing_request_collect_bank_account",
                "description": "Bank account details have been collected for this billing request."
            }
        ]
    },
    {
        "action": "payer_details_confirmed",
        "description": "Payer has confirmed all their details for this billing request.",
        "details": [
            {
                "origin": "api",
                "cause": "billing_request_payer_details_confirmed",
                "description": "Payer has confirmed all their details for this billing request."
            },
            {
                "origin": "payer",
                "cause": "billing_request_payer_details_confirmed",
                "description": "Payer has confirmed all their details for this billing request."
            }
        ]
    },
    {
        "action": "collect_amount",
        "description": "Amount has been collected for this billing request.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_collect_amount",
                "description": "Amount has been collected for this billing request."
            }
        ]
    },
    {
        "action": "bank_authorisation_expired",
        "description": "A bank authorisation for this billing request has expired.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_bank_authorisation_expired",
                "description": "A bank authorisation for this billing request has expired."
            }
        ]
    },
    {
        "action": "flow_exited",
        "description": "The billing request flow has been exited by the payer.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_flow_exited",
                "description": "The billing request flow has been exited by the payer."
            }
        ]
    },
    {
        "action": "collect_customer_details",
        "description": "Customer details have been collected for this billing request.",
        "details": [
            {
                "origin": "api",
                "cause": "billing_request_collect_customer_details",
                "description": "Customer details have been collected for this billing request."
            },
            {
                "origin": "payer",
                "cause": "billing_request_collect_customer_details",
                "description": "Customer details have been collected for this billing request."
            }
        ]
    },
    {
        "action": "created",
        "description": "This billing request has been created.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "billing_request_created",
                "description": "This billing request has been created."
            },
            {
                "origin": "api",
                "cause": "billing_request_created",
                "description": "This billing request has been created."
            },
            {
                "origin": "payer",
                "cause": "billing_request_created",
                "description": "This billing request has been created."
            }
        ]
    },
    {
        "action": "bank_authorisation_failed",
        "description": "A bank authorisation for this billing request has failed because of a bank account mismatch.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_bank_authorisation_failed",
                "description": "A bank authorisation for this billing request has failed because of a bank account mismatch."
            },
            {
                "origin": "gocardless",
                "cause": "billing_request_bank_authorisation_failed",
                "description": "A bank authorisation for this billing request has failed because of a bank account mismatch."
            }
        ]
    },
    {
        "action": "payer_geo_blocked",
        "description": "Payer blocked for 24 hours for attempting to pay from an unsupported location.",
        "details": [
            {
                "origin": "payer",
                "cause": "payer_geo_blocked",
                "description": "Payer blocked for 24 hours for attempting to pay from an unsupported location."
            }
        ]
    },
    {
        "action": "flow_created",
        "description": "A billing request flow has been created against this billing request.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "billing_request_flow_created",
                "description": "A billing request flow has been created against this billing request."
            },
            {
                "origin": "api",
                "cause": "billing_request_flow_created",
                "description": "A billing request flow has been created against this billing request."
            },
            {
                "origin": "payer",
                "cause": "billing_request_flow_created",
                "description": "A billing request flow has been created against this billing request."
            }
        ]
    },
    {
        "action": "bank_authorisation_denied",
        "description": "A bank authorisation for this billing request has been denied by the payer.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_bank_authorisation_denied",
                "description": "A bank authorisation for this billing request has been denied by the payer."
            },
            {
                "origin": "gocardless",
                "cause": "billing_request_bank_authorisation_denied",
                "description": "A bank authorisation for this billing request has been denied by the payer."
            }
        ]
    },
    {
        "action": "select_institution",
        "description": "Institution details have been collected for this billing request.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_select_institution",
                "description": "Institution details have been collected for this billing request."
            }
        ]
    },
    {
        "action": "bank_authorisation_visited",
        "description": "A bank authorisation link for this billing request has been visited.",
        "details": [
            {
                "origin": "payer",
                "cause": "billing_request_bank_authorisation_visited",
                "description": "A bank authorisation link for this billing request has been visited."
            }
        ]
    },
    {
        "action": "cancelled",
        "description": "This billing request has been cancelled none of the resources have been created.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "billing_request_cancelled",
                "description": "This billing request has been cancelled none of the resources have been created."
            },
            {
                "origin": "api",
                "cause": "billing_request_cancelled",
                "description": "This billing request has been cancelled none of the resources have been created."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, RootModel


class BillingRequestChooseCurrency(BaseModel):
    action: Literal["choose_currency"]
    description: str
    details: BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail


class BillingRequestFulfilled(BaseModel):
    action: Literal["fulfilled"]
    description: str
    details: BillingRequestFulfilledBillingRequestFulfilledDetail


class BillingRequestBankAuthorisationAuthorised(BaseModel):
    action: Literal["bank_authorisation_authorised"]
    description: str
    details: BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail


class BillingRequestFlowVisited(BaseModel):
    action: Literal["flow_visited"]
    description: str
    details: BillingRequestFlowVisitedBillingRequestFlowVisitedDetail


class BillingRequestFailed(BaseModel):
    action: Literal["failed"]
    description: str
    details: BillingRequestFailedBillingRequestFailedDetail


class BillingRequestCollectBankAccount(BaseModel):
    action: Literal["collect_bank_account"]
    description: str
    details: BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail


class BillingRequestPayerDetailsConfirmed(BaseModel):
    action: Literal["payer_details_confirmed"]
    description: str
    details: (
        BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail
    )


class BillingRequestCollectAmount(BaseModel):
    action: Literal["collect_amount"]
    description: str
    details: BillingRequestCollectAmountBillingRequestCollectAmountDetail


class BillingRequestBankAuthorisationExpired(BaseModel):
    action: Literal["bank_authorisation_expired"]
    description: str
    details: BillingRequestBankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail


class BillingRequestFlowExited(BaseModel):
    action: Literal["flow_exited"]
    description: str
    details: BillingRequestFlowExitedBillingRequestFlowExitedDetail


class BillingRequestCollectCustomerDetails(BaseModel):
    action: Literal["collect_customer_details"]
    description: str
    details: (
        BillingRequestCollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail
    )


class BillingRequestCreated(BaseModel):
    action: Literal["created"]
    description: str
    details: BillingRequestCreatedBillingRequestCreatedDetail


class BillingRequestBankAuthorisationFailed(BaseModel):
    action: Literal["bank_authorisation_failed"]
    description: str
    details: (
        BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail
    )


class BillingRequestPayerGeoBlocked(BaseModel):
    action: Literal["payer_geo_blocked"]
    description: str
    details: BillingRequestPayerGeoBlockedPayerGeoBlockedDetail


class BillingRequestFlowCreated(BaseModel):
    action: Literal["flow_created"]
    description: str
    details: BillingRequestFlowCreatedBillingRequestFlowCreatedDetail


class BillingRequestBankAuthorisationDenied(BaseModel):
    action: Literal["bank_authorisation_denied"]
    description: str
    details: (
        BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail
    )


class BillingRequestSelectInstitution(BaseModel):
    action: Literal["select_institution"]
    description: str
    details: BillingRequestSelectInstitutionBillingRequestSelectInstitutionDetail


class BillingRequestBankAuthorisationVisited(BaseModel):
    action: Literal["bank_authorisation_visited"]
    description: str
    details: BillingRequestBankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail


class BillingRequestCancelled(BaseModel):
    action: Literal["cancelled"]
    description: str
    details: BillingRequestCancelledBillingRequestCancelledDetail


class BillingRequestChooseCurrencyBillingRequestChooseCurrencyDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["billing_request_choose_currency"]
    description: str


class BillingRequestFulfilledBillingRequestFulfilledDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["billing_request_fulfilled"]
    description: str


class BillingRequestBankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail(
    BaseModel
):
    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


class BillingRequestFlowVisitedBillingRequestFlowVisitedDetail(BaseModel):
    origin: Literal["payer"]
    cause: Literal["billing_request_flow_visited"]
    description: str


class BillingRequestFailedBillingRequestFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["billing_request_failed"]
    description: str


class BillingRequestCollectBankAccountBillingRequestCollectBankAccountDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


class BillingRequestPayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail(
    BaseModel
):
    origin: Literal["api"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


class BillingRequestCollectAmountBillingRequestCollectAmountDetail(BaseModel):
    origin: Literal["payer"]
    cause: Literal["billing_request_collect_amount"]
    description: str


class BillingRequestBankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail(
    BaseModel
):
    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_expired"]
    description: str


class BillingRequestFlowExitedBillingRequestFlowExitedDetail(BaseModel):
    origin: Literal["payer"]
    cause: Literal["billing_request_flow_exited"]
    description: str


class BillingRequestCollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail(
    BaseModel
):
    origin: Literal["api"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


class BillingRequestCreatedBillingRequestCreatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["billing_request_created"]
    description: str


class BillingRequestBankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail(
    BaseModel
):
    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


class BillingRequestPayerGeoBlockedPayerGeoBlockedDetail(BaseModel):
    origin: Literal["payer"]
    cause: Literal["payer_geo_blocked"]
    description: str


class BillingRequestFlowCreatedBillingRequestFlowCreatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["billing_request_flow_created"]
    description: str


class BillingRequestBankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail(
    BaseModel
):
    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


class BillingRequestSelectInstitutionBillingRequestSelectInstitutionDetail(BaseModel):
    origin: Literal["payer"]
    cause: Literal["billing_request_select_institution"]
    description: str


class BillingRequestBankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail(
    BaseModel
):
    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_visited"]
    description: str


class BillingRequestCancelledBillingRequestCancelledDetail(BaseModel):
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
