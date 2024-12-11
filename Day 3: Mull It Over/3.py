import re

def main():
    mulOutputs = []
    with open("3.txt", "r") as file:
        for line in file:
            matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
            for x, y in matches:
                mulOutputs.append(int(x) * int(y))

    print(sum(mulOutputs))

if __name__ == "__main__":
    main()
