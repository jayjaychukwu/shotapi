# shotapi 
## Clone or download this repo and create a virtual environment in the folder
### Run
> **pip install -r requirements.txt**
### Run 
> **python manage.py runserver**
### Go to **"127.0.0.1:8000"** on your browser (or whatever localhost it is running)
<br>

## Docs
###  **Swagger**: 127.0.0.1:8000/
### **Redoc**: 127.0.0.1:8000/redoc  
<br>

## Admin Details: 127.0.0.1:8000/admin
> username: 2341234567890  
> password: superadmin12345

<br>


## Login Method and Instructions
1. Go to 127.0.0.1:8000/ which will open the Swagger Interactable Docs.
2. Go to the accounts/sign-in endpoint under accounts.
3. Use the following details to login:
   > username: 1234567890  
   > otp: 00000
4. Copy the access token and scroll to the top of the page, look for "Authorize" and click it.
5. Insert **Bearer {the token you copied} e.g. Bearer 2163y18hidiodj30ji30** and click "Authorize".
6. Head over to ratings tag and explore the endpoints

**Note**: Dummy data already exists in the database.


## Tests
### To run tests, use:
> python manage.py test
### It will run the tests for all the apps available.  
<br>

## Description
The GET images endpoint shows the user an image information one at a time, if it has been rated before, it won't show the image.

The POST images endpoint is to register the user's rating on a certain image
The timing and scroll features will be implemented by the front end.

There is an OTP endpoint to send the OTP before sign-in. Ask me any question on this if you do not understand.

