import requests
import re

SQLI_PAYLOADS = ["'", "' OR '1'='1"]

ERROR_PATTERNS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark"
]

def scan_sqli(form):
    findings = []

    for payload in SQLI_PAYLOADS:
        data = {}
        for input in form["inputs"]:
            if input["name"]:
                data[input["name"]] = payload

        response = requests.post(form["action"], data=data)

        for error in ERROR_PATTERNS:
            if re.search(error, response.text, re.IGNORECASE):
                findings.append({
                    "type": "SQL Injection",
                    "payload": payload,
                    "severity": "Critical",
                    "evidence": error
                })

    return findings
