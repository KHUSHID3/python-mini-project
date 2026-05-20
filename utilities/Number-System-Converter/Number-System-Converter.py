print("🔢 Advanced Number System Converter 🔢")
print("Convert between Decimal, Binary, Octal, Hexadecimal, and more!\n")


# --------------------------------------------------
# Utility Functions
# --------------------------------------------------
def validate_input(num_str, base):
    """Validate whether the given string is valid for the specified base."""
    try:
        int(num_str, base)
        return True
    except ValueError:
        return False


def convert_to_all(num_str, base, source_name):
    """Convert input number to multiple formats."""
    try:
        n = int(num_str, base)

        print(f"\n✨ Conversions for {source_name}: {num_str.upper()}")
        print("=" * 70)

        # Core conversions
        print(f"🔹 Decimal (Base 10)      : {n}")
        print(f"🔹 Binary (Base 2)        : {format(n, 'b')}")
        print(f"🔹 Octal (Base 8)         : {format(n, 'o')}")
        print(f"🔹 Hexadecimal (Base 16)  : {format(n, 'X')}")

        # Additional conversions
        print(f"🔹 Base-3 (Ternary)       : {to_base(n, 3)}")
        print(f"🔹 Base-5 (Quinary)       : {to_base(n, 5)}")
        print(f"🔹 Base-12 (Duodecimal)   : {to_base(n, 12)}")
        print(f"🔹 Base-36               : {to_base(n, 36)}")

        # Signed representations (8-bit)
        print(f"🔹 8-bit Binary          : {format(n & 0xFF, '08b')}")
        print(f"🔹 8-bit Hex             : {format(n & 0xFF, '02X')}")

        # ASCII Character (if printable)
        if 32 <= n <= 126:
            print(f"🔹 ASCII Character       : '{chr(n)}'")
        else:
            print("🔹 ASCII Character       : Not printable")

        # Unicode Character (safe range)
        if 0 <= n <= 0x10FFFF:
            try:
                print(f"🔹 Unicode Character     : {chr(n)}")
            except:
                print("🔹 Unicode Character     : Invalid code point")
        else:
            print("🔹 Unicode Character     : Out of range")

        # Roman numeral (1–3999)
        if 1 <= n <= 3999:
            print(f"🔹 Roman Numeral         : {to_roman(n)}")
        else:
            print("🔹 Roman Numeral         : Out of range (1-3999)")

        # Mathematical properties
        print(f"🔹 Even/Odd              : {'Even' if n % 2 == 0 else 'Odd'}")
        print(f"🔹 Prime Number          : {'Yes' if is_prime(n) else 'No'}")
        print(f"🔹 Square                : {n ** 2}")
        print(f"🔹 Cube                  : {n ** 3}")
        print(f"🔹 Square Root           : {n ** 0.5:.6f}" if n >= 0 else "🔹 Square Root           : Not real")
        print(f"🔹 Factorial             : {factorial_safe(n)}")

        print("=" * 70 + "\n")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")


def to_base(n, base):
    """Convert decimal integer to any base from 2 to 36."""
    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    negative = n < 0
    n = abs(n)

    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base

    return "-" + result if negative else result


def to_roman(num):
    """Convert integer to Roman numeral."""
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = ""
    for value, symbol in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def factorial_safe(n):
    """Compute factorial safely for small numbers only."""
    if n < 0:
        return "Undefined"
    if n > 20:
        return "Too large to display"

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# --------------------------------------------------
# Main Program
# --------------------------------------------------
while True:
    print("=" * 60)
    print("🎯 Choose the source number system:")
    print("1️⃣  Decimal (Base 10)")
    print("2️⃣  Binary (Base 2)")
    print("3️⃣  Octal (Base 8)")
    print("4️⃣  Hexadecimal (Base 16)")
    print("5️⃣  Base-N Converter (2 to 36)")
    print("6️⃣  Exit")
    print("=" * 60)

    choice = input("➡️ Enter your choice (1-6): ").strip()

    if choice == '1':
        val = input("📝 Enter Decimal Number: ").strip()
        if validate_input(val, 10):
            convert_to_all(val, 10, "Decimal")
        else:
            print("❌ Invalid decimal number.\n")

    elif choice == '2':
        val = input("📝 Enter Binary Number: ").strip()
        if validate_input(val, 2):
            convert_to_all(val, 2, "Binary")
        else:
            print("❌ Invalid binary number (only 0 and 1 allowed).\n")

    elif choice == '3':
        val = input("📝 Enter Octal Number: ").strip()
        if validate_input(val, 8):
            convert_to_all(val, 8, "Octal")
        else:
            print("❌ Invalid octal number (digits 0-7 only).\n")

    elif choice == '4':
        val = input("📝 Enter Hexadecimal Number: ").strip()
        if validate_input(val, 16):
            convert_to_all(val, 16, "Hexadecimal")
        else:
            print("❌ Invalid hexadecimal number (0-9, A-F).\n")

    elif choice == '5':
        try:
            base = int(input("🔢 Enter source base (2-36): "))
            if not (2 <= base <= 36):
                print("❌ Base must be between 2 and 36.\n")
                continue

            val = input(f"📝 Enter Number in Base-{base}: ").strip()
            if validate_input(val, base):
                convert_to_all(val, base, f"Base-{base}")
            else:
                print(f"❌ Invalid number for base {base}.\n")
        except ValueError:
            print("❌ Please enter a valid base.\n")

    elif choice == '6':
        print("\n👋 Thanks for using Advanced Number System Converter! Goodbye!\n")
        break

    else:
        print("❌ Invalid choice! Please select 1 to 6.\n")
