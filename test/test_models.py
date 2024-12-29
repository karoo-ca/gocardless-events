from gocardless_events.models import Event
from gocardless_events.models.billing_request import (
    BillingRequest,
    BillingRequestCreated,
)

billing_request_created_json = """{
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


def test_specific_event() -> None:
    BillingRequestCreated.model_validate_json(billing_request_created_json)


def test_resource_event() -> None:
    BillingRequest.model_validate_json(billing_request_created_json)


def test_parent_event() -> None:
    Event.model_validate_json(billing_request_created_json)
