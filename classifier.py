def classify_document(ocr_text):
    text_upper = ocr_text.upper()

    pfs_keywords = [
        "PERSONAL FINANCIAL STATEMENT",
        "ASSETS AND LIABILITIES",
        "NET WORTH",
        "SCHEDULE A", "SCHEDULE B", "SCHEDULE C"
    ]

    rent_roll_keywords = [
        "RENT ROLL",
        "OCCUPANT NAME",
        "MONTHLY BASE RENT",
        "ANNUAL RATE PSF",
        "EXPIRATION",
        "OCCUPIED SQFT"
    ]

    coi_keywords = [
        "CERTIFICATEOFLIABILITYINSURANCE",
        "ACORD",
        "COMMERCIALGENERALLIABILITY",
        "CERTIFICATEHOLDER",
        "POLICYNUMBER"
    ]

    scores = {
        'Personal Financial Statement': sum(1 for kw in pfs_keywords if kw in text_upper),
        'Rent Roll': sum(1 for kw in rent_roll_keywords if kw in text_upper),
        'Certificate of Insurance': sum(1 for kw in coi_keywords if kw in text_upper)
    }

    if max(scores.values()) == 0:
        return "Unknown Document"

    return max(scores, key=scores.get)