import re
from patterns import PATTERNS


def detect_sensitive_data(text):

    results = []

    for data_type, pattern in PATTERNS.items():

        matches = re.finditer(pattern, text)

        for match in matches:

            results.append({
                "type": data_type,
                "value": match.group()
            })

    return results


def calculate_risk(results):

    count = len(results)

    if count == 0:
        return "LOW"

    elif count <= 2:
        return "MEDIUM"

    else:
        return "HIGH"