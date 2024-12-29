From [GoCardless' docs](https://developer.gocardless.com/api-reference#overview-backwards-compatibility)

> **Backwards Compatibility**

> The following changes are considered backwards compatible:
>
> - Adding new API endpoints
> - Adding new properties to the responses from existing API endpoints
> - Reordering properties returned from existing API endpoints
> - Adding optional request parameters to existing API endpoints
> - Altering the format or length of IDs
> - These strings will never exceed 255 characters, but you should be able to handle anything up to that length
> - Altering the message attributes returned by validation failures / other errors
> - The number of and duration between retries for failed webhooks
> - The behaviour of Scenario Simulators
> - Sending webhooks for new event types
