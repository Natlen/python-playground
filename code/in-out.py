from typing import TypeAlias

#int
def in_int() -> None:
    try:
        desiredType: TypeAlias = int
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: '))
        print(__in)
    except ValueError:
        print(f'the input is not of type {int}\n')

#float
def in_float() -> None:
    try:
        desiredType: TypeAlias = float
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: '))
        print(__in)
    except ValueError:
        print(f'the input is not of type {desiredType}\n')

#bool
def in_bool() -> None:
    try:
        desiredType: TypeAlias = bool
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: '))
        print(__in)
    except ValueError: #will never reach here since - empty string == false, non-empty == true
        print(f'the input is not of type {desiredType}\n')

#list
def in_list() -> None:
    try:
        desiredType: TypeAlias = list
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: ').split())
        print(__in)
    except ValueError: #will never reach here since - empty string == false, non-empty == true
        print(f'the input is not of type {desiredType}\n')

#tuple
def in_tuple() -> None:
    try:
        desiredType: TypeAlias = tuple
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: ').split())
        print(__in)
    except ValueError: #will never reach here since - empty string == false, non-empty == true
        print(f'the input is not of type {desiredType}\n')

#set
def in_set() -> None:
    try:
        desiredType: TypeAlias = set
        __in: desiredType = desiredType(input(f'Enter a {desiredType}: ').split())
        print(__in)
    except ValueError: #will never reach here since - empty string == false, non-empty == true
        print(f'the input is not of type {desiredType}\n')

#set
def in_set() -> None:
    try:
        desiredType: TypeAlias = dict
        __in: desiredType = desiredType(pair.split(':',1) for pair in 
                                        input(f'Enter a {desiredType} at form key1:val1 , ... , keyN:valN: ')
                                        .replace(' ','')
                                        .split(','))
        print(__in)
    except ValueError: #will never reach here since - empty string == false, non-empty == true
        print(f'the input is not of type {desiredType}\n')
