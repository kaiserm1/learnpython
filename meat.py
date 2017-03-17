"""
    Louie's Hawaiian BBQ:
    Louie’s Hawaiian BBQ sells pork, chicken and beef meals, all are available in mini, regular and large.  A mini meal
    includes a single portion of meat, plus one side dish.  A regular includes a double portion of meat with one side
    dish, and a large includes a double portion of meat plus three side dishes.  A single portion of beef is 3.00,
    a double portion is 6.00.  Chicken is similiarly priced, with a single portion costing 2.50 and a double portion
    costing 5.00.  Pork is in quantity, so is the least expensive, with a single portion costing 2.00 and a double
    portion costing 3.00.  Side dishes are 1.00 apiece.  State tax is 8.25% on prepared food.

    Louie needs software which allows him to enter a customer’s meal choice, and computes the price for that meal.
    You are to write an application which will help Louie’s staff compute the price for an order.

    STEP 1:

    Your program is to allow Louie to enter the type of meat and the size, and output the cost of the meal.
    Your program should provide functions:

        price_pork_meal(size)  -- returns price of pork meal based on size parameter
        price_beef_meal(size) -- returns price of beef meal based on size parameter
        price_chicken_meal(size)-- returns price of chicken meal based on size parameter
        final_price(price, tax_percent) – returns final price of meal with tax

    Your program follows the following algorithm:
        * prompt user for a type of meat (Pork,Beef, Chicken)
          (Reprompt user if a valid type of meat is not provided)
        * prompt the user for the size mean (mini, regular or large)
          (If user does not indicate valid size, assume regular)
        * calculate the price of the meal  (call one of the functions above)
        * calculate the final price of the meal (use function)
        * print the price before and after tax
"""


def price_pork_meal(size):
    """
    Calculate the price of a pork meal before taxes depending on meal size.
    :param size: string - size of meal
    :return: float - price of meal
    """
    meat_price = 2.00
    side_price = 1.00
    if size == 'mini':
        return meat_price + side_price
    elif size == 'regular':
        return meat_price * 2 + side_price
    return meat_price * 2 + side_price * 3


def price_beef_meal(size):
    """
    Calculate the price of a beef meal before taxes depending on meal size.
    :param size: string - size of meal
    :return: float - price of meal
    """
    meat_price = 3.00
    side_price = 1.00
    if size == 'mini':
        return meat_price + side_price
    elif size == 'regular':
        return meat_price * 2 + side_price
    return meat_price * 2 + side_price * 3


def price_chicken_meal(size):
    """
    Calculate the price of a chicken meal before taxes depending on meal size.
    :param size: string - size of meal
    :return: float - price of meal
    """
    meat_price = 2.50
    side_price = 1.00
    if size == 'mini':
        return meat_price + side_price
    elif size == 'regular':
        return meat_price * 2 + side_price
    return meat_price * 2 + side_price * 3


def final_price(price, tax_percent):
    """
    Calculate price of meal after taxes.
    :param price: float - price of meal before taxes
    :param tax_percent: float - tax percentage as decimal
    :return: float - total price after taxes
    """
    return price + price * tax_percent


meat_selection = ['pork', 'beef', 'chicken']
meal_size = ['mini', 'regular', 'large']
state_tax = 0.0825

# User selects meat type. If input is invalid, prompt for another try.
while True:
    meat_choice = input('Enter your meat choice: "pork", "beef" or "chicken"\n').lower()
    if meat_choice in meat_selection:
        # User selects meal size. If input is invalid, prompt for another try.
        while True:
            size_choice = input('Enter desired size: "mini", "regular" or "large"\n').lower()
            if size_choice in meal_size:
                break
            else:
                print('Wrong input. Please try again.')
        # All choices made and valid. Exit the loop
        break
    else:
        print('Wrong input. Please try again.')
# Calculate prices before and after taxes, depending on meat choice and size of meal.
if meat_choice == 'pork':
    price = price_pork_meal(size_choice)
elif meat_choice == 'beef':
    price = price_beef_meal(size_choice)
else:
    price = price_chicken_meal(size_choice)
total = final_price(price, state_tax)
print('|---------------------------|')
print('| Price before taxes: {:03.2f}$ |'.format(round(price, 2)))
print('| Total after taxes:  {:03.2f}$ |'.format(round(total, 2)))
print('|---------------------------|')
