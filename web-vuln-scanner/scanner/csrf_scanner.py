def scan_csrf(form):
    for input in form["inputs"]:
        if input["name"] and "csrf" in input["name"].lower():
            return None

    return {
        "type": "CSRF",
        "severity": "Medium",
        "evidence": "No CSRF token found"
    }
