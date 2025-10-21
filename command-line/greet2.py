import argparse

parser = argparse.ArgumentParser(description="A simple greeting program.")
parser.add_argument("name", help="The name to greet.")
parser.add_argument("--age", type=int, default=30, help="The age of the person.")

args = parser.parse_args()

print(f"Hello, {args.name}! You are {args.age} years old.")