*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallee
    Set Password  kalle123
    Set Passwordconfirm  kalle123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Passwordconfirm  kalle123
    Submit Credentials
    Register Should Fail With Message  Username must only contain a-z characters and must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kallee
    Set Password  kalle12
    Set Passwordconfirm  kalle12
    Submit Credentials
    Register Should Fail With Message  Password can not only contain characters and its minimum length is 8

Register With Nonmatching Password And Password Confirmation
    Set Username  kallee
    Set Password  kalle123
    Set Passwordconfirm  kalle124
    Submit Credentials
    Register Should Fail With Message  Passwords must match

Login After Successful Registration
    Set Username  eikalle
    Set Password  kalle123
    Set Passwordconfirm  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  eikalle
    Set Password  kalle123
    Submit Logincredentials
    Login Should Succeed

Login After Failed Registration
    Set Username  eikallee
    Set Password  kalle12
    Set Passwordconfirm  kalle12
    Submit Credentials
    Go To Login Page
    Set Username  eikalle
    Set Password  kalle12
    Submit Logincredentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Logincredentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Passwordconfirm
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
