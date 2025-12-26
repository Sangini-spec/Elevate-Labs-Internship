from flask import Flask, render_template, request
from scanner.crawler import crawl
from scanner.utils import scan_form
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form["url"]
        forms = crawl(target)
        results = []

        for form in forms:
            results.extend(scan_form(form))

        with open("reports/scan_report.json", "w") as f:
            json.dump(results, f, indent=4)

        return render_template("results.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
