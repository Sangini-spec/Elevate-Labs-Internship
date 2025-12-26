from scanner.xss_scanner import scan_xss
from scanner.sqli_scanner import scan_sqli
from scanner.csrf_scanner import scan_csrf

def scan_form(form):
    results = []
    results.extend(scan_xss(form))
    results.extend(scan_sqli(form))

    csrf_result = scan_csrf(form)
    if csrf_result:
        results.append(csrf_result)

    return results
