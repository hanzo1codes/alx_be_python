sunny = "Wear a t-shirt and sunglasses"
rainy = "Don't forget your umbrella and a raincoat"
cold = "ake sure to wear a warm coat and a scarf"
error = "Sorry, I don't have recommendations"
weather_input = input("What's the weather like today? (sunny/rainy/cold)")

if weather_input == "sunny":
    print(sunny)
elif weather_input == "cold":
    print(cold)
elif weather_input == "rainy":
    print(rainy)
else:
    print(error)
