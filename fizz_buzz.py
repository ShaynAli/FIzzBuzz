import sys
import argparse


def divisible_by(n):
    return lambda x: x % n == 0


output_rules = {
    'Fizz': divisible_by(3),
    'Buzz': divisible_by(5)
}


def fizz_buzz(i):
    outputs = [output for output, rule in output_rules.items() if rule(i)]
    return ''.join(outputs) or str(i)


def fizz_buzz_range(stop, *, start=1):
    for i in range(start, stop):
        yield fizz_buzz(i)


def build_parser():
    parser = argparse.ArgumentParser(description='The classic FizzBuzz game in programmatic form.', add_help=False)
    parser.add_argument('-h', '--help', default=argparse.SUPPRESS, action='help',
                        help='Show this help message and exit.')
    parser.add_argument('-s', '--start', default=1, type=int, action='store', metavar='START',
                        help='The number to start FizzBuzzing at (inclusive)')
    parser.add_argument('stop', type=int, action='store', metavar='STOP',
                        help='The number to end FizzBuzzing at (exclusive)')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    for fizz_buzz_output in fizz_buzz_range(start=args.start, stop=args.stop):
        print(fizz_buzz_output)


if __name__ == '__main__':
    main()
