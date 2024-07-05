sunny = "Wear a t-shirt and sunglasses"
rainy = "Don't forget your umbrella and a raincoat"
cold = "ake sure to wear a warm coat and a scarf"
error = "Sorry, I don't have recommendations"
user_input = input("What's the weather like today? (sunny/rainy/cold)")

if user_input == "sunny":
    print(sunny)
elif user_input == "cold":
    print(cold)
elif user_input == "rainy":
    print(rainy)
else:
    print(error)
