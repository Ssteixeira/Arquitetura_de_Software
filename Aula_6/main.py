# Arquivo: main.py
import argparse
from application.use_cases import MLUseCases

def main():
    parser = argparse.ArgumentParser(description="Hexagonal ML Pipeline CLI")
    parser.add_argument('command', choices=['download', 'profile', 'edit', 'train'], help="Command to execute")
    parser.add_argument('csv_filename', help="CSV file to process")

    args = parser.parse_args()

    ml_use_cases = MLUseCases()

    if args.command == 'profile':
        # Chama o método de profiling com o nome do arquivo CSV
        ml_use_cases.profile_data(args.csv_filename)

if __name__ == '__main__':
    main()
