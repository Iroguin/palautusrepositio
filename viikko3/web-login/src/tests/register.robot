*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username    testuser
    Set Password    test123456
    Set Password Confirmation    test123456
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username    te
    Set Password    test12345
    Set Password Confirmation    test12345
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    testuser
    Set Password    test123
    Set Password Confirmation    test123
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username    testuser
    Set Password    abcdefghi
    Set Password Confirmation    abcdefghi
    Submit Registration
    Registration Should Fail With Message    Password can not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username    testuser
    Set Password    test12345
    Set Password Confirmation    test54321
    Submit Registration
    Registration Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Create User    kalle    kalle123456
    Set Username    kalle
    Set Password    test12345
    Set Password Confirmation    test12345
    Submit Registration
    Registration Should Fail With Message    Username is already taken

Login After Successful Registration
    Set Username    newuser
    Set Password    newpass123
    Set Password Confirmation    newpass123
    Submit Registration
    Click Logout Link
    Go To Login Page
    Set Username    newuser
    Set Password    newpass123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username    us
    Set Password    test12345
    Set Password Confirmation    test12345
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long
    Go To Login Page
    Set Username    us
    Set Password    test12345
    Submit Credentials
    Login Should Fail With Message    Invalid username or password

*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password}
    Input Password    password_confirmation    ${password}

Submit Registration
    Click Button    Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Submit Credentials
    Click Button    Login

Login Should Fail With Message
    [Arguments]    ${message}
    Login Page Should Be Open
    Page Should Contain    ${message}