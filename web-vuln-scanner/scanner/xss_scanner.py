import requests

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert('XSS')</script>"
]

def scan_xss(form):
    vulnerabilities = []

    for payload in XSS_PAYLOADS:
        data = {}
        for input in form["inputs"]:
            if input["name"]:
                data[input["name"]] = payload

        if form["method"] == "post":
            response = requests.post(form["action"], data=data)
        else:
            response = requests.get(form["action"], params=data)

        if payload in response.text:
            vulnerabilities.append({
                "type": "XSS",
                "payload": payload,
                "severity": "High",
                "evidence": "Payload reflected in response"
            })

    return vulnerabilities
