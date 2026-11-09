# Worked scenario — seo-structured-data-engineer

## Appropriate request
Task: add valid Product and Offer structured data to a real product page.

## Near-miss request
Not this task: brainstorm blog topics.

## Domain-specific approach
Map visible product name, currency, seller, availability and price to source fields. Example shape: {\"@context\":\"https://schema.org\",\"@type\":\"Product\",\"name\":\"Verified product name\",\"offers\":{\"@type\":\"Offer\",\"priceCurrency\":\"BRL\",\"price\":\"149.90\"}}. This is illustrative; never assert details without real page data. Validate server-rendered JSON-LD and known rich-result requirements.

## Acceptance evidence
Typed mapping, parser output, missing real facts, eligibility limitations.

This is an example, not a completed runtime test. Do not claim real test results without evidence.
