import json

import pytest

from gocardless_events.models import Event
from gocardless_events.models.billing_request import (
    BillingRequest,
    BillingRequestCreated,
)

billing_request_created_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2021-04-08T17:01:06.000Z",
    "resource_type": "billing_requests",
    "action": "created",
    "details": {
        "origin": "api",
        "cause": "billing_request_created",
        "description": "This billing request has been created."
    },
    "metadata": {},
    "resource_metadata": {
        "order_dispatch_date": "2014-05-22"
    },
    "links": {
        "billing_request": "BRQ123"
    }
  }
}
"""

creditor_updated_gocardless_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2018-04-08T17:01:06.000Z",
    "resource_type": "creditors",
    "action": "updated",
    "links": {
        "creditor": "CR123"
    },
    "details": {
        "origin": "gocardless",
        "cause": "creditor_updated",
        "description": "This creditor has been updated.",
        "property": "fx_payout_currency"
    },
    "metadata": {}
  }
}
"""

export_started_gocardless_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2024-07-10T00:00:00.000Z",
    "resource_type": "exports",
    "action": "started",
    "links": {
        "export": "EX0000116MFWYM"
    },
    "details": {
        "origin": "gocardless",
        "cause": "export_started",
        "description": "Export started.",
        "type": "payout_transactions_reconciliation",
        "currency": "GBP"
    },
    "metadata": {}
  }
}
"""

instalment_schedule_payment_created_api_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "instalment_schedules",
    "action": "payment_created",
    "links": {
      "instalment_schedule": "IS123",
      "payment": "PM123"
    },
    "details": {
      "origin": "api",
      "cause": "payment_created",
      "description": "Payment created by an instalment schedule."
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    }
  }
}
"""

mandate_cancelled_bank_account_closed_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "mandates",
    "action": "cancelled",
    "details": {
      "origin": "bank",
      "cause": "bank_account_closed",
      "description": "The bank account for this mandate has been closed.",
      "scheme": "bacs",
      "reason_code": "ADDACS-B"
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "mandate": "MD123"
    }
  }
}
"""


mandate_cancelled_api_json = """
{
  "events": {
    "id": "EV456",
    "created_at": "2014-04-08T17:03:12.000Z",
    "resource_type": "mandates",
    "action": "cancelled",
    "details": {
      "origin": "api",
      "cause": "mandate_cancelled",
      "description": "The mandate was cancelled via an API call."
    },
    "metadata": {
      "cancellor_id": "some_id"
    },
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "mandate": "MD456"
    }
  }
}
"""

mandate_tranferred_bank_account_transferred_json = """
{
  "events": {
    "id": "EV789",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "mandates",
    "action": "transferred",
    "details": {
      "origin": "bank",
      "cause": "bank_account_transferred",
      "description": "The customer's bank account was transferred to a different bank or building society.",
      "scheme": "bacs",
      "reason_code": "AUDDIS-C"
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "mandate": "MD789",
      "previous_customer_bank_account": "BA123",
      "new_customer_bank_account": "BA456"
    }
  }
}
"""

payment_failed_bank_insufficient_funds_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "payments",
    "action": "failed",
    "details": {
      "origin": "bank",
      "cause": "insufficient_funds",
      "description": "The customer's account had insufficient funds to make this payment.",
      "scheme": "sepa_core",
      "reason_code": "AM04",
      "will_attempt_retry": false
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "payment": "PM123"
    }
  }
}
"""

payment_cancelled_bank_mandate_cancelled_json = """
{
  "events": {
    "id": "EV4567",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "payments",
    "action": "cancelled",
    "details": {
      "origin": "bank",
      "cause": "mandate_cancelled",
      "description": "The mandate for this payment was cancelled as the customer's bank account has been closed.",
      "scheme": "bacs",
      "reason_code": "ADDACS-B"
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "payment": "PM456",
      "parent_event": "EV789"
    }
  }
}
"""

payment_cancelled_api_json = """
{
  "events": {
    "id": "EV8901",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "payments",
    "action": "cancelled",
    "details": {
      "origin": "api",
      "cause": "payment_cancelled",
      "description": "Payment cancelled."
    },
    "metadata": {
      "cancellor_id": "some_id"
    },
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "payment": "PM789"
    }
  }
}
"""

payment_confirmed_gocardless_json = """
{
  "events": {
    "id": "EV2345",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "payments",
    "action": "confirmed",
    "details": {
      "origin": "gocardless",
      "cause": "payment_confirmed",
      "description": "Payment confirmed"
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "payment": "PM999"
    }
  }
}
"""

payout_paid_gocardless_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "payouts",
    "action": "paid",
    "details": {
      "origin": "gocardless",
      "cause": "payout_paid",
      "description": "Payout sent"
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "payout": "PO123"
    }
  }
}
"""

refund_created_api_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "refunds",
    "action": "created",
    "details": {
      "origin": "api",
      "cause": "payment_refunded",
      "description": "The refund has been created, and will be submitted in the next batch."
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    },
    "links": {
      "refund": "RF123"
    }
  }
}
"""

scheme_identifier_activated_gocardless_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2023-04-08T17:01:06.000Z",
    "resource_type": "scheme_identifiers",
    "action": "activated",
    "links": {
      "scheme_identifier": "SU222"
    },
    "details": {
      "origin": "gocardless",
      "cause": "scheme_identifier_activated",
      "description": "This scheme identifier has been activated."
    },
    "metadata": {}
  }
}
"""

subscription_payment_created_api_json = """
{
  "events": {
    "id": "EV123",
    "created_at": "2014-04-08T17:01:06.000Z",
    "resource_type": "subscriptions",
    "action": "payment_created",
    "links": {
      "subscription": "SB123",
      "payment": "PM123"
    },
    "details": {
      "origin": "api",
      "cause": "payment_created",
      "description": "Payment created by a subscription."
    },
    "metadata": {},
    "resource_metadata": {
      "order_dispatch_date": "2014-05-22"
    }
  }
}
"""


def _extract_event(payload: str) -> str:
    event = json.loads(payload)["events"]
    return json.dumps(event)


def test_specific_event() -> None:
    event = _extract_event(billing_request_created_json)
    BillingRequestCreated.model_validate_json(event)


def test_resource_event() -> None:
    event = _extract_event(billing_request_created_json)
    BillingRequest.model_validate_json(event)


@pytest.mark.parametrize(
    "payload",
    [
        billing_request_created_json,
        creditor_updated_gocardless_json,
        export_started_gocardless_json,
        instalment_schedule_payment_created_api_json,
        mandate_cancelled_bank_account_closed_json,
        mandate_cancelled_api_json,
        mandate_tranferred_bank_account_transferred_json,
        payment_failed_bank_insufficient_funds_json,
        payment_cancelled_bank_mandate_cancelled_json,
        payment_cancelled_api_json,
        payment_confirmed_gocardless_json,
        payout_paid_gocardless_json,
        refund_created_api_json,
        scheme_identifier_activated_gocardless_json,
        subscription_payment_created_api_json,
    ],
    ids=[
        "billing_request_created",
        "creditor_updated",
        "export_started",
        "instalment_schedule_payment_created",
        "mandate_cancelled_bank_account_closed",
        "mandate_cancelled_api",
        "mandate_transferred_bank_account",
        "payment_failed_insufficient_funds",
        "payment_cancelled_mandate_cancelled",
        "payment_cancelled_api",
        "payment_confirmed",
        "payout_paid",
        "refund_created",
        "scheme_identifier_activated",
        "subscription_payment_created",
    ],
)
def test_parent_event(payload: str) -> None:
    event = _extract_event(payload)
    Event.model_validate_json(event)
