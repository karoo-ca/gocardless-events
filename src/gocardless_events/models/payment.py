from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class SurchargeFeeDebitedSurchargeFeeDebitedGocardlessDetail(BaseModel):
    """
    A surcharge fee has been charged for a payment.
    """

    origin: Literal["gocardless"]
    cause: Literal["surcharge_fee_debited"]
    description: str


SurchargeFeeDebitedSurchargeFeeDebitedDetail = (
    SurchargeFeeDebitedSurchargeFeeDebitedGocardlessDetail
)


class ChargebackCancelledPaymentConfirmedBankDetail(BaseModel):
    """
    The chargeback for this payment was reversed
    """

    origin: Literal["bank"]
    cause: Literal["payment_confirmed"]
    description: str


class ChargebackCancelledPaymentConfirmedGocardlessDetail(BaseModel):
    """
    The chargeback for this payment was reversed
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_confirmed"]
    description: str


ChargebackCancelledPaymentConfirmedDetail = Annotated[
    ChargebackCancelledPaymentConfirmedBankDetail
    | ChargebackCancelledPaymentConfirmedGocardlessDetail,
    Field(..., discriminator="origin"),
]


class CustomerApprovalGrantedCustomerApprovalGrantedCustomerDetail(BaseModel):
    """
    The customer granted approval for this payment
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


CustomerApprovalGrantedCustomerApprovalGrantedDetail = (
    CustomerApprovalGrantedCustomerApprovalGrantedCustomerDetail
)


class LateFailureSettledLateFailureSettledGocardlessDetail(BaseModel):
    """
    This late failed payment has been settled against a payout.
    """

    origin: Literal["gocardless"]
    cause: Literal["late_failure_settled"]
    description: str


LateFailureSettledLateFailureSettledDetail = (
    LateFailureSettledLateFailureSettledGocardlessDetail
)


class ChargedBackAuthorisationDisputedBankDetail(BaseModel):
    """
    This payment was charged back by the customer's bank because the customer disputed authorising the transaction.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


ChargedBackAuthorisationDisputedDetail = ChargedBackAuthorisationDisputedBankDetail


class ChargedBackRefundRequestedBankDetail(BaseModel):
    """
    This payment was charged back by the customer's bank at the customer's request within the 8 week cool-off period.
    """

    origin: Literal["bank"]
    cause: Literal["refund_requested"]
    scheme: str
    reason_code: str
    description: str


ChargedBackRefundRequestedDetail = ChargedBackRefundRequestedBankDetail


class ChargedBackMandateCancelledBankDetail(BaseModel):
    """
    This payment was charged back because the mandate was withdrawn.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


ChargedBackMandateCancelledDetail = ChargedBackMandateCancelledBankDetail


class ChargedBackReturnOnOdfiRequestBankDetail(BaseModel):
    """
    This payment was charged back by the customer's bank because the customer disputed authorising the transaction.
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


ChargedBackReturnOnOdfiRequestDetail = ChargedBackReturnOnOdfiRequestBankDetail


class ChargedBackOtherBankDetail(BaseModel):
    """
    The payment was charged back.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


ChargedBackOtherDetail = ChargedBackOtherBankDetail


class CustomerApprovalDeniedCustomerApprovalDeniedCustomerDetail(BaseModel):
    """
    The customer denied approval for this payment
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_denied"]
    description: str


CustomerApprovalDeniedCustomerApprovalDeniedDetail = (
    CustomerApprovalDeniedCustomerApprovalDeniedCustomerDetail
)


class ResubmissionRequestedPaymentRetriedApiDetail(BaseModel):
    """
    An attempt to retry this payment was requested.
    """

    origin: Literal["api"]
    cause: Literal["payment_retried"]
    description: str


ResubmissionRequestedPaymentRetriedDetail = ResubmissionRequestedPaymentRetriedApiDetail


class ResubmissionRequestedPaymentAutoretriedGocardlessDetail(BaseModel):
    """
    The payment was scheduled for resubmission automatically by GoCardless.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_autoretried"]
    description: str


ResubmissionRequestedPaymentAutoretriedDetail = (
    ResubmissionRequestedPaymentAutoretriedGocardlessDetail
)


class FailedReferToPayerBankDetail(BaseModel):
    """
    The customer's account had insufficient funds to make this payment.
    """

    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


FailedReferToPayerDetail = FailedReferToPayerBankDetail


class FailedBankAccountClosedBankDetail(BaseModel):
    """
    This payment failed because the customer is deceased.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


FailedBankAccountClosedDetail = FailedBankAccountClosedBankDetail


class FailedInvalidBankDetailsBankDetail(BaseModel):
    """
    The account number was invalid. The mandate will also be cancelled or failed.
    """

    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


FailedInvalidBankDetailsDetail = FailedInvalidBankDetailsBankDetail


class FailedAuthorisationDisputedBankDetail(BaseModel):
    """
    The customer claims that they asked you to cancel their mandate before you took the payment.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


FailedAuthorisationDisputedDetail = FailedAuthorisationDisputedBankDetail


class FailedReturnOnOdfiRequestBankDetail(BaseModel):
    """
    This payment was charged back by the customer's bank because the customer disputed authorising the transaction.
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


FailedReturnOnOdfiRequestDetail = FailedReturnOnOdfiRequestBankDetail


class FailedOtherBankDetail(BaseModel):
    """
    There was an internal error processing this payment.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class FailedOtherGocardlessDetail(BaseModel):
    """
    There was an internal error processing this payment.
    """

    origin: Literal["gocardless"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


FailedOtherDetail = Annotated[
    FailedOtherBankDetail | FailedOtherGocardlessDetail,
    Field(..., discriminator="origin"),
]


class FailedTestFailureBankDetail(BaseModel):
    """
    GoCardless has marked this payment as failed in sandbox to enable testing of payment failure webhooks.
    """

    origin: Literal["bank"]
    cause: Literal["test_failure"]
    scheme: str
    reason_code: str
    description: str


FailedTestFailureDetail = FailedTestFailureBankDetail


class FailedMandateCancelledBankDetail(BaseModel):
    """
    The customer cancelled the mandate at their bank before the payment could be collected.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


FailedMandateCancelledDetail = FailedMandateCancelledBankDetail


class FailedBankAccountTransferredBankDetail(BaseModel):
    """
    Your customer's mandate was transferred to a new bank account but this payment was submitted to the old account. You may wish to retry the payment once you have received a transferred webhook for the corresponding mandate.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


FailedBankAccountTransferredDetail = FailedBankAccountTransferredBankDetail


class FailedDirectDebitNotEnabledBankDetail(BaseModel):
    """
    The bank account for this payment does not support SEPA Direct Debit. The mandate will also be cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


FailedDirectDebitNotEnabledDetail = FailedDirectDebitNotEnabledBankDetail


class FailedAccountBlockedForAnyFinancialTransactionBankDetail(BaseModel):
    """
    This payment failed because the payer's account was blocked.
    """

    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


FailedAccountBlockedForAnyFinancialTransactionDetail = (
    FailedAccountBlockedForAnyFinancialTransactionBankDetail
)


class FailedInsufficientFundsBankDetail(BaseModel):
    """
    The customer's account had insufficient funds to make this payment.
    """

    origin: Literal["bank"]
    cause: Literal["insufficient_funds"]
    scheme: str
    reason_code: str
    description: str


FailedInsufficientFundsDetail = FailedInsufficientFundsBankDetail


class FailedPaymentStoppedBankDetail(BaseModel):
    """
    The payment was stopped by the payer or their bank.
    """

    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


FailedPaymentStoppedDetail = FailedPaymentStoppedBankDetail


class FailedBankDeclinedPaymentBankDetail(BaseModel):
    """
    Payment declined by the bank.
    """

    origin: Literal["bank"]
    cause: Literal["bank_declined_payment"]
    scheme: str
    reason_code: str
    description: str


FailedBankDeclinedPaymentDetail = FailedBankDeclinedPaymentBankDetail


class FailedDailyPaymentLimitReachedBankDetail(BaseModel):
    """
    Payment exceeds the daily payment limit for this payer imposed by the bank.
    """

    origin: Literal["bank"]
    cause: Literal["daily_payment_limit_reached"]
    scheme: str
    reason_code: str
    description: str


FailedDailyPaymentLimitReachedDetail = FailedDailyPaymentLimitReachedBankDetail


class FailedInsufficientPaymentPermissionsBankDetail(BaseModel):
    """
    Payment denied due to missing approvals from the bank.
    """

    origin: Literal["bank"]
    cause: Literal["insufficient_payment_permissions"]
    scheme: str
    reason_code: str
    description: str


FailedInsufficientPaymentPermissionsDetail = (
    FailedInsufficientPaymentPermissionsBankDetail
)


class FailedPaymentViolatedMandateParametersBankDetail(BaseModel):
    """
    The payment failed due to a violation of the associated mandate consent parameters.
    """

    origin: Literal["bank"]
    cause: Literal["payment_violated_mandate_parameters"]
    scheme: str
    reason_code: str
    description: str


FailedPaymentViolatedMandateParametersDetail = (
    FailedPaymentViolatedMandateParametersBankDetail
)


class SubmittedPaymentSubmittedGocardlessDetail(BaseModel):
    """
    Payment submitted to the banks. As a result it can no longer be cancelled.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_submitted"]
    description: str


SubmittedPaymentSubmittedDetail = SubmittedPaymentSubmittedGocardlessDetail


class ConfirmedPaymentConfirmedGocardlessDetail(BaseModel):
    """
    Enough time has passed since the payment was submitted for the banks to return an error so this payment is now confirmed.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_confirmed"]
    description: str


ConfirmedPaymentConfirmedDetail = ConfirmedPaymentConfirmedGocardlessDetail


class CreatedPaymentCreatedApiDetail(BaseModel):
    """
    Payment created via the API.
    """

    origin: Literal["api"]
    cause: Literal["payment_created"]
    description: str


class CreatedPaymentCreatedGocardlessDetail(BaseModel):
    """
    Payment created by a subscription.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_created"]
    description: str


CreatedPaymentCreatedDetail = Annotated[
    CreatedPaymentCreatedApiDetail | CreatedPaymentCreatedGocardlessDetail,
    Field(..., discriminator="origin"),
]


class CreatedInstalmentScheduleCreatedApiDetail(BaseModel):
    """
    Payment created by an instalment schedule.
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_created"]
    description: str


CreatedInstalmentScheduleCreatedDetail = CreatedInstalmentScheduleCreatedApiDetail


class ChargebackSettledChargebackSettledGocardlessDetail(BaseModel):
    """
    This charged back payment has been settled against a payout.
    """

    origin: Literal["gocardless"]
    cause: Literal["chargeback_settled"]
    description: str


ChargebackSettledChargebackSettledDetail = (
    ChargebackSettledChargebackSettledGocardlessDetail
)


class PaidOutPaymentPaidOutGocardlessDetail(BaseModel):
    """
    The payment has been paid out by GoCardless.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_paid_out"]
    description: str


PaidOutPaymentPaidOutDetail = PaidOutPaymentPaidOutGocardlessDetail


class CancelledBankAccountClosedBankDetail(BaseModel):
    """
    This payment was cancelled because the customer is deceased.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class CancelledBankAccountClosedApiDetail(BaseModel):
    """
    The bank account for this payment was disabled at your request.
    """

    origin: Literal["api"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


CancelledBankAccountClosedDetail = Annotated[
    CancelledBankAccountClosedBankDetail | CancelledBankAccountClosedApiDetail,
    Field(..., discriminator="origin"),
]


class CancelledReferToPayerBankDetail(BaseModel):
    """
    This payment has been cancelled because the bank details for its mandate are incorrect.
    """

    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


CancelledReferToPayerDetail = CancelledReferToPayerBankDetail


class CancelledInvalidBankDetailsBankDetail(BaseModel):
    """
    This payment has been cancelled because the bank details for its mandate are incorrect.
    """

    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


CancelledInvalidBankDetailsDetail = CancelledInvalidBankDetailsBankDetail


class CancelledAuthorisationDisputedBankDetail(BaseModel):
    """
    This payment has been cancelled because the payer disputes authorising its mandate.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


CancelledAuthorisationDisputedDetail = CancelledAuthorisationDisputedBankDetail


class CancelledMandateCancelledBankDetail(BaseModel):
    """
    This payment has been cancelled because its mandate was cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class CancelledMandateCancelledApiDetail(BaseModel):
    """
    The mandate for this payment was cancelled at your request.
    """

    origin: Literal["api"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class CancelledMandateCancelledGocardlessDetail(BaseModel):
    """
    The mandate for this payment was cancelled at your request.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


CancelledMandateCancelledDetail = Annotated[
    CancelledMandateCancelledBankDetail
    | CancelledMandateCancelledApiDetail
    | CancelledMandateCancelledGocardlessDetail,
    Field(..., discriminator="origin"),
]


class CancelledOtherBankDetail(BaseModel):
    """
    There was an internal error processing this payment.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


CancelledOtherDetail = CancelledOtherBankDetail


class CancelledInstalmentScheduleCancelledGocardlessDetail(BaseModel):
    """
    payment_cancelled_at_request
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_cancelled"]
    scheme: str
    reason_code: str
    description: str


class CancelledInstalmentScheduleCancelledApiDetail(BaseModel):
    """
    payment_cancelled_at_request
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_cancelled"]
    scheme: str
    reason_code: str
    description: str


CancelledInstalmentScheduleCancelledDetail = Annotated[
    CancelledInstalmentScheduleCancelledGocardlessDetail
    | CancelledInstalmentScheduleCancelledApiDetail,
    Field(..., discriminator="origin"),
]


class CancelledPaymentCancelledApiDetail(BaseModel):
    """
    This payment was cancelled at your request.
    """

    origin: Literal["api"]
    cause: Literal["payment_cancelled"]
    scheme: str
    reason_code: str
    description: str


CancelledPaymentCancelledDetail = CancelledPaymentCancelledApiDetail


class CancelledBankAccountTransferredBankDetail(BaseModel):
    """
    The mandate for this payment was cancelled as the customer asked their bank to transfer the mandate to a new account but the bank has failed to send GoCardless the new bank details.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


CancelledBankAccountTransferredDetail = CancelledBankAccountTransferredBankDetail


class CancelledDirectDebitNotEnabledBankDetail(BaseModel):
    """
    This payment has been cancelled because the bank account it was going to be taken from does not support Direct Debit.
    """

    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


CancelledDirectDebitNotEnabledDetail = CancelledDirectDebitNotEnabledBankDetail


class CancelledAccountBlockedForAnyFinancialTransactionBankDetail(BaseModel):
    """
    This payment failed because the payer's account was blocked.
    """

    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


CancelledAccountBlockedForAnyFinancialTransactionDetail = (
    CancelledAccountBlockedForAnyFinancialTransactionBankDetail
)


class CancelledPaymentStoppedBankDetail(BaseModel):
    """
    The payment was stopped by the payer or their bank.
    """

    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


CancelledPaymentStoppedDetail = CancelledPaymentStoppedBankDetail


class CancelledMandateExpiredGocardlessDetail(BaseModel):
    """
    The mandate expired before the payment could be collected.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    scheme: str
    reason_code: str
    description: str


CancelledMandateExpiredDetail = CancelledMandateExpiredGocardlessDetail


class CancelledMandateSuspendedByPayerBankDetail(BaseModel):
    """
    The mandate for this payment was suspended by the payer.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_suspended_by_payer"]
    scheme: str
    reason_code: str
    description: str


CancelledMandateSuspendedByPayerDetail = CancelledMandateSuspendedByPayerBankDetail


class CancelledReturnOnOdfiRequestBankDetail(BaseModel):
    """
    The payment was cancelled because of an ODFI return request.
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


CancelledReturnOnOdfiRequestDetail = CancelledReturnOnOdfiRequestBankDetail


class CancelledInitialOneOffPaymentFailedGocardlessDetail(BaseModel):
    """
    This mandate has been cancelled because the initial faster payment failed
    """

    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    scheme: str
    reason_code: str
    description: str


CancelledInitialOneOffPaymentFailedDetail = (
    CancelledInitialOneOffPaymentFailedGocardlessDetail
)


class PaymentSurchargeFeeDebited(BaseModel):
    """
    A surcharge fee has been charged for this payment because it failed or got charged back.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["surcharge_fee_debited"]
    details: SurchargeFeeDebitedSurchargeFeeDebitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentChargebackCancelled(BaseModel):
    """
    The customer's bank has cancelled the chargeback request. This is almost always at the request of the customer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["chargeback_cancelled"]
    details: ChargebackCancelledPaymentConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentCustomerApprovalGranted(BaseModel):
    """
    The payment required additional approval from the customer before it could be submitted and that approval has been granted.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["customer_approval_granted"]
    details: CustomerApprovalGrantedCustomerApprovalGrantedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentLateFailureSettled(BaseModel):
    """
    The payment was a late failure which had already been paid out and has been debited from a payout.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["late_failure_settled"]
    details: LateFailureSettledLateFailureSettledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentChargedBack(BaseModel):
    """
    The customer asked their bank to refund the payment under the Direct Debit Guarantee and it has been returned to the customer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["charged_back"]
    details: Annotated[
        ChargedBackAuthorisationDisputedDetail
        | ChargedBackRefundRequestedDetail
        | ChargedBackMandateCancelledDetail
        | ChargedBackReturnOnOdfiRequestDetail
        | ChargedBackOtherDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentCustomerApprovalDenied(BaseModel):
    """
    The payment required additional approval from the customer before it could be submitted and that approval has been denied.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["customer_approval_denied"]
    details: CustomerApprovalDeniedCustomerApprovalDeniedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentResubmissionRequested(BaseModel):
    """
    A request to resubmit the payment was made by the payment retry endpoint. This can also mean that the payment was automatically scheduled for resubmission by GoCardless if you have opted in for the intelligent retries feature.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["resubmission_requested"]
    details: Annotated[
        ResubmissionRequestedPaymentRetriedDetail
        | ResubmissionRequestedPaymentAutoretriedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentFailed(BaseModel):
    """
    The payment could not be collected usually because the customer did not have sufficient funds available. GoCardless will automatically retry the payment if event'swill_attempt_retryfield is true. See the intelligent retries section below.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["failed"]
    details: Annotated[
        FailedReferToPayerDetail
        | FailedBankAccountClosedDetail
        | FailedInvalidBankDetailsDetail
        | FailedAuthorisationDisputedDetail
        | FailedReturnOnOdfiRequestDetail
        | FailedOtherDetail
        | FailedTestFailureDetail
        | FailedMandateCancelledDetail
        | FailedBankAccountTransferredDetail
        | FailedDirectDebitNotEnabledDetail
        | FailedAccountBlockedForAnyFinancialTransactionDetail
        | FailedInsufficientFundsDetail
        | FailedPaymentStoppedDetail
        | FailedBankDeclinedPaymentDetail
        | FailedDailyPaymentLimitReachedDetail
        | FailedInsufficientPaymentPermissionsDetail
        | FailedPaymentViolatedMandateParametersDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentSubmitted(BaseModel):
    """
    The payment has been submitted to the banks. It will be a few days until it is collected or fails.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["submitted"]
    details: SubmittedPaymentSubmittedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentConfirmed(BaseModel):
    """
    The payment has been collected from the customer's bank account and is now being held by GoCardless. It can take up to 5 working days for a payment to be collected and will then be held for a short time before becomingpaid_out.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["confirmed"]
    details: ConfirmedPaymentConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentCreated(BaseModel):
    """
    The payment has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["created"]
    details: Annotated[
        CreatedPaymentCreatedDetail | CreatedInstalmentScheduleCreatedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentChargebackSettled(BaseModel):
    """
    The payment was charged back having previously been paid out and has been debited from a payout.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["chargeback_settled"]
    details: ChargebackSettledChargebackSettledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentPaidOut(BaseModel):
    """
    The payment has left GoCardless and has been sent to the creditor's bank account.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["paid_out"]
    details: PaidOutPaymentPaidOutDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class PaymentCancelled(BaseModel):
    """
    The payment was cancelled.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["payments"]
    action: Literal["cancelled"]
    details: Annotated[
        CancelledBankAccountClosedDetail
        | CancelledReferToPayerDetail
        | CancelledInvalidBankDetailsDetail
        | CancelledAuthorisationDisputedDetail
        | CancelledMandateCancelledDetail
        | CancelledOtherDetail
        | CancelledInstalmentScheduleCancelledDetail
        | CancelledPaymentCancelledDetail
        | CancelledBankAccountTransferredDetail
        | CancelledDirectDebitNotEnabledDetail
        | CancelledAccountBlockedForAnyFinancialTransactionDetail
        | CancelledPaymentStoppedDetail
        | CancelledMandateExpiredDetail
        | CancelledMandateSuspendedByPayerDetail
        | CancelledReturnOnOdfiRequestDetail
        | CancelledInitialOneOffPaymentFailedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


PaymentType = Annotated[
    PaymentSurchargeFeeDebited
    | PaymentChargebackCancelled
    | PaymentCustomerApprovalGranted
    | PaymentLateFailureSettled
    | PaymentChargedBack
    | PaymentCustomerApprovalDenied
    | PaymentResubmissionRequested
    | PaymentFailed
    | PaymentSubmitted
    | PaymentConfirmed
    | PaymentCreated
    | PaymentChargebackSettled
    | PaymentPaidOut
    | PaymentCancelled,
    Field(..., discriminator="action"),
]
Payment = RootModel[PaymentType]
