directory structure:

```
docs
├── billing_request
│   ├── bank_authorisation_authorised.html
│   ├── bank_authorisation_denied.html
│   └── ...
├── creditor
│   ├── account_auto_frozen.html
│   ├── account_auto_frozen_reverted.html
│   └── ...
└── ...
…
```

input:

file path: {{ resource_type }}/{{ action }}

```html
<h3><code>{{ action }}</code></h3>
<p>{{ description }}</p>
<table>
  <thead>
    <tr>
      <th>{{ key1 }}</th>
      <th>{{ key2 }}</th>
      <th>...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{{ key1_value1 }}</td>
      <td>{{ key2_value1 }}</td>
      <td>...</td>
    </tr>
    <tr>
      <td>{{ key1_value2 }}</td>
      <td>{{ key2_value2 }}</td>
      <td>...</td>
    </tr>
    ...
  </tbody>
</table>
```

output:

```json
{
  "{{ resource_type }}s": [
    {
      "action": "{{ action }}",
      "description": "{{ description }}",
      "details": [
        {
          "{{ key1 }}": "{{ key1_value1 }}",
          "{{ key2 }}": "{{ key2_value1 }}",
          ...
        },
        {
          "{{ key1 }}": "{{ key1_value2 }}",
          "{{ key2 }}": "{{ key2_value2 }}",
          ...
        },
        ...
      ]
    },
    ...
  },
  ...
}
``
```
