import json

with open('trivyreport.json') as jsonfile:
    jsondata = ''.join(line for line in jsonfile if not line.startswith('2022' or '2023'))
    res = json.loads(jsondata)
    for r in res["Results"]:
        for v in r["Vulnerabilities"]:
            trivySeverity = v["Severity"]
            if trivySeverity == 'LOW':
                trivyProductSev = int(1)
                trivyNormalizedSev = trivyProductSev * 10
                print("Threshold for LOW Severity: ")
                print(trivyNormalizedSev)
            elif trivySeverity == 'MEDIUM':
                 trivyProductSev = int(4)
                 trivyNormalizedSev = trivyProductSev * 10
                 print("Threshold for MEDIUM Severity: ")
                 print(trivyNormalizedSev)
            elif trivySeverity == 'HIGH':
                 trivyProductSev = int(7)
                 trivyNormalizedSev = trivyProductSev * 10
                 print("Threshold for HIGH Severity: ")
                 print(trivyNormalizedSev)
            elif trivySeverity == 'CRITICAL':
                 trivyProductSev = int(9)
                 trivyNormalizedSev = trivyProductSev * 10
                 print("Threshold for CRITICAL Severity: ")
                 print(trivyNormalizedSev)
