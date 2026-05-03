#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/26 02:19:15 by fanilran            #+#    #+#            #
#   Updated: 2026/04/27 17:32:05 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class TempError(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError("Caught input_temperature error: "
                         "invalid literal for int() with base 10: "
                         f"'{temp_str}'")
    if temp > 40:
        raise TempError("Caught input_temperature error: "
                        f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise TempError("Caught input_temperature error: "
                        f"{temp} is too cold for plants (min 0°C)")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    try:
        print("Input data is '25'")
        res = input_temperature("25")
        if res <= 40 and res >= 0:
            print(f"Temperature is now {res}°C\n")
    except ValueError as e:
        print(f"{e}\n")
    except TempError as e:
        print(f"{e}\n")
    try:
        print("Input data is 'abc'")
        res = input_temperature("abc")
        if res <= 40 and res >= 0:
            print(f"Température {res}°C\n")
    except ValueError as e:
        print(f"{e}\n")
    except TempError as e:
        print(f"{e}\n")
    try:
        print("Input data is '100'")
        res = input_temperature("100")
        if res <= 40 and res >= 0:
            print(f"Température {res}°C\n")
    except ValueError as e:
        print(f"{e}\n")
    except TempError as e:
        print(f"{e}\n")
    try:
        print("Input data is '-50'")
        res = input_temperature("-50")
        if res <= 40 and res >= 0:
            print(f"Température {res}°C\n")
    except ValueError as e:
        print(f"{e}\n")
    except TempError as e:
        print(f"{e}\n")
    print("All tests completed - program didn't crash!")


test_temperature()
