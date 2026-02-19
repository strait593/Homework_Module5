text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def sum_total(text: str) -> float:

    formatted_text = text.replace(',','').replace(':','').split()

    def number_generator(text):
        
        for element in text:

            try:
               yield float(element)

            except ValueError as e:
                continue

    total = sum(number_generator(formatted_text))
    return total
        
total_income = sum_total(text)

print(f"Overall income is equal to {total_income}")