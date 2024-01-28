def get_positive_integer_input(prompt):
    # Get a positive integer input from the user
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Pl2ease enter a positive integer!")
            return value
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(prompt):
    # Get a yes or no input from the user
    while True:
        try:
            response = input(prompt).strip().lower()
            if response not in ['y', 'n']:
                raise ValueError('Please answer "Y" or "N".')
            return response == 'y'
        except ValueError:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app):
    # Calculate the total price based on input parameters
    pizza_price = 12
    delivery_cost = 2.50 if num_pizzas < 5 and is_delivery else 0
    total_price = num_pizzas * pizza_price + delivery_cost

    # Apply a 50% discount on Tuesdays
    if is_tuesday:
        total_price *= 0.5

    # Apply a 25% discount if the app is used
    if used_app:
        total_price *= 0.75

    return round(total_price, 2)

def main():
    # Main function to run the pizza price calculator
    print("BPP Pizza Price Calculator")
    print("==========================")

    try:
        # Get input from the user and calculate the total price
        num_pizzas = get_positive_integer_input("How many pizzas ordered? ")
        is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")
        is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")
        used_app = get_yes_no_input("Did the customer use the app? (Y/N) ")

        total_price = calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app)

        # Display the total price
        print(f"\nTotal Price: £{total_price:.2f}.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
