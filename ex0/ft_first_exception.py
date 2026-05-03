#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/07 14:51:01 by fanilran            #+#    #+#            #
#   Updated: 2026/04/27 17:30:43 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        res = input_temperature("25")
        print(f"Temperature is now {res}°c\n")
    except ValueError as e:
        print(f"{e}\n")
    try:
        print("Input data is 'abc'")
        res = input_temperature("abc")
        print(f"Temperature is now {res}°c\n")
    except ValueError as e:
        print(f"{e}\n")
    print("All tests completed - program didn't crash!")


test_temperature()
