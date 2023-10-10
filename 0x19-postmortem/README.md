# Postmprtem 📓
This is an example of an incident report for the issue of [the web stack debugging#0 task](https://github.com/Ammar-Khaled/alx-system_engineering-devops/tree/main/0x0D-web_stack_debugging_0).

## Issue Summary 📝
From Aug 28, 2023 6:00 AM (GMT+03:00), requests to Apache web server resulted in 500 error response messages.
The issue affected 100% of http requests traffic to this web server. Users have an empty reply with a status code 500 server error. The root cause of this issue was that apache web server was not running.

## Timeline ⏲️
* 6:00 AM: The issue was created
* 6:00 AM: Outage begins
* 6:26 AM: I have recieved an email with the issue
* 6:54 AM: The shell command starts apache service to run
* 6:54 AM: Successful responses from apache
* 7:58 AM: 100% of traffic back online with a status code 200 OK

## Root Cause 💥
The apache processing was not running successfully, so there was no response

## Resolution and recovery 🏖️
A suitable shell command was excuted to run the apache service

## Corrective and Preventative Measures 💡
* Make sure that the web server is configured properly and running successfully
