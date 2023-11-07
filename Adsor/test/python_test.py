import sys

if len(sys.argv) != 4:
    print("Please provide two numbers as command line arguments.")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    print(f"First number: {num1}")
    print(f"Second number: {num2}")

