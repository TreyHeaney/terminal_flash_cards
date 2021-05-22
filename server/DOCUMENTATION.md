# Flash Cards API Documentation

- [Flash Cards API Documentation](#flash-cards-api-documentation)
- [Routes](#routes)
    - [/sign_up](#sign_up)
    - [/sign_in](#sign_in)
    - [/save](#save)
- [Full Bodies](#full-bodies)
  - [Save Format](#save-format)

# Routes
### /sign_up
  *Create a new user in the database.*
  - __POST__:
    - __BODY__: 
      ```
      {
        "user": "example_username",
        "password": "epicman123"
      }
      ```
    - __RESPONSE__:
      - __SUCCESS__: 200
        ```
        {
          "message": "Login successful!",
          "authorization": "eyJhbGciOiJIUzI1NiIs..."  
        }
        ```
      - __FAIL__: 401: Bad credentials, 500: Server error.
        ```
        {
            "message": "Incorrect password." / "User not found."
        }
        ```

### /sign_in
  *Verifies a user's credentials and return an authorization.*
  - __POST__:
    - __BODY__: 
      ```
      {
        "user": "example_username",
        "password": "epicman123"
      }
      ```
    - __RESPONSE__:
      - __SUCCESS__: 201
        ```
        {
          "message": "Account successfully created! You can now sign in."
        }
        ```
      - __FAIL__: 409: Existing user, 500: Server error.
        ```
        {
          "message": "Incorrect password." / "User not found."
        }
        ```

### /save
  *Manage a user's remote save.*
  - __GET__:
    - __BODY__: 
        ```
        HEADERS
        authorization: /*Auth returned from sign_in*/
        ```
    - __RESPONSE__:
      - __SUCCESS__: 200 
        Response Body: [Save Format](#save-format)
      - __FAIL__: 401: Bad auth, 500: Server error.
        ```
        {
          "message": "Please sign in."
        }
        ```
  - __POST__:
    - __BODY__: 
      ```
      HEADERS
      authorization: /*Auth returned from sign_in*/
      ```
      Request Body: [Save Format](#save-format)
    - __RESPOSNE__:
      - __SUCCESS__: 200
        ```
        {
          "message": "Updated save!"
        }
        ```
      - __FAIL__: 401: Bad auth, 500: Server error.
        ```
        {
          "message": "Please sign in."
        }
        ```


# Full Bodies
## Save Format
```
{
  "C++":{
    "What are the curly brackets {} called? ":{
      "meta":{
        "score":1.3780037126638276,
        "wrong_streak":1,
        "last_correct":1621437158.8350954
      },
      "answers":[
        "domain",
        "area",
        "dominion",
        "body"
      ]
    },
    ...
  },
  ...
}
```