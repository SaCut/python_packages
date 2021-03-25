# python request package

# let's connect to the live web using requests api
# we will connect to www.bbc.co.uk and check if the website is working
import requests

response = requests.get("http://www.bbc.co.uk/")

# if responses.status_code == 200:
# 	print("the website is up and running: status code " + str(responses.status_code))
# else:
# 	print("Oops, something went wrong! status code: " + str(responses.status_code))

# #response code 200 means everything is working correctly

# # test: create a function called status_code_check
# # function should return status code with appropriate message
# def status_code_check(site):
# 	responses = requests.get(site)

# 	if responses.status_code == 200:
# 		return "the website is up and running: status code " + str(responses.status_code)
# 	else:
# 		return "Oops, something went wrong! status code: " + str(responses.status_code)

# print(status_code_check("http://www.bbc.co.uk/"))

if response:
	print("success, and the status code is: " + response.status_code)
else:
	print("failure. The status code is: " + response.status_code)


# requests goes one step further in simplifying this process for us
# if you use the response package in a condition expression
# it will evaluate to True if the status code was between 200 and 400, False otherwise

# 