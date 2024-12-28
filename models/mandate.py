"""
"mandates": [
    {
        "action": "reinstated",
        "description": "The mandate has become active again after it was cancelled or expired. This can be due to the customer's bank wishing to undo a cancellation or expiry notice they sent or because the mandate was successfully reinstated via the reinstate endpoint.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_reinstated",
                "description": "The time window after submission for the banks to refuse a mandate has ended without any errors being received so this mandate is now active."
            },
            {
                "origin": "bank",
                "cause": "mandate_reinstated",
                "description": "A cancelled mandate has been re-instated by the customer's bank."
            }
        ]
    },
    {
        "action": "customer_approval_granted",
        "description": "The mandate required additional approval from the customer (e.g. permission from a second signatory) and that approval has been granted.",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_granted",
                "description": "The customer has granted approval for this mandate"
            }
        ]
    },
    {
        "action": "expired",
        "description": "No collection attempts were made against the mandate within the dormancy period of your service user number. As a result it has expired and no further collections can be taken against it. If you wish to continue taking payments from this customer you should request their permission and use the reinstate endpoint.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_expired",
                "description": "The mandate is being marked as expired because no payments have been collected against it for the dormancy period of your service user number. If you have access to the mandate reinstation API endpoint you can use this to attempt to set this mandate up again."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "description": "The mandate has expired."
            }
        ]
    },
    {
        "action": "resubmission_requested",
        "description": "A request to resubmit the mandate was made by the mandate reinstate endpoint.",
        "details": [
            {
                "origin": "api",
                "cause": "resubmission_requested",
                "description": "An attempt to reinstate this mandate was requested."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "description": "The customer's bank account was transferred to a different bank or building society."
            }
        ]
    },
    {
        "action": "failed",
        "description": "The mandate could not be set up generally because the specified bank account does not accept Direct Debit payments or is closed.",
        "details": [
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R14ACH_RETURN-R15",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-C01ACH_RETURN-C02ACH_RETURN-C03ACH_RETURN-C06ACH_RETURN-C07NOTIFICATION_OF_CHANGE-C01NOTIFICATION_OF_CHANGE-C02NOTIFICATION_OF_CHANGE-C03NOTIFICATION_OF_CHANGE-C06NOTIFICATION_OF_CHANGE-C07NOTIFICATION_OF_CHANGE-C08NOTIFICATION_OF_CHANGE-C09",
                "description": "This mandate was cancelled due to a Notification of Change indicating the customer's account number or branch number was incorrect please contact the customer."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-C05NOTIFICATION_OF_CHANGE-C05",
                "description": "This mandate was cancelled due to a Notification of Change indicating the customer's selected account type was incorrect please contact the customer."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R02ACH_RETURN-R12",
                "description": "The bank account for this mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07",
                "description": "The mandate was already cancelled."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07ACH_RETURN-R10ACH_RETURN-R29ACH_RETURN-R51",
                "description": "The mandate was already cancelled."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R03ACH_RETURN-R04ACH_RETURN-R13ACH_RETURN-R28ACH_RETURN-R82",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16ACH_RETURN-R20ACH_RETURN-R34",
                "description": "The bank account does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R06ACH_RETURN-R08ACH_RETURN-R16ACH_RETURN-R20ACH_RETURN-R29ACH_RETURN-R31ACH_RETURN-R26",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R85",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "The mandate has been cancelled because a payment under it was charged back."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R08ACH_RETURN-R11",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "ARUDD-5ARUDD-YARUDD-E",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "bacs",
                "reason_code": "ARUDD-6",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "AUDDIS-2",
                "description": "The bank account for this mandate has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "bacs",
                "reason_code": "AUDDIS-5",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "AUDDIS-B",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "bacs",
                "reason_code": "AUDDIS-FAUDDIS-GAUDDIS-N",
                "description": "The bank account does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "AUDDIS-3AUDDIS-C",
                "description": "The customer's bank account was transferred to a different bank or building society."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "15",
                "description": "The bank account specified does not exist."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "becs",
                "reason_code": "2",
                "description": "The bank account does not support Direct Debit."
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
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "DEN",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "becs",
                "reason_code": "789",
                "description": "There was an internal error processing this mandate."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "RC02",
                "description": "The bank account specified does not exist."
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
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "MD07",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "AC01",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs",
                "reason_code": "NARR",
                "description": "There was an internal error processing this mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pay_to",
                "reason_code": "MD20",
                "description": "The mandate has expired."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pay_to",
                "reason_code": "NARRUNKN",
                "description": "There was an internal error processing this mandate."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC05NEGATIVE_ACKNOWLEDGEMENT-AC05",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC04",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC03",
                "description": "The customer's bank account was transferred to a different bank or building society."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AG01",
                "description": "This mandate was cancelled by the customer or their bank."
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
                "cause": "refer_to_payer",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AM04DISHONOUR-MS01",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-900PAYMENT_STATUS_REPORT-902PAYMENT_STATUS_REPORT-912PAYMENT_STATUS_REPORT-1023PAYMENT_STATUS_REPORT-2014PAYMENT_STATUS_REPORT-2017PAYMENT_STATUS_REPORT-2018PAYMENT_STATUS_REPORT-2019PAYMENT_STATUS_REPORT-2020PAYMENT_STATUS_REPORT-2034PAYMENT_STATUS_REPORT-0518PAYMENT_STATUS_REPORT-0567PAYMENT_STATUS_REPORT-0573",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-905",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-910",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-914",
                "description": "The account holder name may be different than that associated with the electronic transaction to run."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "sepa_core",
                "reason_code": "AC01",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            }
        ]
    },
    {
        "action": "submitted",
        "description": "The mandate has been submitted to the banks and should become active in a few days unless the bank declines the request.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_submitted",
                "description": "The mandate has been submitted to the banks."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "description": "The customer's bank account was transferred to a different bank or building society."
            }
        ]
    },
    {
        "action": "transferred",
        "description": "The mandate has been transferred to a different bank account either using a bank switching service (where it is supported) or with help from GoCardless Support when a customer asks to change their bank account (we can make the switch after verifying the details). The event will includelinks[previous_customer_bank_account]andlinks[new_customer_bank_account]. When using a bank switching service the mandate may have been submitted again depending on how the involved banks handled the transfer.",
        "details": [
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "description": "The customer's bank account was transferred to a different bank or building society."
            },
            {
                "origin": "api",
                "cause": "mandate_transferred",
                "description": "This mandate was transferred to a new bank account through GoCardless."
            }
        ]
    },
    {
        "action": "consumed",
        "description": "The mandate has been used to create a payment and has now been consumed. It cannot be used again.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_consumed",
                "description": "The mandate has been used to create a payment and has now been consumed. It cannot be used again."
            }
        ]
    },
    {
        "action": "customer_approval_skipped",
        "description": "The mandate originally was believed to require additional approval from the customer (e.g. permission from a second signatory) but approval has been skipped (for example because the mandate was erroneously marked as needing a second signature).",
        "details": [
            {
                "origin": "customer",
                "cause": "customer_approval_skipped",
                "description": "The customer has skipped approval for this mandate"
            }
        ]
    },
    {
        "action": "active",
        "description": "The mandate has been successfully set up by the customer's bank.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_activated",
                "description": "The time window after submission for the banks to refuse a mandate has ended without any errors being received so this mandate is now active."
            },
            {
                "origin": "bank",
                "cause": "mandate_activated",
                "description": "The customer's bank has confirmed that this mandate has been activated."
            }
        ]
    },
    {
        "action": "created",
        "description": "The mandate has been created.",
        "details": [
            {
                "origin": "api",
                "cause": "mandate_created",
                "description": "Mandate created via the API."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_created",
                "description": "Mandate created by a bulk change"
            }
        ]
    },
    {
        "action": "blocked",
        "description": "The mandate has been blocked because the customer's details matched against an entry in either our global blocklist or the blocklist populated by you. This mandate cannot be unblocked and no payments can be created against it. If you still wish to collect payments from this customer you will need to remove their details from any blocks you have created and ask them to set up a new mandate. If you contacted GoCardless to block the customer's details you will need to make a request to unblock them.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "mandate_blocked",
                "description": "The mandate has been blocked because the customer's details matched against an entry in the blocklist populated by you."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_blocked_by_gocardless",
                "description": "The mandate has been blocked because the customer's details matched against an entry in our global blocklist."
            }
        ]
    },
    {
        "action": "replaced",
        "description": "The mandate has been cancelled and replaced by a new mandate (for example because the creditor has moved to a new Service User Number). The event will includelinks[new_mandate]with the ID of the new mandate.",
        "details": [
            {
                "origin": "gocardless",
                "cause": "scheme_identifier_changed",
                "description": "The creditor has changed to a different scheme identifier so this mandate has been cancelled and replaced by a new one."
            }
        ]
    },
    {
        "action": "cancelled",
        "description": "The mandate has been cancelled either by the customer through their bank or this API or automatically when their bank account is closed.",
        "details": [
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R14ACH_RETURN-R15",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R02ACH_RETURN-R12",
                "description": "The bank account for this mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R07",
                "description": "The mandate was cancelled at a bank branch."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R06ACH_RETURN-R08ACH_RETURN-R10ACH_RETURN-R11ACH_RETURN-R29ACH_RETURN-R31ACH_RETURN-R51",
                "description": "The customer disputes having authorised you to set up a mandate with them."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R03ACH_RETURN-R04ACH_RETURN-R13ACH_RETURN-R28ACH_RETURN-R82",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R16ACH_RETURN-R34",
                "description": "The bank account does not support Direct Debit."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R05ACH_RETURN-R06ACH_RETURN-R08ACH_RETURN-R16ACH_RETURN-R20ACH_RETURN-R29ACH_RETURN-R26",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "return_on_odfi_request",
                "scheme": "ach",
                "reason_code": "ACH_RETURN-R06",
                "description": "mandate_cancelled_because_payment_charged_back"
            },
            {
                "origin": "api",
                "cause": "mandate_cancelled",
                "scheme": "None",
                "reason_code": "None",
                "description": "The mandate was cancelled at your request."
            },
            {
                "origin": "api",
                "cause": "bank_account_closed",
                "scheme": "None",
                "reason_code": "None",
                "description": "The customer's account was disabled at your request."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ADDACS-0ADDACS-1",
                "description": "The mandate was cancelled at a bank branch."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ADDACS-2",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "bank_account_transferred",
                "scheme": "bacs",
                "reason_code": "ADDACS-3ADDACS-CADDACS-E",
                "description": "The customer's bank account was transferred to a different bank or building society."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ADDACS-B",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "authorisation_disputed",
                "scheme": "bacs",
                "reason_code": "ADDACS-D",
                "description": "The customer has disputed the amount of notice specified on the mandate via their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "bacs",
                "reason_code": "ARUDD-1",
                "description": "The mandate was cancelled at a bank branch."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-2",
                "description": "This mandate has been cancelled because a payment against it indicated that the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "bacs",
                "reason_code": "ARUDD-B",
                "description": "The bank account for this mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "bacs",
                "reason_code": "ARUDD-6",
                "description": "This mandate has been cancelled because a payment under it failed."
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
                "cause": "invalid_bank_details",
                "scheme": "sepa_core",
                "reason_code": "AC01BE06",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "AC04",
                "description": "The bank account for this mandate has been closed. Any subscriptions and pending payment will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "sepa_core",
                "reason_code": "AG01AC06",
                "description": "The bank account for this mandate does not support SEPA direct debit. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "account_blocked_for_any_financial_transaction",
                "scheme": "sepa_core",
                "reason_code": "AC06",
                "description": "The bank account for this mandate was blocked. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "sepa_core",
                "reason_code": "MD01",
                "description": "A payment under this mandate failed indicating that the mandate has been cancelled at the customer's bank. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "sepa_core",
                "reason_code": "MD07",
                "description": "This mandate has been cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "MANDATE_INFORMATION-0232MANDATE_INFORMATION-0233MANDATE_INFORMATION-0234",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "betalingsservice",
                "reason_code": "INFORMATION_LIST-0257",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "direct_debit_not_enabled",
                "scheme": "becs",
                "reason_code": "2",
                "description": "The bank account does not support Direct Debit."
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
                "cause": "other",
                "scheme": "becs",
                "reason_code": "2",
                "description": "This mandate has been cancelled because a payment under it failed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "3",
                "description": "The bank account for this mandate has been closed."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "4",
                "description": "This bank account has been closed as the customer is deceased."
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
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "RC02",
                "description": "The bank account specified does not exist."
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
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs",
                "reason_code": "MD07",
                "description": "This bank account has been closed as the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs",
                "reason_code": "AC01",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "becs",
                "reason_code": "NARR",
                "description": "There was an internal error processing this mandate."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pay_to",
                "reason_code": "MD16MS02",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pay_to",
                "reason_code": "MD17",
                "description": "The mandate was cancelled at your request."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pay_to",
                "reason_code": "MD21",
                "description": "The mandate has been cancelled due to fraud."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "pay_to",
                "reason_code": "MSUCMCFCMCOC",
                "description": "The mandate has been suspended."
            },
            {
                "origin": "bank",
                "cause": "refer_to_payer",
                "scheme": "pay_to",
                "reason_code": "UNKN",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "AC02",
                "description": "This mandate was cancelled due to a Notification of Change indicating the customer's account number or branch number was incorrect please contact the customer."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pay_to",
                "reason_code": "AC06",
                "description": "The account associated with the customer's mandate is blocked."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pay_to",
                "reason_code": "AC13",
                "description": "This mandate was cancelled due to a Notification of Change indicating the customer's selected account type was incorrect please contact the customer."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pay_to",
                "reason_code": "AC04AC05",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pay_to",
                "reason_code": "MD07",
                "description": "This mandate has been cancelled because the customer is deceased."
            },
            {
                "origin": "bank",
                "cause": "other",
                "scheme": "pay_to",
                "reason_code": "SL11SL12",
                "description": "The customer's account is not permitted to send funds to the beneficiary."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC04",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "becs_nz",
                "reason_code": "DISHONOUR-AC05NEGATIVE_ACKNOWLEDGEMENT-AC05",
                "description": "The bank account specified does not exist. Any subscriptions and pending payments will also be cancelled."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-905",
                "description": "The customer's account was closed at their bank."
            },
            {
                "origin": "bank",
                "cause": "bank_account_closed",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-910",
                "description": "This bank account has been closed as the customer is deceased."
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
                "cause": "mandate_cancelled",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-917PAYMENT_STATUS_REPORT-920",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "bank",
                "cause": "invalid_bank_details",
                "scheme": "pad",
                "reason_code": "PAYMENT_STATUS_REPORT-0518PAYMENT_STATUS_REPORT-0567",
                "description": "The specified bank account does not exist or was closed."
            },
            {
                "origin": "bank",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "PAYER_MANDATE_CANCELLED",
                "description": "This mandate was cancelled by the customer or their bank."
            },
            {
                "origin": "gocardless",
                "cause": "mandate_cancelled",
                "scheme": "faster_payments",
                "reason_code": "MERCHANT_MANDATE_CANCELLED",
                "description": "The mandate was cancelled at your request."
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


class MandateReinstated(BaseModel):
    action: Literal["reinstated"]
    description: str
    details: MandateReinstatedMandateReinstatedDetail


class MandateCustomerApprovalGranted(BaseModel):
    action: Literal["customer_approval_granted"]
    description: str
    details: MandateCustomerApprovalGrantedCustomerApprovalGrantedDetail


class MandateExpired(BaseModel):
    action: Literal["expired"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateExpiredMandateExpiredDetail,
                MandateExpiredMandateCancelledDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateResubmissionRequested(BaseModel):
    action: Literal["resubmission_requested"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateResubmissionRequestedResubmissionRequestedDetail,
                MandateResubmissionRequestedBankAccountTransferredDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateFailed(BaseModel):
    action: Literal["failed"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateFailedBankAccountClosedDetail,
                MandateFailedReferToPayerDetail,
                MandateFailedMandateCancelledDetail,
                MandateFailedAuthorisationDisputedDetail,
                MandateFailedInvalidBankDetailsDetail,
                MandateFailedDirectDebitNotEnabledDetail,
                MandateFailedOtherDetail,
                MandateFailedReturnOnOdfiRequestDetail,
                MandateFailedBankAccountTransferredDetail,
                MandateFailedPaymentStoppedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateSubmitted(BaseModel):
    action: Literal["submitted"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateSubmittedMandateSubmittedDetail,
                MandateSubmittedBankAccountTransferredDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateTransferred(BaseModel):
    action: Literal["transferred"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateTransferredBankAccountTransferredDetail,
                MandateTransferredMandateTransferredDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateConsumed(BaseModel):
    action: Literal["consumed"]
    description: str
    details: MandateConsumedMandateConsumedDetail


class MandateCustomerApprovalSkipped(BaseModel):
    action: Literal["customer_approval_skipped"]
    description: str
    details: MandateCustomerApprovalSkippedCustomerApprovalSkippedDetail


class MandateActive(BaseModel):
    action: Literal["active"]
    description: str
    details: MandateActiveMandateActivatedDetail


class MandateCreated(BaseModel):
    action: Literal["created"]
    description: str
    details: MandateCreatedMandateCreatedDetail


class MandateBlocked(BaseModel):
    action: Literal["blocked"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateBlockedMandateBlockedDetail,
                MandateBlockedMandateBlockedByGocardlessDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateReplaced(BaseModel):
    action: Literal["replaced"]
    description: str
    details: MandateReplacedSchemeIdentifierChangedDetail


class MandateCancelled(BaseModel):
    action: Literal["cancelled"]
    description: str
    details: List[
        Annotated[
            Union[
                MandateCancelledBankAccountClosedDetail,
                MandateCancelledMandateCancelledDetail,
                MandateCancelledAuthorisationDisputedDetail,
                MandateCancelledInvalidBankDetailsDetail,
                MandateCancelledDirectDebitNotEnabledDetail,
                MandateCancelledReferToPayerDetail,
                MandateCancelledReturnOnOdfiRequestDetail,
                MandateCancelledBankAccountTransferredDetail,
                MandateCancelledAccountBlockedForAnyFinancialTransactionDetail,
                MandateCancelledPaymentStoppedDetail,
                MandateCancelledOtherDetail,
                MandateCancelledInitialOneOffPaymentFailedDetail,
            ],
            Field(..., discriminator="cause"),
        ]
    ]


class MandateReinstatedMandateReinstatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_reinstated"]
    description: str


class MandateCustomerApprovalGrantedCustomerApprovalGrantedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


class MandateExpiredMandateExpiredDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    description: str


class MandateExpiredMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    description: str


class MandateResubmissionRequestedResubmissionRequestedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["resubmission_requested"]
    description: str


class MandateResubmissionRequestedBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateFailedBankAccountClosedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedReferToPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedInvalidBankDetailsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedDirectDebitNotEnabledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class MandateFailedPaymentStoppedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class MandateSubmittedMandateSubmittedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_submitted"]
    description: str


class MandateSubmittedBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateTransferredBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    description: str


class MandateTransferredMandateTransferredDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["mandate_transferred"]
    description: str


class MandateConsumedMandateConsumedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_consumed"]
    description: str


class MandateCustomerApprovalSkippedCustomerApprovalSkippedDetail(BaseModel):
    origin: Literal["customer"]
    cause: Literal["customer_approval_skipped"]
    description: str


class MandateActiveMandateActivatedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_activated"]
    description: str


class MandateCreatedMandateCreatedDetail(BaseModel):
    origin: Literal["api"]
    cause: Literal["mandate_created"]
    description: str


class MandateBlockedMandateBlockedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_blocked"]
    description: str


class MandateBlockedMandateBlockedByGocardlessDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["mandate_blocked_by_gocardless"]
    description: str


class MandateReplacedSchemeIdentifierChangedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["scheme_identifier_changed"]
    description: str


class MandateCancelledBankAccountClosedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledMandateCancelledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledAuthorisationDisputedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledInvalidBankDetailsDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledDirectDebitNotEnabledDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledReferToPayerDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledReturnOnOdfiRequestDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledBankAccountTransferredDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledAccountBlockedForAnyFinancialTransactionDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledPaymentStoppedDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledOtherDetail(BaseModel):
    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


class MandateCancelledInitialOneOffPaymentFailedDetail(BaseModel):
    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    scheme: str
    reason_code: str
    description: str


MandateType = Annotated[
    Union[
        MandateReinstated,
        MandateCustomerApprovalGranted,
        MandateExpired,
        MandateResubmissionRequested,
        MandateFailed,
        MandateSubmitted,
        MandateTransferred,
        MandateConsumed,
        MandateCustomerApprovalSkipped,
        MandateActive,
        MandateCreated,
        MandateBlocked,
        MandateReplaced,
        MandateCancelled,
    ],
    Field(..., discriminator="action"),
]

Mandate = RootModel[MandateType]
