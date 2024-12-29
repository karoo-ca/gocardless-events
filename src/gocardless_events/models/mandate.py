from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class MandateReinstated(BaseModel):
    """
    The mandate has become active again after it was cancelled or expired. This can be due to the customer's bank wishing to undo a cancellation or expiry notice they sent or because the mandate was successfully reinstated via the reinstate endpoint.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["reinstated"]
    details: MandateReinstatedMandateReinstatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateCustomerApprovalGranted(BaseModel):
    """
    The mandate required additional approval from the customer (e.g. permission from a second signatory) and that approval has been granted.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["customer_approval_granted"]
    details: MandateCustomerApprovalGrantedCustomerApprovalGrantedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateExpired(BaseModel):
    """
    No collection attempts were made against the mandate within the dormancy period of your service user number. As a result it has expired and no further collections can be taken against it. If you wish to continue taking payments from this customer you should request their permission and use the reinstate endpoint.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["expired"]
    details: Annotated[
        MandateExpiredMandateExpiredDetail | MandateExpiredMandateCancelledDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateResubmissionRequested(BaseModel):
    """
    A request to resubmit the mandate was made by the mandate reinstate endpoint.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["resubmission_requested"]
    details: Annotated[
        MandateResubmissionRequestedResubmissionRequestedDetail
        | MandateResubmissionRequestedBankAccountTransferredDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateFailed(BaseModel):
    """
    The mandate could not be set up generally because the specified bank account does not accept Direct Debit payments or is closed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["failed"]
    details: Annotated[
        MandateFailedBankAccountClosedDetail
        | MandateFailedReferToPayerDetail
        | MandateFailedMandateCancelledDetail
        | MandateFailedAuthorisationDisputedDetail
        | MandateFailedInvalidBankDetailsDetail
        | MandateFailedDirectDebitNotEnabledDetail
        | MandateFailedOtherDetail
        | MandateFailedReturnOnOdfiRequestDetail
        | MandateFailedBankAccountTransferredDetail
        | MandateFailedPaymentStoppedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateSubmitted(BaseModel):
    """
    The mandate has been submitted to the banks and should become active in a few days unless the bank declines the request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["submitted"]
    details: Annotated[
        MandateSubmittedMandateSubmittedDetail
        | MandateSubmittedBankAccountTransferredDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateTransferred(BaseModel):
    """
    The mandate has been transferred to a different bank account either using a bank switching service (where it is supported) or with help from GoCardless Support when a customer asks to change their bank account (we can make the switch after verifying the details). The event will includelinks[previous_customer_bank_account]andlinks[new_customer_bank_account]. When using a bank switching service the mandate may have been submitted again depending on how the involved banks handled the transfer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["transferred"]
    details: Annotated[
        MandateTransferredBankAccountTransferredDetail
        | MandateTransferredMandateTransferredDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateConsumed(BaseModel):
    """
    The mandate has been used to create a payment and has now been consumed. It cannot be used again.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["consumed"]
    details: MandateConsumedMandateConsumedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateCustomerApprovalSkipped(BaseModel):
    """
    The mandate originally was believed to require additional approval from the customer (e.g. permission from a second signatory) but approval has been skipped (for example because the mandate was erroneously marked as needing a second signature).
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["customer_approval_skipped"]
    details: MandateCustomerApprovalSkippedCustomerApprovalSkippedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateActive(BaseModel):
    """
    The mandate has been successfully set up by the customer's bank.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["active"]
    details: MandateActiveMandateActivatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateCreated(BaseModel):
    """
    The mandate has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["created"]
    details: MandateCreatedMandateCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateBlocked(BaseModel):
    """
    The mandate has been blocked because the customer's details matched against an entry in either our global blocklist or the blocklist populated by you. This mandate cannot be unblocked and no payments can be created against it. If you still wish to collect payments from this customer you will need to remove their details from any blocks you have created and ask them to set up a new mandate. If you contacted GoCardless to block the customer's details you will need to make a request to unblock them.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["blocked"]
    details: Annotated[
        MandateBlockedMandateBlockedDetail
        | MandateBlockedMandateBlockedByGocardlessDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateReplaced(BaseModel):
    """
    The mandate has been cancelled and replaced by a new mandate (for example because the creditor has moved to a new Service User Number). The event will includelinks[new_mandate]with the ID of the new mandate.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["replaced"]
    details: MandateReplacedSchemeIdentifierChangedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateCancelled(BaseModel):
    """
    The mandate has been cancelled either by the customer through their bank or this API or automatically when their bank account is closed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["mandates"]
    action: Literal["cancelled"]
    details: Annotated[
        MandateCancelledBankAccountClosedDetail
        | MandateCancelledMandateCancelledDetail
        | MandateCancelledAuthorisationDisputedDetail
        | MandateCancelledInvalidBankDetailsDetail
        | MandateCancelledDirectDebitNotEnabledDetail
        | MandateCancelledReferToPayerDetail
        | MandateCancelledReturnOnOdfiRequestDetail
        | MandateCancelledBankAccountTransferredDetail
        | MandateCancelledAccountBlockedForAnyFinancialTransactionDetail
        | MandateCancelledPaymentStoppedDetail
        | MandateCancelledOtherDetail
        | MandateCancelledInitialOneOffPaymentFailedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class MandateReinstatedMandateReinstatedDetail(BaseModel):
    """
    The time window after submission for the banks to refuse a mandate has ended without any errors being received so this mandate is now active.
    """

    origin: Literal["gocardless", "bank"]
    cause: Literal["mandate_reinstated"]
    description: str


class MandateCustomerApprovalGrantedCustomerApprovalGrantedDetail(BaseModel):
    """
    The customer has granted approval for this mandate
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


class MandateExpiredMandateExpiredDetail(BaseModel):
    """
    The mandate is being marked as expired because no payments have been collected against it for the dormancy period of your service user number. If you have access to the mandate reinstation API endpoint you can use this to attempt to set this mandate up again.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    description: str


class MandateExpiredMandateCancelledDetail(BaseModel):
    """
    This mandate was cancelled by the customer or their bank.
    """

    origin: Literal["bank", "gocardless"]
    cause: Literal["mandate_cancelled"]
    description: str


class MandateResubmissionRequestedResubmissionRequestedDetail(BaseModel):
    """
    An attempt to reinstate this mandate was requested.
    """

    origin: Literal["api"]
    cause: Literal["resubmission_requested"]
    description: str


class MandateResubmissionRequestedBankAccountTransferredDetail(BaseModel):
    """
    The customer's bank account was transferred to a different bank or building society.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateFailedBankAccountClosedDetail(BaseModel):
    """
    This bank account has been closed as the customer is deceased.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedReferToPayerDetail(BaseModel):
    """
    This mandate was cancelled due to a Notification of Change indicating the customer's account number or branch number was incorrect please contact the customer.
    """

    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedMandateCancelledDetail(BaseModel):
    """
    The mandate was already cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedAuthorisationDisputedDetail(BaseModel):
    """
    The mandate was already cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedInvalidBankDetailsDetail(BaseModel):
    """
    The specified bank account does not exist or was closed.
    """

    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedDirectDebitNotEnabledDetail(BaseModel):
    """
    The bank account does not support Direct Debit.
    """

    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedOtherDetail(BaseModel):
    """
    This mandate has been cancelled because a payment under it failed.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedReturnOnOdfiRequestDetail(BaseModel):
    """
    The mandate has been cancelled because a payment under it was charged back.
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedBankAccountTransferredDetail(BaseModel):
    """
    The customer's bank account was transferred to a different bank or building society.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedPaymentStoppedDetail(BaseModel):
    """
    The payment was stopped by the payer or their bank.
    """

    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class MandateSubmittedMandateSubmittedDetail(BaseModel):
    """
    The mandate has been submitted to the banks.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_submitted"]
    description: str


class MandateSubmittedBankAccountTransferredDetail(BaseModel):
    """
    The customer's bank account was transferred to a different bank or building society.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateTransferredBankAccountTransferredDetail(BaseModel):
    """
    The customer's bank account was transferred to a different bank or building society.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateTransferredMandateTransferredDetail(BaseModel):
    """
    This mandate was transferred to a new bank account through GoCardless.
    """

    origin: Literal["api"]
    cause: Literal["mandate_transferred"]
    description: str


class MandateConsumedMandateConsumedDetail(BaseModel):
    """
    The mandate has been used to create a payment and has now been consumed. It cannot be used again.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_consumed"]
    description: str


class MandateCustomerApprovalSkippedCustomerApprovalSkippedDetail(BaseModel):
    """
    The customer has skipped approval for this mandate
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_skipped"]
    description: str


class MandateActiveMandateActivatedDetail(BaseModel):
    """
    The time window after submission for the banks to refuse a mandate has ended without any errors being received so this mandate is now active.
    """

    origin: Literal["gocardless", "bank"]
    cause: Literal["mandate_activated"]
    description: str


class MandateCreatedMandateCreatedDetail(BaseModel):
    """
    Mandate created via the API.
    """

    origin: Literal["api", "gocardless"]
    cause: Literal["mandate_created"]
    description: str


class MandateBlockedMandateBlockedDetail(BaseModel):
    """
    The mandate has been blocked because the customer's details matched against an entry in the blocklist populated by you.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_blocked"]
    description: str


class MandateBlockedMandateBlockedByGocardlessDetail(BaseModel):
    """
    The mandate has been blocked because the customer's details matched against an entry in our global blocklist.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_blocked_by_gocardless"]
    description: str


class MandateReplacedSchemeIdentifierChangedDetail(BaseModel):
    """
    The creditor has changed to a different scheme identifier so this mandate has been cancelled and replaced by a new one.
    """

    origin: Literal["gocardless"]
    cause: Literal["scheme_identifier_changed"]
    description: str


class MandateCancelledBankAccountClosedDetail(BaseModel):
    """
    This bank account has been closed as the customer is deceased.
    """

    origin: Literal["bank", "api"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledMandateCancelledDetail(BaseModel):
    """
    The mandate was cancelled at a bank branch.
    """

    origin: Literal["bank", "api", "gocardless"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledAuthorisationDisputedDetail(BaseModel):
    """
    The customer disputes having authorised you to set up a mandate with them.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledInvalidBankDetailsDetail(BaseModel):
    """
    The specified bank account does not exist or was closed.
    """

    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledDirectDebitNotEnabledDetail(BaseModel):
    """
    The bank account does not support Direct Debit.
    """

    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledReferToPayerDetail(BaseModel):
    """
    This mandate has been cancelled because a payment under it failed.
    """

    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledReturnOnOdfiRequestDetail(BaseModel):
    """
    mandate_cancelled_because_payment_charged_back
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledBankAccountTransferredDetail(BaseModel):
    """
    The customer's bank account was transferred to a different bank or building society.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledAccountBlockedForAnyFinancialTransactionDetail(BaseModel):
    """
    The bank account for this mandate was blocked. Any subscriptions and pending payments will also be cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledPaymentStoppedDetail(BaseModel):
    """
    The payment was stopped by the payer or their bank.
    """

    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledOtherDetail(BaseModel):
    """
    This mandate has been cancelled because a payment under it failed.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledInitialOneOffPaymentFailedDetail(BaseModel):
    """
    This mandate has been cancelled because the initial faster payment failed
    """

    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    scheme: str
    reason_code: str
    description: str


MandateType = Annotated[
    MandateReinstated
    | MandateCustomerApprovalGranted
    | MandateExpired
    | MandateResubmissionRequested
    | MandateFailed
    | MandateSubmitted
    | MandateTransferred
    | MandateConsumed
    | MandateCustomerApprovalSkipped
    | MandateActive
    | MandateCreated
    | MandateBlocked
    | MandateReplaced
    | MandateCancelled,
    Field(..., discriminator="action"),
]

Mandate = RootModel[MandateType]
