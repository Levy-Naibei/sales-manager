# Backend developer screening test

- This a DRF api for uploading customers and orders.
- SMS is sent to customer when order is made

## Requirements

- Docker
- OpenID connect provider of your choice e.g Okta, Google, 
- Africa's Talking
- 

## Gettting started(Docker Locally)

- add env vars as shown .env.sample file
- Taste the endpoints on postman/browser

## Docker commands

- See `Makefile` e.g to build containers run `make build`

## API endpoints


## AFRICA'S TALKING

- Live phone numbers cannot be used or use service in real life since we are on sandbox;
- Thus, you may see status delivery failed
- View the SMSs sent when order is made: [SMS](https://account.africastalking.com/apps/sandbox/sms/bulk/outbox)

## Deployed App

- Find the link: [savanah]()
- Test the various enpoints on browser/postman