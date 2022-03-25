import json

trivyNormalizedLowSeverity = 0
trivyNormalizedMediumSeverity = 0
trivyNormalizedHighSeverity = 0
trivyNormalizedCriticalSeverity = 0

with open('trivyreport.json') as jsonfile:
    jsondata = ''.join(line for line in jsonfile if not line.startswith('2022' or '2023'))
    res = json.loads(jsondata)
    for r in res["Results"]:
        for v in r["Vulnerabilities"]:
            trivySeverity = v["Severity"]
            if trivySeverity == 'LOW':
               trivyProductSev = int(1)
               trivyNormalizedLowSeverity = trivyNormalizedLowSeverity + trivyProductSev * 10
            elif trivySeverity == 'MEDIUM':
                 trivyProductSev = int(4)
                 trivyNormalizedMediumSeverity = trivyNormalizedMediumSeverity + trivyProductSev * 10
            elif trivySeverity == 'HIGH':
                 trivyProductSev = int(7)
                 trivyNormalizedHighSeverity = trivyNormalizedHighSeverity + trivyProductSev * 10
            elif trivySeverity == 'CRITICAL':
                 trivyProductSev = int(9)
                 trivyNormalizedCriticalSeverity = trivyNormalizedCriticalSeverity + trivyProductSev * 10
                 
print("Threshold for LOW Severity: ")
print(trivyNormalizedLowSeverity)
print("Threshold for MEDIUM Severity: ")
print(trivyNormalizedMediumSeverity)
print("Threshold for HIGH Severity: ")
print(trivyNormalizedHighSeverity)
print("Threshold for CRITICAL Severity: ")
print(trivyNormalizedCriticalSeverity)
