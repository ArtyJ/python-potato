import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('--input', type=str, dest='input_str')
    parser.add_argument('--output', type=str, dest='output')
    args = parser.parse_args()

    print(f'input_str={args.input_str} and output={args.output}')
