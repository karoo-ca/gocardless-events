"""
"payer_authorizations": [
    {
        "action": "failed",
        "description": "PayerAuthorisation is failed. Customer CustomerBankAccount and Mandate creation have been failed.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "customer_creation_failed",
                "description": "PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed."
            },
            {
                "origin": "gocardless",
                "cause": "customer_bank_account_creation_failed",
                "description": "PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_creation_failed",
                "description": "PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed."
            }
        ]
    },
    {
        "action": "completed",
        "description": "PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payer_authorisation_completed",
                "description": "PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class PayerAuthorizationFailed(BaseModel):
    action: Literal["failed"]
    description: str
    details: List[
        Annotated[
            Union[
                PayerAuthorizationFailedCustomerCreationFailedDetail,
                PayerAuthorizationFailedCustomerBankAccountCreationFailedDetail,
                PayerAuthorizationFailedMandateCreationFailedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PayerAuthorizationCompleted(BaseModel):
    action: Literal["completed"]
    description: str
    details: PayerAuthorizationCompletedPayerAuthorisationCompletedDetail


class PayerAuthorizationFailedCustomerCreationFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["customer_creation_failed"]
    description: str


class PayerAuthorizationFailedCustomerBankAccountCreationFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["customer_bank_account_creation_failed"]
    description: str


class PayerAuthorizationFailedMandateCreationFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_creation_failed"]
    description: str


class PayerAuthorizationCompletedPayerAuthorisationCompletedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payer_authorisation_completed"]
    description: str


PayerAuthorizationType = Annotated[
    Union[
        PayerAuthorizationFailed,
        PayerAuthorizationCompleted,
    ],
    Field(..., discriminator="action"),
]

PayerAuthorization = RootModel[PayerAuthorizationType]
