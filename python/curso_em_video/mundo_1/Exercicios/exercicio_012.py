# Create an algorythm that reads the price of a product and shows its price with a 5% discount.
product_price = float(input("What is the price of the product? R$"))
discount = product_price * 0.05
final_price = product_price - discount
print(f"The product's price with a 5% discount is R${final_price:.2f}")