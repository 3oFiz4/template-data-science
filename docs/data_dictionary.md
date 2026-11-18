# Data Dictionary

Document column meanings, types, known data quirks, and agreed-upon edge cases here.

| Column | Type | Description | Known Quirks / Edge Cases |
| :--- | :--- | :--- | :--- |
| `example_id` | `string` | Unique record identifier | None |
| `created_at` | `datetime` | Event timestamp (UTC) | Rows before `2026-03-01` may have null `country` |
| `rev_net_adj` | `float` | Net revenue after refunds | Negative values indicate full chargebacks |
