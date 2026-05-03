#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:32:46 by fanilran            #+#    #+#            #
#   Updated: 2026/04/27 15:55:12 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Error(Exception):
    def __init__(self, sms: str = "Unknows Error") -> None:
        super().__init__(sms)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise Error("Caught PlantError: Invalid plant name to water: "
              f"'{plant_name}'.. ending tests and returning to main")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    lst = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for i in lst:
            water_plant(i)
    except Error as e:
        print(f"{e}")
    finally:
        print("Closing watering system\n")

    lst = ["tomato", "Lettuce", "Carrots"]
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for i in lst:
            water_plant(i)
    except Error as e:
        print(f"{e}")
    finally:
        print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")

test_watering_system()