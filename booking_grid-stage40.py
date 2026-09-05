# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: BookingGrid
import argparse

def main():
    parser = argparse.ArgumentParser(description='BookingGrid CLI')
    parser.add_argument('command', choices=['book', 'cancel', 'list', 'pay'], help='Command to execute')
    parser.add_argument('--client', type=str, help='Client email')
    parser.add_argument('--service', type=str, help='Service name')
    parser.add_argument('--slot', type=str, help='Slot date')
    parser.add_argument('--amount', type=float, help='Payment amount')
    args = parser.parse_args()
    if args.command == 'book':
        print(f'Booking: {args.client} -> {args.service} on {args.slot}')
    elif args.command == 'cancel':
        print(f'Cancelled: {args.client} booking')
    elif args.command == 'list':
        print('All bookings...')
    elif args.command == 'pay':
        print(f'Payment: {args.amount} for {args.client}')

if __name__ == '__main__':
    main()
