# sunny = "Wear a t-shirt and sunglasses."
# cold = "Make sure to wear a warm coat and a scarf."
# rainy = "Don't forget your umbrella and a raincoat."
#
# weather = input("What's the weather like today? (sunny/rainy/cold):")
#
# if weather == "sunny":
#     print(sunny)
# elif weather == "cold":
#     print(cold)
# elif weather == "rainy":
#     print(rainy)
# else:
#     print("Sorry, not sure what to advise.")


def get_weather_advice():
    # Prompt the user for the current weather condition
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Provide clothing recommendations based on the weather condition
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to execute the script
if __name__ == "__main__":
    get_weather_advice()
