sunny = "Wear a t-shirt and sunglasses"
cold = "Make sure to wear a warm coat and a scarf"
rainy = "Don't forget your umbrella and a raincoat"

weather = input("What's the weather like today? (sunny/rainy/cold):")
if weather == "sunny":
    print(sunny)
elif weather == "cold":
    print(cold)
elif weather == "rainy":
    print(rainy)
else:
    print("Sorry, I don't have recommendations")

