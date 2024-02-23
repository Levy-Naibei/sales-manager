# Backend developer screening test

- This a DRF api for uploading customers and orders.
- SMS is sent to customer when order is made

## Requirements

- Docker
- OpenID connect provider of your choice e.g Okta, Google, 
- Africa's Talking

## Gettting started(Docker Locally)

- add env vars as shown .env.sample file
- Run `make build`
- Run `make superuser`
- Taste the api endpoints on postman from port `8000`

## Docker commands

- Build and run containers: `make build`
- Run tests: `make test`
- Run Test Coverage: `make test-coverage`
- Run Test coverage report: `make test-report`
- See HTML format of test report: `make test-html`

    - See `Makefile` file for other CMDs


## Create an OIDC app in Okta

  - [Sign in](https://developer.okta.com/login/) to your Admin Console as a user with administrative privileges
  - In the Admin Console, go to `Applications > Applications`.
  - Click `Create App Integration`.
  - On the Create a new app integration page, `select OIDC - OpenID Connect as the Sign-in method`. 
  - Choose `Web Application` for the Application type. Click `Next`.
  - Enter a name for your app integration.
  - For the `Grant type`, leave the default of `Authorization Code grant flow`.
  - In the `Sign-in redirect URIs` box, specify the callback location where Okta returns a browser (along with the token) after the user finishes authenticating.
  - In the `Assignments section`, select `everyone` for testing purposes.
  - Click `Save`. The settings page for the app integration appears, showing the General tab. Make note of the `Client ID` and `Client secret` listed in the Client Credentials section. You need this information for the `Get an access token` and `make a request` task.
  - Select the `Okta API Scopes tab` and then click Grant for each of the scopes that you want to add to the app grant collection. Ensure that you grant the scopes for the API access you require.

## Get Authorisation Code

- `Note`: Authorization code is `One time` and expires after `300` seconds
- See some URL parameter values are from Okta app set up above
- Go to your browser and put this URL:

     https://`<your-okta-domain>`/oauth2/v1/authorize?response_type=`code`&        scope=`<scope-selected-during-okta-setup>`&
        client_id=`<your-okta-cleint-id>`&
        redirect_uri=`<sign-redirect-url>`&
        state=`<your-value>`&
        nonce=`<your-value>`

- This opens a OKTA login Widget, put your okta `username` and `passwaord`
- Okta returns a browser (along with the token) after the user finishes authenticating; Extract the code from redirect url code parameter 

## Get access token 

`Note`: The token expires after `3600` seconds
Endpoint: `https://localhost:8000/oauth2/v1/token`

- Launch Postman desktop app
  - Click `Authorization Tab` 
  - Add username=`{clientid}` & password=`{clientsecret}`
  - Click on `Body Tab` 
  - Add `Authentication code` and `redirect_uri` on the token request body

## Make request
- POST requests API Endpoints shown on the table below
  - Click on `Authorization Tab`
  - Select `Bearer token`
  - Paste the token from response above


## API endpoints

| Endpoint                                                      | FUNCTIONALITY                            |
| ------------------------------------------------------------- | :--------------------------------------- |
| POST &emsp;&emsp; ap1/v1/sales/create-customer/               | This creates customer                    |
| POST &emsp;&emsp; ap1/v1/sales/create-order/                  | This creates/makes order                 |
| GET &emsp;&emsp; ap1/v1/sales/customers/                      | This gets all customers                  |
| GET &emsp;&emsp; ap1/v1/sales/orders/                         | This gets all orders                     |

### Create Customer

`POST ap1/v1/sales/create-customer/`

Example request body:

```application/json
  {
    "name":"john doe",
    "phone_number": "+254704590344",
    "email": "example@gmail.com"
  }
```

Authentication required, returns a customer
Required fields: `name`, `phone_number`, `email`
`Note`: Customer `Code` is automatically generated when customer instance is saved

### Create Order

`POST ap1/v1/sales/create-order/`

Example request body:

```application/json
  {
    "customer": "customer id",
    "item": "macbook m2",
    "amount": "56000.68"
  }
```

Authentication required, returns an order
Required fields: `customer`, `item`, `amount`
`Note`: Order date is populated automatically when order is made


## AFRICA'S TALKING

- Live phone numbers cannot be used or use service in real life since we are on sandbox;
- Thus, you may see status delivery failed
- View the SMSs sent when order is made: [SMS](https://account.africastalking.com/apps/sandbox/sms/bulk/outbox)

## Credit

- [Okta Documentation](https://help.okta.com/oie/en-us/content/topics/apps/apps_apps.htm)