import re

def main():
    ## Part 1
    # mulOutputs = []
    # with open("3.txt", "r") as file:
    #     for line in file:
    #         matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    #         for x, y in matches:
    #             mulOutputs.append(int(x) * int(y))

    ## Part 2
    mulOutputs = []
    with open("3.txt", "r") as file:
        disabled = False
        for line in file:
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
            print(matches)
            for match in matches:
                if match == "do()":
                    disabled = False
                elif match == "don't()":
                    disabled = True
                elif not disabled:
                    x, y = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', match)[0]
                    mulOutputs.append(int(x) * int(y))

    print(sum(mulOutputs))

if __name__ == "__main__":
    main()
