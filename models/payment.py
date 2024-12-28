"""
"payments": [
    {
        "action": "surcharge_fee_debited",
        "description": "A surcharge fee has been charged for this payment because it failed or got charged back.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "surcharge_fee_debited",
                "description": "A surcharge fee has been charged for a payment."
            }
        ]
    },
    {
        "action": "chargeback_cancelled",
        "description": "The customer's bank has cancelled the chargeback request. This is almost always at the request of the customer.",
        "details": [
            {
                "origin": "bank",
                "cause": "payment_confirmed",
                "description": "The chargeback for this payment was reversed"
            },
            {
                "origin": "gocardless",
                "cause": "payment_confirmed",
                "description": "The chargeback for this payment was reversed"
            }
        ]
    },
    {
        "action": "customer_approval_granted",
        "description": "The payment required additional approval from the customer before it could be submitted and that approval has been granted.",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_granted",
                "description": "The customer granted approval for this payment"
            }
        ]
    },
    {
        "action": "late_failure_settled",
        "description": "The payment was a late failure which had already been paid out and has been debited from a payout.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "late_failure_settled",
                "description": "This late failed payment has been settled against a payout."
            }
        ]
    },
    {
        "action": "charged_back",
        "description": "The customer asked their bank to refund the payment under the Direct Debit Guarantee and it has been returned to the customer.",
        "details": [
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R31",
                "description": "This payment was charged back by the customer's bank because the customer disputed authorising the transaction."
            },
            {
                "origin": "bank",
                "cause": "refund_requested",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16",
                "description": "This payment was charged back by the customer's bank at the customer's request within the 8 week cool-off period."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07",
                "description": "This payment was charged back because the mandate was withdrawn."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R08ACH_RETURN-R10ACH_RETURN-R11ACH_RETURN-R29",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "This payment was charged back by the customer's bank because the customer disputed authorising the transaction."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-1",
                "description": "The customer has disputed that the amount taken differs from the amount they were notified of."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-2",
                "description": "The customer has disputed having been notified of this Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-4",
                "description": "The customer claims that they asked you to cancel their mandate before you took the payment."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-5DDICA-6DDICA-8",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "This payment was charged back by the customer's bank because the customer disputed authorising the transaction."
            },
            {
                "origin": "bank",
                "cause": "refund_requested",
                "scheme": "sepa_core",
                "reason_code": "MD06",
                "description": "This payment was charged back by the customer's bank at the customer's request within the 8 week cool-off period."
            },
            {
                "origin": "bank",
                "cause": "refund_requested",
                "scheme": "betalingsservice",
                "reason_code": "PAYMENT_INFORMATION-0239",
                "description": "This payment was charged back by the customer's bank at the customer's request within the 8 week cool-off period."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "UDUNAUT",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs",
                "reason_code": "CBC",
                "description": "The customer cancelled their mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "UCDUOTHR",
                "description": "The payment was charged back."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "MD01",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-915",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-916PAYMENT_STATUS_REPORT-919",
                "description": "The customer has disputed that the amount taken differs from the amount they were notified of."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-918PAYMENT_STATUS_REPORT-921",
                "description": "The customer has disputed having been notified of this Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-917PAYMENT_STATUS_REPORT-920",
                "description": "This payment was charged back because the mandate was withdrawn."
            }
        ]
    },
    {
        "action": "customer_approval_denied",
        "description": "The payment required additional approval from the customer before it could be submitted and that approval has been denied.",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_denied",
                "description": "The customer denied approval for this payment"
            }
        ]
    },
    {
        "action": "resubmission_requested",
        "description": "A request to resubmit the payment was made by the payment retry endpoint. This can also mean that the payment was automatically scheduled for resubmission by GoCardless if you have opted in for the intelligent retries feature.",
        "details": [
            {
                "origin": "api",
                "cause": "payment_retried",
                "description": "An attempt to retry this payment was requested."
            },
            {
                "origin": "gocardless",
                "cause": "payment_autoretried",
                "description": "The payment was scheduled for resubmission automatically by GoCardless."
            }
        ]
    },
    {
        "action": "failed",
        "description": "The payment could not be collected usually because the customer did not have sufficient funds available. GoCardless will automatically retry the payment if event'swill_attempt_retryfield is true. See the intelligent retries section below.",
        "details": [
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R01ACH_RETURN-R09",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R14ACH_RETURN-R15",
                "description": "This payment failed because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R04ACH_RETURN-R13ACH_RETURN-R28ACH_RETURN-R82",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R03",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R02",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R12",
                "description": "This payment has been cancelled because the account has been sold to another financial institution."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16",
                "description": "This payment has been cancelled because the payer's bank account is frozen. ACH authorization will be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R32ACH_RETURN-R34ACH_RETURN-R83",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R20ACH_RETURN-R67ACH_RETURN-R75",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R08ACH_RETURN-R23ACH_RETURN-R29",
                "description": "The customer refused to accept this payment."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07",
                "description": "The customer claims that they asked you to cancel their mandate before you took the payment."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "This payment was charged back by the customer's bank because the customer disputed authorising the transaction."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "This payment has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R11",
                "description": "The payment was charged back. Customer advises an authorization to debit exists but there is an error or defect in the payment such that the entry does not conform to the terms of the authorization."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05",
                "description": "This payment was charged back because the customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R08",
                "description": "The customer has placed a stop on this payment and the authorisation has been cancelled. Please contact the customer to set up a new authorisation."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R31",
                "description": "This payment has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R10",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R24ACH_RETURN-R29ACH_RETURN-R83ACH_RETURN-R84ACH_RETURN-R85ACH_RETURN-R17",
                "description": "There was an internal error processing this payment."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R81",
                "description": "This payment has been cancelled because the customer's bank does not support the required payment type or transaction format."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R75",
                "description": "This payment was cancelled because the return entry was not a duplicate of an entry previously returned by the RDFI."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R34",
                "description": "This payment was cancelled because the financial institution's participation has been restricted by a regulatory authority."
            },
            {
                "origin": "bank",
                "cause": "test_failure",
                "scheme": "sepa_core",
                "reason_code": "TEST",
                "description": "GoCardless has marked this payment as failed in sandbox to enable testing of payment failure webhooks."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "bacs",
                "reason_code": "ARUDD-0",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ARUDD-1",
                "description": "The customer cancelled the mandate at their bank before the payment could be collected."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-2",
                "description": "This payment failed because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "ARUDD-3",
                "description": "Your customer's mandate was transferred to a new bank account but this payment was submitted to the old account. You may wish to retry the payment once you have received a transferred webhook for the corresponding mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "ARUDD-4",
                "description": "The customer has disputed having been notified of this Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "ARUDD-5ARUDD-YARUDD-E",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-B",
                "description": "The customer closed their account before the payment could be taken. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "bacs",
                "reason_code": "ARUDD-6",
                "description": "No mandate was setup for this payment. Some smaller banks require additional time to process mandates and may not have processed this customer's mandate yet so you may wish to retry the payment."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "ARUDD-7",
                "description": "The customer has disputed that the amount taken differs from the amount they were notified of."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "sepa_core",
                "reason_code": "AC01BE06",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "AC04",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "sepa_core",
                "reason_code": "AG01AC06",
                "description": "The bank account for this payment does not support SEPA Direct Debit. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "account_blocked_for_any_financial_transaction",
                "scheme": "sepa_core",
                "reason_code": "AC06",
                "description": "This payment failed because the payer's account was blocked."
            },
            {
                "origin": "bank",
                "cause": "insufficient_funds",
                "scheme": "sepa_core",
                "reason_code": "AM04",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "The customer cancelled their mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "MD07",
                "description": "This payment failed because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "sepa_core",
                "reason_code": "MS03RR04",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "sepa_core",
                "reason_code": "MS02",
                "description": "The customer refused to accept this payment."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "sepa_core",
                "reason_code": "SL01",
                "description": "The payment failed due to a restriction on Direct Debit payments from the payer's bank account."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "9",
                "description": "The customer's bank refused to accept this payment please refer to customer."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "278",
                "description": "There was an internal error processing this payment."
            },
            {
                "origin": "bank",
                "cause": "payment_stopped",
                "scheme": "becs",
                "reason_code": "2",
                "description": "The payment was stopped by the payer or their bank."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "becs",
                "reason_code": "2789",
                "description": "The payment failed due to a restriction on Direct Debit payments from the payer's bank account."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs",
                "reason_code": "6",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "15",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "34",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "DEN",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "gocardless",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "INT_ERR",
                "description": "There was an internal error processing this payment."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "RC02",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "MD01",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "AC04",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "MD07",
                "description": "This payment failed because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "AC01",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs",
                "reason_code": "NARR",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pay_to",
                "reason_code": "278",
                "description": "There was an internal error processing this payment."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "15",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pay_to",
                "reason_code": "34",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "RC02",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "betalingsservice",
                "reason_code": "PAYMENT_INFORMATION-0237",
                "description": "The customer refused to accept this payment."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "PAYMENT_INFORMATION-0238",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "betalingsservice",
                "reason_code": "INFORMATION_LIST-0282",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "betalingsservice",
                "reason_code": "INFORMATION_LIST-0253",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC05NEGATIVE_ACKNOWLEDGEMENT-AC05",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC04",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AG01",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC03NEGATIVE_ACKNOWLEDGEMENT-AC03",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AM04NEGATIVE_ACKNOWLEDGEMENT-AM04",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-MS01",
                "description": "The customer refused to accept this payment."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AM02",
                "description": "The payment failed due to a restriction on Direct Debit payments from the payer's bank account."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-901",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-900PAYMENT_STATUS_REPORT-902PAYMENT_STATUS_REPORT-912PAYMENT_STATUS_REPORT-1023PAYMENT_STATUS_REPORT-2014PAYMENT_STATUS_REPORT-2017PAYMENT_STATUS_REPORT-2018PAYMENT_STATUS_REPORT-2019PAYMENT_STATUS_REPORT-2020PAYMENT_STATUS_REPORT-0518PAYMENT_STATUS_REPORT-2034PAYMENT_STATUS_REPORT-0567PAYMENT_STATUS_REPORT-0573",
                "description": "The account number was invalid. The mandate will also be cancelled or failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-905",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-907PAYMENT_STATUS_REPORT-911PAYMENT_STATUS_REPORT-990",
                "description": "The payment failed due to a restriction on Direct Debit payments from the payer's bank account."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-910",
                "description": "This payment failed because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-903PAYMENT_STATUS_REPORT-908PAYMENT_STATUS_REPORT-914",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-909",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-BE05",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs_nz",
                "reason_code": "ACKNOWLEDGEMENT-FAILED",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "insufficient_funds",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "bank_declined_payment",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "Payment declined by the bank."
            },
            {
                "origin": "bank",
                "cause": "daily_payment_limit_reached",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "Payment exceeds the daily payment limit for this payer imposed by the bank."
            },
            {
                "origin": "bank",
                "cause": "insufficient_payment_permissions",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "Payment denied due to missing approvals from the bank."
            },
            {
                "origin": "bank",
                "cause": "payment_violated_mandate_parameters",
                "scheme": "faster_payments",
                "reason_code": "FAILED",
                "description": "The payment failed due to a violation of the associated mandate consent parameters."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "sepa_credit_transfer",
                "reason_code": "FAILED",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "insufficient_funds",
                "scheme": "sepa_credit_transfer",
                "reason_code": "FAILED",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "sepa_instant_credit_transfer",
                "reason_code": "FAILED",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "insufficient_funds",
                "scheme": "sepa_instant_credit_transfer",
                "reason_code": "FAILED",
                "description": "The customer's account had insufficient funds to make this payment."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pay_to",
                "reason_code": "FAILED",
                "description": "The payment failed but the reason for the failure was not provided usually for regulatory reasons."
            },
            {
                "origin": "bank",
                "cause": "insufficient_funds",
                "scheme": "pay_to",
                "reason_code": "FAILED",
                "description": "The customer's account had insufficient funds to make this payment."
            }
        ]
    },
    {
        "action": "submitted",
        "description": "The payment has been submitted to the banks. It will be a few days until it is collected or fails.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payment_submitted",
                "description": "Payment submitted to the banks. As a result it can no longer be cancelled."
            }
        ]
    },
    {
        "action": "confirmed",
        "description": "The payment has been collected from the customer's bank account and is now being held by GoCardless. It can take up to 5 working days for a payment to be collected and will then be held for a short time before becomingpaid_out.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payment_confirmed",
                "description": "Enough time has passed since the payment was submitted for the banks to return an error so this payment is now confirmed."
            }
        ]
    },
    {
        "action": "created",
        "description": "The payment has been created.",
        "details": [
            {
                "origin": "api",
                "cause": "payment_created",
                "description": "Payment created via the API."
            },
            {
                "origin": "gocardless",
                "cause": "payment_created",
                "description": "Payment created by a subscription."
            },
            {
                "origin": "api",
                "cause": "instalment_schedule_created",
                "description": "Payment created by an instalment schedule."
            }
        ]
    },
    {
        "action": "chargeback_settled",
        "description": "The payment was charged back having previously been paid out and has been debited from a payout.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "chargeback_settled",
                "description": "This charged back payment has been settled against a payout."
            }
        ]
    },
    {
        "action": "paid_out",
        "description": "The payment has left GoCardless and has been sent to the creditor's bank account.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "payment_paid_out",
                "description": "The payment has been paid out by GoCardless."
            }
        ]
    },
    {
        "action": "cancelled",
        "description": "The payment was cancelled.",
        "details": [
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R14ACH_RETURN-R15",
                "description": "This payment was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-C01ACH_RETURN-C02ACH_RETURN-C03ACH_RETURN-C05ACH_RETURN-C06ACH_RETURN-C07ACH_RETURN-R08ACH_RETURN-R26NOTIFICATION_OF_CHANGE-C01NOTIFICATION_OF_CHANGE-C02NOTIFICATION_OF_CHANGE-C03NOTIFICATION_OF_CHANGE-C05NOTIFICATION_OF_CHANGE-C06NOTIFICATION_OF_CHANGE-C07NOTIFICATION_OF_CHANGE-C08NOTIFICATION_OF_CHANGE-C09NOTIFICATION_OF_CHANGE-R08",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R02ACH_RETURN-R12",
                "description": "This payment has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R03ACH_RETURN-R04ACH_RETURN-R13ACH_RETURN-R26ACH_RETURN-R28ACH_RETURN-R82",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R20ACH_RETURN-R34",
                "description": "This payment has been cancelled because the bank account it was going to be taken from does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R06ACH_RETURN-R08ACH_RETURN-R10ACH_RETURN-R11ACH_RETURN-R29ACH_RETURN-R31ACH_RETURN-R51",
                "description": "This payment has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R29",
                "description": "This payment has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07ACH_RETURN-R06",
                "description": "This payment has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R85",
                "description": "There was an internal error processing this payment."
            },
            {
                "origin": "gocardless",
                "cause": "instalment_schedule_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "payment_cancelled_at_request"
            },
            {
                "origin": "api",
                "cause": "payment_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "This payment was cancelled at your request."
            },
            {
                "origin": "api",
                "cause": "mandate_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "The mandate for this payment was cancelled at your request."
            },
            {
                "origin": "api",
                "cause": "instalment_schedule_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "payment_cancelled_at_request"
            },
            {
                "origin": "api",
                "cause": "bank_account_closed",
                "scheme": "None",
                "reason_code": "None",
                "description": "The bank account for this payment was disabled at your request."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ADDACS-0ADDACS-1",
                "description": "The mandate for this payment was cancelled at a bank branch."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ADDACS-2ADDACS-B",
                "description": "The mandate for this payment was cancelled as the customer's bank account has been closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "ADDACS-3ADDACS-C",
                "description": "The mandate for this payment was cancelled as the customer asked their bank to transfer the mandate to a new account but the bank has failed to send GoCardless the new bank details."
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
                "description": "This payment was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-B",
                "description": "This payment was cancelled because the customer closed their bank account before it could be collected."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "bacs",
                "reason_code": "ARUDD-6",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "sepa_core",
                "reason_code": "AC01BE06",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "AC04MD07",
                "description": "This payment has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "sepa_core",
                "reason_code": "AG01AC06",
                "description": "This payment has been cancelled because the bank account it was going to be taken from does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "account_blocked_for_any_financial_transaction",
                "scheme": "sepa_core",
                "reason_code": "AC06",
                "description": "This payment failed because the payer's account was blocked."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "This payment has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "This payment has been cancelled because the payer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "DDICA-4DDICA-5DDICA-6",
                "description": "This payment has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "AUDDIS-2AUDDIS-B",
                "description": "This payment has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "AUDDIS-5",
                "description": "This payment has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "AUDDIS-3AUDDIS-C",
                "description": "This payment has been cancelled because the customer requested their bank transfer their Direct Debit to a new account but the bank did not send GoCardless the new bank details."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "bacs",
                "reason_code": "AUDDIS-FAUDDIS-GAUDDIS-N",
                "description": "This payment has been cancelled because the bank account for its mandate does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "ARUDD-5ARUDD-EARUDD-Y",
                "description": "This payment has been cancelled because the bank details for its mandate are not valid."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ARUDD-1",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "PAYMENT_INFORMATION-0238",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "MANDATE_INFORMATION-0232MANDATE_INFORMATION-0233MANDATE_INFORMATION-0234",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "INFORMATION_LIST-0253INFORMATION_LIST-0257",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC03",
                "description": "This payment has been cancelled because the customer requested their bank transfer their Direct Debit to a new account but the bank did not send GoCardless the new bank details."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-MS01",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC04",
                "description": "The bank account for this payment has been closed. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC05NEGATIVE_ACKNOWLEDGEMENT-AC05",
                "description": "The bank account specified does not exist. The mandate will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AG01",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-BE05",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-900PAYMENT_STATUS_REPORT-902PAYMENT_STATUS_REPORT-912PAYMENT_STATUS_REPORT-1023PAYMENT_STATUS_REPORT-2014PAYMENT_STATUS_REPORT-2017PAYMENT_STATUS_REPORT-2018PAYMENT_STATUS_REPORT-2019PAYMENT_STATUS_REPORT-2020PAYMENT_STATUS_REPORT-2034PAYMENT_STATUS_REPORT-0518PAYMENT_STATUS_REPORT-0567PAYMENT_STATUS_REPORT-0573",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-905",
                "description": "This payment has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-910",
                "description": "This payment was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-918PAYMENT_STATUS_REPORT-921",
                "description": "This payment has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-915",
                "description": "This payment has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-917PAYMENT_STATUS_REPORT-920",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "15",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "becs",
                "reason_code": "2",
                "description": "This payment has been cancelled because the bank account for its mandate does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "payment_stopped",
                "scheme": "becs",
                "reason_code": "2",
                "description": "The payment was stopped by the payer or their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "3",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "4",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "DEN",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "789",
                "description": "An error was received from the banks while setting up the mandate for this payment."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "UDUNAUT",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs",
                "reason_code": "CBC",
                "description": "This payment has been cancelled because its mandate was cancelled."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "RC02",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "becs",
                "reason_code": "MD01",
                "description": "This payment has been cancelled because the customer disputes authorising its mandate."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "AC04",
                "description": "This payment has been cancelled because the bank account it was going to be taken from has been closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "MD07",
                "description": "This payment was cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "AC01",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs",
                "reason_code": "NARR",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "15",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pay_to",
                "reason_code": "3",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "DEN",
                "description": "This payment has been cancelled because the bank details for its mandate are incorrect."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_expired",
                "scheme": "None",
                "reason_code": "None",
                "description": "The mandate expired before the payment could be collected."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-903PAYMENT_STATUS_REPORT-908PAYMENT_STATUS_REPORT-914",
                "description": "The customer's bank wasn't able to pay the Direct Debit. This is almost always due to insufficient funds but is occasionally used as a catch-all for other failures."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "PAYER_MANDATE_CANCELLED",
                "description": "This payment was canceled because the customer cancelled the mandate at their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_suspended_by_payer",
                "scheme": "pay_to",
                "reason_code": "SBP",
                "description": "The mandate for this payment was suspended by the payer."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "MERCHANT_MANDATE_CANCELLED",
                "description": "The mandate for this payment was cancelled at your request."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "MANDATE_EXPIRED",
                "description": "The mandate expired before the payment could be collected."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "The payment was cancelled because of an ODFI return request."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16",
                "description": "This payment has been cancelled because the payer's bank account is frozen. ACH authorization will be cancelled."
            },
            {
                "origin": "gocardless",
                "cause": "initial_one_off_payment_failed",
                "scheme": "None",
                "reason_code": "None",
                "description": "This mandate has been cancelled because the initial faster payment failed"
            }
        ]
    }
],
"""

from __future__ import annotations
from typing import Annotated, Literal, Union, List
from pydantic import BaseModel, Field, RootModel


class PaymentSurchargeFeeDebited(BaseModel):
    action: Literal["surcharge_fee_debited"]
    description: str
    details: PaymentSurchargeFeeDebitedSurchargeFeeDebitedDetail


class PaymentChargebackCancelled(BaseModel):
    action: Literal["chargeback_cancelled"]
    description: str
    details: PaymentChargebackCancelledPaymentConfirmedDetail


class PaymentCustomerApprovalGranted(BaseModel):
    action: Literal["customer_approval_granted"]
    description: str
    details: PaymentCustomerApprovalGrantedCustomerApprovalGrantedDetail


class PaymentLateFailureSettled(BaseModel):
    action: Literal["late_failure_settled"]
    description: str
    details: PaymentLateFailureSettledLateFailureSettledDetail


class PaymentChargedBack(BaseModel):
    action: Literal["charged_back"]
    description: str
    details: List[
        Annotated[
            Union[
                PaymentChargedBackAuthorisationDisputedDetail,
                PaymentChargedBackRefundRequestedDetail,
                PaymentChargedBackMandateCancelledDetail,
                PaymentChargedBackReturnOnOdfiRequestDetail,
                PaymentChargedBackOtherDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PaymentCustomerApprovalDenied(BaseModel):
    action: Literal["customer_approval_denied"]
    description: str
    details: PaymentCustomerApprovalDeniedCustomerApprovalDeniedDetail


class PaymentResubmissionRequested(BaseModel):
    action: Literal["resubmission_requested"]
    description: str
    details: List[
        Annotated[
            Union[
                PaymentResubmissionRequestedPaymentRetriedDetail,
                PaymentResubmissionRequestedPaymentAutoretriedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PaymentFailed(BaseModel):
    action: Literal["failed"]
    description: str
    details: List[
        Annotated[
            Union[
                PaymentFailedReferToPayerDetail,
                PaymentFailedBankAccountClosedDetail,
                PaymentFailedInvalidBankDetailsDetail,
                PaymentFailedAuthorisationDisputedDetail,
                PaymentFailedReturnOnOdfiRequestDetail,
                PaymentFailedOtherDetail,
                PaymentFailedTestFailureDetail,
                PaymentFailedMandateCancelledDetail,
                PaymentFailedBankAccountTransferredDetail,
                PaymentFailedDirectDebitNotEnabledDetail,
                PaymentFailedAccountBlockedForAnyFinancialTransactionDetail,
                PaymentFailedInsufficientFundsDetail,
                PaymentFailedPaymentStoppedDetail,
                PaymentFailedBankDeclinedPaymentDetail,
                PaymentFailedDailyPaymentLimitReachedDetail,
                PaymentFailedInsufficientPaymentPermissionsDetail,
                PaymentFailedPaymentViolatedMandateParametersDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PaymentSubmitted(BaseModel):
    action: Literal["submitted"]
    description: str
    details: PaymentSubmittedPaymentSubmittedDetail


class PaymentConfirmed(BaseModel):
    action: Literal["confirmed"]
    description: str
    details: PaymentConfirmedPaymentConfirmedDetail


class PaymentCreated(BaseModel):
    action: Literal["created"]
    description: str
    details: List[
        Annotated[
            Union[
                PaymentCreatedPaymentCreatedDetail,
                PaymentCreatedInstalmentScheduleCreatedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PaymentChargebackSettled(BaseModel):
    action: Literal["chargeback_settled"]
    description: str
    details: PaymentChargebackSettledChargebackSettledDetail


class PaymentPaidOut(BaseModel):
    action: Literal["paid_out"]
    description: str
    details: PaymentPaidOutPaymentPaidOutDetail


class PaymentCancelled(BaseModel):
    action: Literal["cancelled"]
    description: str
    details: List[
        Annotated[
            Union[
                PaymentCancelledBankAccountClosedDetail,
                PaymentCancelledReferToPayerDetail,
                PaymentCancelledInvalidBankDetailsDetail,
                PaymentCancelledAuthorisationDisputedDetail,
                PaymentCancelledMandateCancelledDetail,
                PaymentCancelledOtherDetail,
                PaymentCancelledInstalmentScheduleCancelledDetail,
                PaymentCancelledPaymentCancelledDetail,
                PaymentCancelledBankAccountTransferredDetail,
                PaymentCancelledDirectDebitNotEnabledDetail,
                PaymentCancelledAccountBlockedForAnyFinancialTransactionDetail,
                PaymentCancelledPaymentStoppedDetail,
                PaymentCancelledMandateExpiredDetail,
                PaymentCancelledMandateSuspendedByPayerDetail,
                PaymentCancelledReturnOnOdfiRequestDetail,
                PaymentCancelledInitialOneOffPaymentFailedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class PaymentSurchargeFeeDebitedSurchargeFeeDebitedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["surcharge_fee_debited"]
    description: str


class PaymentChargebackCancelledPaymentConfirmedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_confirmed"]
    description: str


class PaymentCustomerApprovalGrantedCustomerApprovalGrantedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


class PaymentLateFailureSettledLateFailureSettledDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["late_failure_settled"]
    description: str


class PaymentChargedBackAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class PaymentChargedBackRefundRequestedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refund_requested"]
    scheme: str
    reason_code: str
    description: str


class PaymentChargedBackMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class PaymentChargedBackReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class PaymentChargedBackOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class PaymentCustomerApprovalDeniedCustomerApprovalDeniedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_denied"]
    description: str


class PaymentResubmissionRequestedPaymentRetriedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["payment_retried"]
    description: str


class PaymentResubmissionRequestedPaymentAutoretriedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payment_autoretried"]
    description: str


class PaymentFailedReferToPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedBankAccountClosedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedInvalidBankDetailsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedTestFailureDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["test_failure"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedDirectDebitNotEnabledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedAccountBlockedForAnyFinancialTransactionDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedInsufficientFundsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["insufficient_funds"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedPaymentStoppedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedBankDeclinedPaymentDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_declined_payment"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedDailyPaymentLimitReachedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["daily_payment_limit_reached"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedInsufficientPaymentPermissionsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["insufficient_payment_permissions"]
    scheme: str
    reason_code: str
    description: str


class PaymentFailedPaymentViolatedMandateParametersDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_violated_mandate_parameters"]
    scheme: str
    reason_code: str
    description: str


class PaymentSubmittedPaymentSubmittedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payment_submitted"]
    description: str


class PaymentConfirmedPaymentConfirmedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payment_confirmed"]
    description: str


class PaymentCreatedPaymentCreatedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["payment_created"]
    description: str


class PaymentCreatedInstalmentScheduleCreatedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["instalment_schedule_created"]
    description: str


class PaymentChargebackSettledChargebackSettledDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["chargeback_settled"]
    description: str


class PaymentPaidOutPaymentPaidOutDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["payment_paid_out"]
    description: str


class PaymentCancelledBankAccountClosedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledReferToPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledInvalidBankDetailsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledInstalmentScheduleCancelledDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_cancelled"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledPaymentCancelledDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["payment_cancelled"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledDirectDebitNotEnabledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledAccountBlockedForAnyFinancialTransactionDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledPaymentStoppedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledMandateExpiredDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledMandateSuspendedByPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_suspended_by_payer"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class PaymentCancelledInitialOneOffPaymentFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    scheme: str
    reason_code: str
    description: str


PaymentType = Annotated[
    Union[
        PaymentSurchargeFeeDebited,
        PaymentChargebackCancelled,
        PaymentCustomerApprovalGranted,
        PaymentLateFailureSettled,
        PaymentChargedBack,
        PaymentCustomerApprovalDenied,
        PaymentResubmissionRequested,
        PaymentFailed,
        PaymentSubmitted,
        PaymentConfirmed,
        PaymentCreated,
        PaymentChargebackSettled,
        PaymentPaidOut,
        PaymentCancelled,
    ],
    Field(..., discriminator="action"),
]

Payment = RootModel[PaymentType]
