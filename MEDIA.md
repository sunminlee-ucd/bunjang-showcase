# Brand Lens media capture notes

Captured on **19 October 2026** from the authenticated deployed application at https://bunjang-web-x5omgavbua-du.a.run.app/.

## Captured views

| View | What it shows | MP4 interval |
| --- | --- | --- |
| [Analysis controls](assets/01-analysis-controls.jpg) | Search terms, page/starting-point controls, resumption, and analysis filters | 0–5 seconds |
| [Observation summary](assets/02-observed-summary.jpg) | Existing sold/reserved counts and category summaries | 5–10 seconds |
| [Collection history](assets/03-collection-history.jpg) | Saved run dates and search terms | 10–15 seconds |
| [Cost calculator](assets/04-cost-calculator.jpg) | Empty product inputs, zero results, and displayed rate/shipping defaults | 15–20 seconds |

The screenshots are unretouched JPEG browser captures. The [MP4](assets/brand-lens-ui-walkthrough.mp4) and [GIF](assets/brand-lens-ui-walkthrough.gif) scale and pad the four stills for a consistent frame. They form a **silent navigation montage**, not a continuous screen recording or a timing/performance measurement.

## Data and interpretation

- The summary contains an existing observation sample for Rick Owens search variants. It is not a newly collected sample or a statement of current market conditions.
- History contains runs saved on earlier dates. Capture date, run date, listing-update time, and actual transaction date are different concepts.
- Sold and reserved are platform listing states. Counts do not establish total marketplace transactions; posted prices do not establish final payment amounts.
- The calculator contains no entered product, contact, or purchase data. Its displayed exchange rate and shipping charge are application defaults, not verified current quotations. Calculation results, tax treatment, translation, and PDF export were not tested.
- Selected interface aggregates are visible in the screenshots. The underlying listing dataset and complete product source remain private.
- The separate [visual similarity example](assets/image-similarity-demo.png) uses generated color patches. It is a code demo, not an application screenshot or marketplace test.

## Verification boundary

The capture session reused an existing local-browser login, viewed the analysis, cost, and history tabs, and opened one saved history entry. It did not start a new collection, submit a cloud job, delete records, change account settings, enter API keys, or export results.

The media demonstrates rendered UI and existing results. It does not independently validate the aggregate values, demonstrate live collection/retry/cancellation, certify cloud availability, or establish customer adoption or financial returns.

Media checks: four JPEGs decode; the 20-second H.264 MP4 fully decodes; the GIF contains 80 frames at a total duration of 20 seconds. Each scene was inspected in a contact sheet.
