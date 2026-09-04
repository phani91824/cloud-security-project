PATTERNS = {

    "Email":
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    "Phone Number":
    r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",

    "Credit Card":
    r"\b(?:\d{4}[- ]?){3}\d{4}\b",

    "Aadhaar-like Number":
    r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b",

    "Password":
    r"(?i)\bpassword\s*[:=]\s*[^\s]+",

    "API Key":
    r"(?i)\b(?:api[_-]?key|apikey)\s*[:=]\s*[A-Za-z0-9_\-]+",

    "Secret Key":
    r"(?i)\b(?:secret[_-]?key|secret)\s*[:=]\s*[A-Za-z0-9_\-]+"
}