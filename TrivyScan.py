import json

with open('trivyreport.json', encoding="utf") as jsonfile:
    jsondata = ''.join(line for line in jsonfile if not line.startswith('2022' or '2023'))
    res = json.loads(jsondata)
    for r in res["Results"]:
        for v in r["Vulnerabilities"]:
            print(v["Severity"])
