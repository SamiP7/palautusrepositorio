*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  moimoimoi2
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  moimoimoi2
    Output Should Contain  Username must only contain a-z characters and must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kallee  moimoi2
    Output Should Contain  Password can not only contain characters and its minimum length is 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallee  moimoimoi
    Output Should Contain  Password can not only contain characters and its minimum length is 8

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123