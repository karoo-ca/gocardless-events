from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class PayerAuthorizationFailed(BaseModel):
    """
    PayerAuthorisation is failed. Customer CustomerBankAccount and Mandate creation have been failed.
    """

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
    """
    PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created.
    """

    action: Literal["completed"]
    description: str
    details: PayerAuthorizationCompletedPayerAuthorisationCompletedDetail


class PayerAuthorizationFailedCustomerCreationFailedDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["customer_creation_failed"]
    description: str


class PayerAuthorizationFailedCustomerBankAccountCreationFailedDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["customer_bank_account_creation_failed"]
    description: str


class PayerAuthorizationFailedMandateCreationFailedDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_creation_failed"]
    description: str


class PayerAuthorizationCompletedPayerAuthorisationCompletedDetail(BaseModel):
    """
    PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created.
    """

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
