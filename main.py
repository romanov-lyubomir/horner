from texttable import Texttable
from math import gcd # Greatest common divisor


def format_print(text, color, sep=" ", end="\n"):
    colors = {
        "purple": '\033[95m',
        "cyan": '\033[96m',
        "dark_cyan": '\033[36m',
        "blue": '\033[94m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "red": '\033[91m',
        "bold": '\033[1m',
        "underline": '\033[4m',
        "end": '\033[0m'
    }
    print(colors[color] + text + colors["end"], sep=sep, end=end)

def extend_list(list, length):
    if len(list) < length:
        for i in range(length - len(list)):
            list.append("")
    return list

def polynomial(coefficients):
    result = ""
    for i in range(len(coefficients)):
        power = len(coefficients) - i - 1
        if coefficients[i] > 0:
            result += "+"
        if power != 1 and power != 0:
            if coefficients[i] == 1:
                result += f"x^{power}"
            elif coefficients[i] == 0:
                continue
            else:
                result += f"{coefficients[i]}x^{str(power)}"
        elif power == 1:
            if coefficients[i] == 1:
                result += f"x"
            elif coefficients[i] == 0:
                continue
            else:
                result += f"{coefficients[i]}x"
        elif power == 0:
            if coefficients[i] == 0:
                continue
            else:
                result += f"{coefficients[i]}"
    if result[0] == "+":
        result = result[1:]
    return result



def divisors(n):
    if n < 0:
        n = abs(n)
    return [-i for i in range(1, n+1) if n % i == 0] + [i for i in range(1, n+1) if n % i == 0]

def simplify_fraction(numerator, denominator):
    return [numerator // gcd(numerator, denominator), denominator // gcd(numerator, denominator)]


deg=int(input("Enter the degree of the polynomial: "))
coeffs=[]
for i in range(deg+1):
    coeffs.append(int(input("Enter the coefficient of x^"+str(deg-i)+": ")))

pq_list=[]
for q in divisors(coeffs[0]):
    for p in divisors(coeffs[-1]):
        pq_list.append([p,q])

print("=============")
format_print(color="blue", text=f"The polynomial is: {polynomial(coeffs)}")


for i in range(len(pq_list)):
    if (pq_list[i][0] > 0 and pq_list[i][1] < 0) or (pq_list[i][0] < 0 and pq_list[i][1] < 0):
        pq_list[i][0] = -pq_list[i][0]
        pq_list[i][1] = -pq_list[i][1]


for i in range(len(pq_list)):
    if type(pq_list[i]) == list:
        pq_list[i] = simplify_fraction(pq_list[i][0], pq_list[i][1])



for i in range(len(pq_list)):
    if pq_list.count(pq_list[i]) > 1:
        pq_list[i] = None
pq_list = [i for i in pq_list if i != None]

pq_list.sort(key=lambda x: abs(x[0]/x[1]) if type(x) == list else abs(x))

print("=============")
format_print(color="blue", text=f"The possible roots are: {pq_list}")

roots = {}

t = Texttable()
t.add_row([""] + coeffs)

for pq in pq_list:
    numbers = [coeffs[0]]
    for i in range(1, len(coeffs)):
        numbers.append(pq[0]/pq[1] * numbers[i-1] + coeffs[i])
    if numbers[-1] == 0:
        roots[f"{pq}"] = roots[f"{pq}"] + 1 if f"{pq}" in roots else 1
        coeffs = numbers[:-1]
    t.add_row([f"{pq[0]}/{pq[1]}"] + extend_list(numbers, deg+1))

print("=============")
print("Horner's scheme is: ")
print(t.draw())

print("=============")
format_print(color="green", text=f"Roots: {roots}")
print("=============")
