#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 09:57:27 by fanilran            #+#    #+#            #
#   Updated: 2026/04/27 14:17:15 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operation(operation_number: int) -> None:
    if operation_number == 0:
        int(45)
    elif operation_number == 1:
        25 / 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
        f"abc, 2544{5}"
    else:
        print("Operation completed successfully\n")


def test_error_type() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operation(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("All error types tested successfully!")


test_error_type()
