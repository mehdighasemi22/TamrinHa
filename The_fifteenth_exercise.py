def calculate_total(cart, prices):
    total_price = 0

    for item, quantity in cart.items():  #cart.items() = hamon key/value hast
        if item in prices:  
            unit_price = prices[item]  
            total_price += quantity * unit_price 
        else:
            print(f"gheymat {item} dar list gheymat-ha mojood nist")

    return total_price



cart = {"Apple": 3, "Banana": 5, "Orange": 2}
prices = {"Apple": 1.5, "Banana": 0.5, "Orange": 1.25}

print("Output =", calculate_total(cart, prices)) 

cart1 = {"Book": 2}
prices1 = {"Book": 10}

print("Output =", calculate_total(cart1, prices1))  
