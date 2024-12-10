def isSafeReport(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def main():
    ### Part 1
    safeReportsCount = 0
    with open("2.txt", "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if isSafeReport(report):
                safeReportsCount += 1

    print(safeReportsCount)

if __name__ == "__main__":
    main()
