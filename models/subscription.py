"""
"subscriptions": [
    {
        "action": "customer_approval_granted",
        "description": "The subscription required additional approval from the customer before it could become active and that approval has been granted.",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_granted",
                "description": "The customer granted approval for this subscription"
            }
        ]
    },
    {
        "action": "finished",
        "description": "This subscription has finished. No further payments will be created.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "subscription_finished",
                "description": "The subscription has finished."
            }
        ]
    },
    {
        "action": "resumed",
        "description": "This subscription was resumed.",
        "details": [
            {
                "origin": "api",
                "cause": "subscription_resumed",
                "description": "The subscription was resumed."
            },
            {
                "origin": "gocardless",
                "cause": "subscription_resumed",
                "description": "The subscription was resumed."
            }
        ]
    },
    {
        "action": "amended",
        "description": "The subscription amount has been changed.",
        "details": [
            {
                "origin": "api",
                "cause": "subscription_amended",
                "description": "Subscription amount has been amended."
            }
        ]
    },
    {
        "action": "customer_approval_denied",
        "description": "The subscription required additional approval from the customer before it could become active and that approval has been denied.",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_denied",
                "description": "The customer denied approval for this subscription"
            }
        ]
    },
    {
        "action": "paused",
        "description": "This subscription has been paused.",
        "details": [
            {
                "origin": "api",
                "cause": "subscription_paused",
                "description": "The subscription has been paused."
            },
            {
                "origin": "gocardless",
                "cause": "subscription_paused",
                "description": "The subscription has been paused."
            }
        ]
    },
    {
        "action": "scheduled_pause_cancelled",
        "description": "An upcoming pause for this subscription has been cancelled.",
        "details": [
            {
                "origin": "api",
                "cause": "scheduled_pause_cancelled",
                "description": "An upcoming pause for this subscription has been cancelled."
            }
        ]
    },
    {
        "action": "scheduled_pause",
        "description": "This subscription has been scheduled to be paused at a future date.",
        "details": [
            {
                "origin": "api",
                "cause": "scheduled_pause",
                "description": "The subscription has been scheduled to be paused at a future date."
            }
        ]
    },
    {
        "action": "created",
        "description": "The subscription has been created.",
        "details": [
            {
                "origin": "api",
                "cause": "subscription_created",
                "description": "Subscription created via the API."
            }
        ]
    },
    {
        "action": "payment_created",
        "description": "A payment has been created by this subscription.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payment_created",
                "description": "Payment created by a subscription."
            }
        ]
    },
    {
        "action": "scheduled_resume",
        "description": "This paused subscription has been scheduled to be resumed at a future date.",
        "details": [
            {
                "origin": "api",
                "cause": "scheduled_resume",
                "description": "This paused subscription has been scheduled to be resumed at a future date."
            }
        ]
    },
    {
        "action": "cancelled",
        "description": "This subscription has been cancelled. No further payments will be created.",
        "details": [
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R14ACH_RETURN-R15",
                "description": "This subscription was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-C01ACH_RETURN-C02ACH_RETURN-C03ACH_RETURN-C05ACH_RETURN-C06ACH_RETURN-C07ACH_RETURN-R08NOTIFICATION_OF_CHANGE-C01NOTIFICATION_OF_CHANGE-C02NOTIFICATION_OF_CHANGE-C03NOTIFICATION_OF_CHANGE-C05NOTIFICATION_OF_CHANGE-C06NOTIFICATION_OF_CHANGE-C07NOTIFICATION_OF_CHANGE-R08",
                "description": "This subscription has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R02ACH_RETURN-R12",
                "description": "This subscription has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07",
                "description": "This subscription was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R10",
                "description": "This subscription has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R03ACH_RETURN-R04ACH_RETURN-R13ACH_RETURN-R28ACH_RETURN-R82",
                "description": "This subscription has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16ACH_RETURN-R20ACH_RETURN-R34",
                "description": "This subscription has been cancelled because the bank account it was going to be taken from does not support direct debit."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16ACH_RETURN-R20ACH_RETURN-R29",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R08ACH_RETURN-R10ACH_RETURN-R11ACH_RETURN-R29ACH_RETURN-R31ACH_RETURN-R51",
                "description": "This subscription has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "api",
                "cause": "subscription_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "The subscription has been cancelled at your request."
            },
            {
                "origin": "api",
                "cause": "mandate_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "The subscription was cancelled because its mandate was cancelled at your request."
            },
            {
                "origin": "api",
                "cause": "bank_account_closed",
                "scheme": "None",
                "reason_code": "None",
                "description": "The mandate for this subscription was cancelled at your request."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_expired",
                "scheme": "None",
                "reason_code": "None",
                "description": "The subscription was cancelled because its mandate has expired."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ADDACS-0ADDACS-1",
                "description": "The mandate for this subscription was cancelled at a bank branch."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ADDACS-2ADDACS-B",
                "description": "The mandate for this subscription was cancelled as the customer's bank account has been closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "ADDACS-3ADDACS-C",
                "description": "The mandate for this subscription was cancelled as the customer asked their bank to transfer the mandate to a new account but the bank has failed to send GoCardless the new bank details."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "ADDACS-D",
                "description": "The customer disputes authorising this mandate."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-2",
                "description": "This subscription was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "bacs",
                "reason_code": "ARUDD-6",
                "description": "An error was received from the banks while setting up the mandate for this subscription."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-B",
                "description": "This subscription was cancelled because the customer closed their bank account before it could be collected."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "sepa_core",
                "reason_code": "AC01BE06",
                "description": "This subscription has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "AC04MD07",
                "description": "This subscription has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "sepa_core",
                "reason_code": "AG01AC06",
                "description": "This subscription has been cancelled because the bank account it was going to be taken from does not support direct debit."
            },
            {
                "origin": "bank",
                "cause": "account_blocked_for_any_financial_transaction",
                "scheme": "sepa_core",
                "reason_code": "AC06",
                "description": "This subscription has been cancelled because the bank account for its mandate was blocked."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "This subscription has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "This subscription has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-3DDICA-4DDICA-5DDICA-6DDICA-8",
                "description": "This subscription has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "AUDDIS-2AUDDIS-B",
                "description": "This subscription has been cancelled because the bank account for its mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "AUDDIS-5",
                "description": "This subscription has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "AUDDIS-3AUDDIS-C",
                "description": "This subscription has been cancelled because the customer has requested for direct debits to be taken from a new account but their bank did not send GoCardless the new bank details."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "bacs",
                "reason_code": "AUDDIS-FAUDDIS-GAUDDIS-N",
                "description": "This subscription has been cancelled because the bank account for its mandate does not support direct debit."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "ARUDD-5ARUDD-YARUDD-E",
                "description": "This subscription has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ARUDD-1",
                "description": "This subscription was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "api",
                "cause": "plan_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "The subscription has been cancelled because the associated plan was cancelled."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "UDUNAUT",
                "description": "This subscription has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs",
                "reason_code": "CBC",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "becs",
                "reason_code": "2",
                "description": "This subscription has been cancelled because the bank account for its mandate does not support direct debit."
            },
            {
                "origin": "bank",
                "cause": "payment_stopped",
                "scheme": "becs",
                "reason_code": "2",
                "description": "The subscription was cancelled because the payment was stopped by the payer or their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "4",
                "description": "This subscription was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "DEN",
                "description": "This subscription has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC04",
                "description": "This subscription has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-900PAYMENT_STATUS_REPORT-902PAYMENT_STATUS_REPORT-912PAYMENT_STATUS_REPORT-1023PAYMENT_STATUS_REPORT-2014PAYMENT_STATUS_REPORT-2017PAYMENT_STATUS_REPORT-2018PAYMENT_STATUS_REPORT-2019PAYMENT_STATUS_REPORT-2020PAYMENT_STATUS_REPORT-2034PAYMENT_STATUS_REPORT-0518PAYMENT_STATUS_REPORT-0567PAYMENT_STATUS_REPORT-0573",
                "description": "This subscription has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-905",
                "description": "This subscription has been cancelled because the bank account for its mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-907",
                "description": "This subscription has been cancelled because the bank account for its mandate does not support direct debit."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-910",
                "description": "This subscription was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-915",
                "description": "This subscription has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-914",
                "description": "An error was received from the banks while setting up the mandate for this subscription."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-914",
                "description": "An error was received from the banks while setting up the mandate for this subscription."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-917PAYMENT_STATUS_REPORT-920",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "PAYER_MANDATE_CANCELLED",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_suspended_by_payer",
                "scheme": "pay_to",
                "reason_code": "SBP",
                "description": "The subscription has been cancelled because its mandate was suspended by payer."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "MERCHANT_MANDATE_CANCELLED",
                "description": "The mandate for this subscription was cancelled at your request."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "MANDATE_EXPIRED",
                "description": "The subscription was cancelled because its mandate has expired."
            },
            {
                "origin": "gocardless",
                "cause": "initial_one_off_payment_failed",
                "scheme": "None",
                "reason_code": "None",
                "description": "This subscription has been cancelled because its mandate was cancelled."
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class SubscriptionCustomerApprovalGranted(BaseModel):
    action: Literal["customer_approval_granted"]
    description: str
    details: SubscriptionCustomerApprovalGrantedCustomerApprovalGrantedDetail


class SubscriptionFinished(BaseModel):
    action: Literal["finished"]
    description: str
    details: SubscriptionFinishedSubscriptionFinishedDetail


class SubscriptionResumed(BaseModel):
    action: Literal["resumed"]
    description: str
    details: SubscriptionResumedSubscriptionResumedDetail


class SubscriptionAmended(BaseModel):
    action: Literal["amended"]
    description: str
    details: SubscriptionAmendedSubscriptionAmendedDetail


class SubscriptionCustomerApprovalDenied(BaseModel):
    action: Literal["customer_approval_denied"]
    description: str
    details: SubscriptionCustomerApprovalDeniedCustomerApprovalDeniedDetail


class SubscriptionPaused(BaseModel):
    action: Literal["paused"]
    description: str
    details: SubscriptionPausedSubscriptionPausedDetail


class SubscriptionScheduledPauseCancelled(BaseModel):
    action: Literal["scheduled_pause_cancelled"]
    description: str
    details: SubscriptionScheduledPauseCancelledScheduledPauseCancelledDetail


class SubscriptionScheduledPause(BaseModel):
    action: Literal["scheduled_pause"]
    description: str
    details: SubscriptionScheduledPauseScheduledPauseDetail


class SubscriptionCreated(BaseModel):
    action: Literal["created"]
    description: str
    details: SubscriptionCreatedSubscriptionCreatedDetail


class SubscriptionPaymentCreated(BaseModel):
    action: Literal["payment_created"]
    description: str
    details: SubscriptionPaymentCreatedPaymentCreatedDetail


class SubscriptionScheduledResume(BaseModel):
    action: Literal["scheduled_resume"]
    description: str
    details: SubscriptionScheduledResumeScheduledResumeDetail


class SubscriptionCancelled(BaseModel):
    action: Literal["cancelled"]
    description: str
    details: List[
        Annotated[
            Union[
                SubscriptionCancelledBankAccountClosedDetail,
                SubscriptionCancelledReturnOnOdfiRequestDetail,
                SubscriptionCancelledReferToPayerDetail,
                SubscriptionCancelledMandateCancelledDetail,
                SubscriptionCancelledInvalidBankDetailsDetail,
                SubscriptionCancelledDirectDebitNotEnabledDetail,
                SubscriptionCancelledAuthorisationDisputedDetail,
                SubscriptionCancelledSubscriptionCancelledDetail,
                SubscriptionCancelledMandateExpiredDetail,
                SubscriptionCancelledBankAccountTransferredDetail,
                SubscriptionCancelledAccountBlockedForAnyFinancialTransactionDetail,
                SubscriptionCancelledPlanCancelledDetail,
                SubscriptionCancelledPaymentStoppedDetail,
                SubscriptionCancelledOtherDetail,
                SubscriptionCancelledMandateSuspendedByPayerDetail,
                SubscriptionCancelledInitialOneOffPaymentFailedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class SubscriptionCustomerApprovalGrantedCustomerApprovalGrantedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


class SubscriptionFinishedSubscriptionFinishedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["subscription_finished"]
    description: str


class SubscriptionResumedSubscriptionResumedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["subscription_resumed"]
    description: str


class SubscriptionAmendedSubscriptionAmendedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["subscription_amended"]
    description: str


class SubscriptionCustomerApprovalDeniedCustomerApprovalDeniedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_denied"]
    description: str


class SubscriptionPausedSubscriptionPausedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["subscription_paused"]
    description: str


class SubscriptionScheduledPauseCancelledScheduledPauseCancelledDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["scheduled_pause_cancelled"]
    description: str


class SubscriptionScheduledPauseScheduledPauseDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["scheduled_pause"]
    description: str


class SubscriptionCreatedSubscriptionCreatedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["subscription_created"]
    description: str


class SubscriptionPaymentCreatedPaymentCreatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payment_created"]
    description: str


class SubscriptionScheduledResumeScheduledResumeDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["scheduled_resume"]
    description: str


class SubscriptionCancelledBankAccountClosedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledReferToPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledInvalidBankDetailsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledDirectDebitNotEnabledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledSubscriptionCancelledDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["subscription_cancelled"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledMandateExpiredDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledAccountBlockedForAnyFinancialTransactionDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledPlanCancelledDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["plan_cancelled"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledPaymentStoppedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledMandateSuspendedByPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_suspended_by_payer"]
    scheme: str
    reason_code: str
    description: str


class SubscriptionCancelledInitialOneOffPaymentFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    scheme: str
    reason_code: str
    description: str


SubscriptionType = Annotated[
    Union[
        SubscriptionCustomerApprovalGranted,
        SubscriptionFinished,
        SubscriptionResumed,
        SubscriptionAmended,
        SubscriptionCustomerApprovalDenied,
        SubscriptionPaused,
        SubscriptionScheduledPauseCancelled,
        SubscriptionScheduledPause,
        SubscriptionCreated,
        SubscriptionPaymentCreated,
        SubscriptionScheduledResume,
        SubscriptionCancelled,
    ],
    Field(..., discriminator="action"),
]

Subscription = RootModel[SubscriptionType]
