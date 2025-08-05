credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


credit_number = credit_number[::-1]  # -1 means reverse a string - ანუ შებრუნებულია
print(credit_number)