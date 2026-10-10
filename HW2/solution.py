"""Answer key for the Trail Supply Planner problem."""


MIN_DISTANCE = 1
MAX_DISTANCE = 30
MIN_TEMPERATURE = 0
MAX_TEMPERATURE = 100


def calculate_water(distance, temperature):
    """Return the recommended water in liters."""
    water = distance * 0.25

    if temperature > 80:
        water = water + 1

    return water


def print_gear_advice(is_raining, is_sunny, temperature):
    """Print every recommendation that applies to the conditions."""
    if is_raining:
        print("Pack a rain jacket.")

    if is_sunny:
        print("Pack sunscreen and a hat.")

    if temperature < 40:
        print("Pack an insulated layer.")
    elif temperature <= 70:
        print("Pack a light extra layer.")


if __name__ == "__main__":
    distance = float(input("Trail distance in miles: "))
    temperature = float(input("Expected temperature in Fahrenheit: "))
    rain_answer = input("Is rain expected? Enter y or n: ")
    sun_answer = input("Will it be sunny? Enter y or n: ")

    distance_is_valid = distance >= MIN_DISTANCE and distance <= MAX_DISTANCE
    temperature_is_valid = (temperature >= MIN_TEMPERATURE and
                            temperature <= MAX_TEMPERATURE)
    weather_answers_are_valid = ((rain_answer == "y" or rain_answer == "n")
                                 and
                                 (sun_answer == "y" or sun_answer == "n"))

    if not distance_is_valid:
        print("Distance must be from 1 through 30 miles.")
    elif not temperature_is_valid:
        print("Temperature must be from 0 through 100 degrees Fahrenheit.")
    elif not weather_answers_are_valid:
        print("Weather questions must be answered with y or n.")
    else:
        is_raining = rain_answer == "y"
        is_sunny = sun_answer == "y"
        water = calculate_water(distance, temperature)

        print(f"Bring at least {water:.2f} liters of water.")
        print_gear_advice(is_raining, is_sunny, temperature)
