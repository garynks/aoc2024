def isSafeReport(report):
    increasing = all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def isKindOfSafeReport(report):
    if isSafeReport(report):
        return True
    
    for i in range(len(report)):
        dampenedReport = report[:i] + report[i+1:]
        if isSafeReport(dampenedReport):
            return True
    return False

def main():
    ### Part 1 & Part 2
    safeReportsCount = 0
    kindOfSafeReportsCount = 0
    with open("2.txt", "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if isSafeReport(report):
                safeReportsCount += 1
            if isKindOfSafeReport(report):
                kindOfSafeReportsCount += 1


    print(safeReportsCount)
    print(kindOfSafeReportsCount)

if __name__ == "__main__":
    main()
