# Footbal World(FOWO) Fantasy Football API Documentation

Thanks for using the Footbal World API. This is your one-stop-shop for accessing data from our fantasy football website, www.sportsworldcentral.com.


## Table of Contents

- [Public API](#public-api)
- [Getting Started](#getting-started)
  - [Analytics](#analytics)
  - [Player](#player)
  - [Scoring](#scoring)
  - [Membership](#membership)
- [Terms of Service](#terms-of-service)
- [Example Code](#example-code)
- [Software Development Kit (SDK)](#software-development-kit-sdk)

## Public API

Our API is hosted at [API URL]/([API URL]/). 

You can access the interactive documentation at [[API URL]/docs]([API URL]/docs).

You can view the OpenAPI Specification (OAS) file at [[API URL]/openapi.json]([API URL]/openapi.json).

## Getting Started

Since all of the data is public, the FOWO API doesn't require any authentication. All of the the following data is available using GET endpoints that return JSON data.

### Analytics

Get information about health of the API and counts of leagues, teams, and players.

### Player
You can get a list of an NFL players, or search for an individual player by player_id.

### Scoring

You can get a list of NFL player performances, including the fantasy points they scored using FOWO league scoring.

### Membership
Get information about all the FOWO fantasy football leagues and the teams in them.

## Terms of Service

By using the API, you agree to the following terms of service:

- **Usage Limits**: You are allowed up to 2000 requests per day. Exceeding this limit may result in your API key being suspended.
- **Data Ownership**: You can use the data however you like as long as you give credit to Footbal World.
- **No Warranty**: We don't provide any warranty of the API or its operations.

## Example Code

Here is some Python example code for accessing the health check endpoint:

```
import httpx

HEALTH_CHECK_ENDPOINT = "/"
    
with httpx.Client(base_url=self.FOWO_base_url) as client:
    response = client.get(self.HEALTH_CHECK_ENDPOINT)
    print(response.json())
```

## Software Development Kit (SDK)
*Coming Soon*

Check back for the Python SDK for our API.

