#!/usr/bin/env python3
"""
Coverage numbers for the Punjabi captions proof.

WARNING: one figure below (189,235 / 29.1%) is still from a secondary
summary found Nov 3, 2026 and could NOT be verified Nov 5, 2026.
Verify it at Statistics Canada before any public use. This script prints
the figures AND their verification status, so an unverified figure can
never be mistaken for a verified one. Verified Nov 5, 2026: Brampton
mother tongue 141,005 (23.7%) and Canada Punjabi speakers 942,000.

Run: python3 src/coverage.py
"""

FIGURES = [
    {
        "measure": "Brampton, Punjabi mother tongue (2021 Census)",
        "value": 141005,
        "share": 0.237,
        "source": "City of Brampton Census Bulletin #3 (Oct 2022), compiling Statistics Canada 2021 Census: '141,005 individuals reported Punjabi as mother tongue, accounting for 23.7 per cent' (single-response basis)",
        "verified_at_primary_source": True,
    },
    {
        "measure": "Brampton, people who could speak Punjabi (2021 Census)",
        "value": 189235,
        "share": 0.291,
        "source": "Secondary summary, Nov 3, 2026 — NOT found in Brampton Census Bulletin #3; that bulletin instead gives 114,145 (17.54%) speaking Punjabi most often at home. Do not use 189,235 / 29.1% until found at Statistics Canada.",
        "verified_at_primary_source": False,
    },
    {
        "measure": "Canada, Punjabi speakers (2021 Census)",
        "value": 942000,
        "share": None,
        "source": "Statistics Canada, The Daily, Jan 22, 2025: 'the languages other than English and French with the most speakers in Canada were Spanish (1.2 million), Mandarin (987,000), Punjabi (942,000) and Arabic (838,000)'",
        "verified_at_primary_source": True,
    },
]

def main():
    print("Coverage — Punjabi in Brampton")
    print("=" * 40)
    for f in FIGURES:
        share = f" ({f['share']:.1%})" if f["share"] is not None else ""
        print(f"\n{f['measure']}: {f['value']:,}{share}")
        print(f"  Source: {f['source']}")
        print(f"  Verified at primary source: {f['verified_at_primary_source']}")
    print("\nZoom, translated captions (page updated Nov 3, 2026):")
    print("  Punjabi listed: False")
    print("  Hindi, Bengali, Tamil, Telugu listed: True")
    print("  Source: Zoom Support, translated captions page (fetched Nov 3, 2026)")
    print("\nConclusion, in numbers:")
    print("  A language with 141,005 mother-tongue speakers in Brampton alone")
    print("  (23.7%, 2021 Census) and 942,000 speakers across Canada,")
    print("  is absent from a caption list that already includes")
    print("  comparable languages. That is the falsifying row, in numbers.")
    print("  (The 189,235 / 29.1% 'could speak Punjabi' figure is still")
    print("  UNVERIFIED — do not use it until found at Statistics Canada.)")

if __name__ == "__main__":
    main()
