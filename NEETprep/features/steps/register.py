from behave import *

@given(u'As New User I am on the NEETprep New login page')
def step_impl(context):
    print("Inside - As New User: on NEETprep New login page")


@when(u'As New User I enter my mobile number')
def step_impl(context):
    print("Inside - As New User: entered mobile number")


@when(u'As New User I click the Send OTP button')
def step_impl(context):
    print("Inside - As New User: clicked Send OTP button")


@when(u'As New User I enter the OTP')
def step_impl(context):
    print("Inside - As New User: entered OTP")


@when(u'As New User I click the OTP button to verify OTP')
def step_impl(context):
    print("Inside - As New User: clicked Verify OTP button")


@when(u'As New User I See regsitration page & click I am new here button')
def step_impl(context):
    print("Inside - As New User: clicked 'I am new here' button")


@when(u'As New User I enter Full Name in new user field')
def step_impl(context):
    print("Inside - As New User: entered Full Name")


@when(u'As New User I enter valid emailID')
def step_impl(context):
    print("Inside - As New User: entered valid email ID")


@when(u'As New User I click Next button & will see account successfully created message')
def step_impl(context):
    print("Inside - As New User: clicked 'Next' button and saw account created message")


@when(u'As New User I fill board exam year')
def step_impl(context):
    print("Inside - As New User: filled board exam year")


@when(u'As New User I click Continue button')
def step_impl(context):
    print("Inside - As New User: clicked 'Continue' button")


@when(u'As New User I click Get Started button & Exit buy course page')
def step_impl(context):
    print("Inside - As New User: clicked 'Get Started' button and exited buy course page")


@then(u'As New User I will sucessfully land on NEETprep dashbaord')
def step_impl(context):
    print("Inside - As New User: successfully landed on NEETprep dashboard")
