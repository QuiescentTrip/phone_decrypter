import sys

def main(kode):
    kode_liste = kode.split(" ")
    output = ""
    phone = {
    0: "+",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ"
    }

    for string in kode_liste:
        a, b = string.split("-")
        første_tall = int(a)
        andre_tall = int(b)
        output += phone.get(første_tall)[andre_tall-1]

    return (" ".join(output.lower().split("+")))

if __name__ == "__main__":
    print(main('7-4 9-3 7-4 8-1 3-2 6-1 0-1'))
