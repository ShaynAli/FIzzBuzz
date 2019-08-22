import sys
import argparse


def divisible_by(n):
    """
    Generates a function to check the divisibility of a number by n
    :param n: The factor to test divisibility against
    :return: A function which returns True if a number is divisible by n and False otherwise
    """
    return lambda x: x % n == 0


""" These outputs are printed if their corresponding rules apply """
output_rules = {
    'Fizz': divisible_by(3),
    'Buzz': divisible_by(5)
}


def fizz_buzz(x):
    outputs = [output for output, rule in output_rules.items() if rule(x)]
    return ''.join(outputs) or str(x)


def fizz_buzz_range(stop, *, start=1):
    """
    Returns a generator which yields the appropriate FizzBuzz from start to stop.
    Can be called as fizz_buzz_range(45) where start defaults to 1 , or start can be specified as in
    fizz_buzz_range(start=10, stop=45).
    :param stop: The exclusive upper bound
    :param start: The inclusive lower bound, defaults to 1
    :return: The next FizzBuzz
    """
    for i in range(start, stop):
        yield fizz_buzz(i)


def build_parser():
    """
    Builds the FizzBuzz parser
    :return: The parser which this program uses in the command line
    """
    parser = argparse.ArgumentParser(description='The classic FizzBuzz game in programmatic form.', add_help=False)
    parser.add_argument('-h', '--help', default=argparse.SUPPRESS, action='help',
                        help='Show this help message and exit.')
    parser.add_argument('-s', '--start', default=1, type=int, action='store', metavar='START',
                        help='The number to start FizzBuzzing at (inclusive).')
    parser.add_argument('stop', type=int, action='store', metavar='STOP',
                        help='The number to end FizzBuzzing at (exclusive).')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    for fizz_buzz_output in fizz_buzz_range(start=args.start, stop=args.stop):
        print(fizz_buzz_output)


if __name__ == '__main__':
    main()
