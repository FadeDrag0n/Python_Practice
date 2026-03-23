def safe_int_input(prom: str = 'Please enter a number:') -> int:
    while True:
        try:
            return int(input(prom))
        except ValueError:
            print('Please enter a number')