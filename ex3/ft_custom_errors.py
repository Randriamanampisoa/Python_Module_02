#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 16:17:22 by fanilran            #+#    #+#            #
#   Updated: 2026/04/27 17:14:21 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, sms: str = "Unknown plant error") -> None:
        super().__init__(sms)


class PlantError(GardenError):
    def __init__(self, sms: str = "Unknown plant error") -> None:
        super().__init__(sms)


class WaterError(GardenError):
    def __init__(self, sms: str = "Unknown plant error") -> None:
        super().__init__(sms)


def verification_PlanteError(temp: int) -> None:
    if temp <= 40 and temp >= 0:
        print("The temperature is just right for the plant.")
    else:
        raise PlantError("Caught PlantError: This temperature exceeds "
                         "the permitted range (must be ≥ 0 and ≤ 40).")


def verification_WaterError(water: int) -> None:
    if water >= 5 and water <= 10:
        print("The water used to water the plant is perfectly suitable")
    else:
        raise WaterError("Caught WaterError: This water level does not "
                         "guarantee plant health (must be ≥ 5 and ≤ 10).")


def test_verification() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        verification_PlanteError(41)
    except PlantError as e:
        print(e)
    print()
    try:
        print("Testing WaterError...")
        verification_WaterError(50)
    except WaterError as e:
        print(e)
    print()
    try:
        print("Testing catching all garden errors...")
        verification_PlanteError(41)
    except GardenError as e:
        print(e)
    try:
        verification_WaterError(50)
    except GardenError as e:
        print(e)
    print("\nAll custom error types work correctly!")


test_verification()
