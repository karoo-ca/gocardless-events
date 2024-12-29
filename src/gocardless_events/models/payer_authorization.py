from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class FailedCustomerCreationFailedGocardlessDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["customer_creation_failed"]
    description: str


FailedCustomerCreationFailedDetail = FailedCustomerCreationFailedGocardlessDetail


class FailedCustomerBankAccountCreationFailedGocardlessDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["customer_bank_account_creation_failed"]
    description: str


FailedCustomerBankAccountCreationFailedDetail = (
    FailedCustomerBankAccountCreationFailedGocardlessDetail
)


class FailedMandateCreationFailedGocardlessDetail(BaseModel):
    """
    PayerAuthorisation has failed. Customer CustomerBankAccount and Mandate creation have failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_creation_failed"]
    description: str


FailedMandateCreationFailedDetail = FailedMandateCreationFailedGocardlessDetail


class CompletedPayerAuthorisationCompletedGocardlessDetail(BaseModel):
    """
    PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["payer_authorisation_completed"]
    description: str


CompletedPayerAuthorisationCompletedDetail = (
    CompletedPayerAuthorisationCompletedGocardlessDetail
)


class PayerAuthorizationFailed(BaseModel):
    """
    PayerAuthorisation is failed. Customer CustomerBankAccount and Mandate creation have been failed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payer_authorizations"]
    action: Literal["failed"]
    details: Annotated[
        FailedCustomerCreationFailedDetail
        | FailedCustomerBankAccountCreationFailedDetail
        | FailedMandateCreationFailedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PayerAuthorizationCompleted(BaseModel):
    """
    PayerAuthorisation is completed. Customer CustomerBankAccount and Mandate have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payer_authorizations"]
    action: Literal["completed"]
    details: CompletedPayerAuthorisationCompletedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


PayerAuthorizationType = Annotated[
    PayerAuthorizationFailed | PayerAuthorizationCompleted,
    Field(..., discriminator="action"),
]
PayerAuthorization = RootModel[PayerAuthorizationType]
