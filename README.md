# FastAPI-DeliveryFeeCalculator

## Description

This is a backend solution for the preliminary assignment for the [Wolt Summer 2024 engineering internship](https://github.com/woltapp/engineering-internship-2024). The solution is a FastAPI application that calculates the delivery fee for a given order.

Project is also used as a learning opportunity for me to get familiar with FastAPI and Docker. And it is also used for some of the University of Helsinki's [DevOps with Docker](https://devopswithdocker.com) course exercises.

### Specification

Implement an HTTP API (single POST endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

#### Request

Example:

```json
{
  "cart_value": 790,
  "delivery_distance": 2235,
  "number_of_items": 4,
  "time": "2024-01-15T13:00:00Z"
}
```

##### Field details

| Field             | Type    | Description                                                                | Example value                            |
| :---------------- | :------ | :------------------------------------------------------------------------- | :--------------------------------------- |
| cart_value        | Integer | Value of the shopping cart **in cents**.                                   | **790** (790 cents = 7.90€)              |
| delivery_distance | Integer | The distance between the store and customer’s location **in meters**.      | **2235** (2235 meters = 2.235 km)        |
| number_of_items   | Integer | The **number of items** in the customer's shopping cart.                   | **4** (customer has 4 items in the cart) |
| time              | String  | Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). | **2024-01-15T13:00:00Z**                 |

#### Response

Example:

```json
{ "delivery_fee": 710 }
```

##### Field details

| Field        | Type    | Description                           | Example value               |
| :----------- | :------ | :------------------------------------ | :-------------------------- |
| delivery_fee | Integer | Calculated delivery fee **in cents**. | **710** (710 cents = 7.10€) |

## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10](https://www.python.org/downloads/release/python-380/)
- [Poetry](https://python-poetry.org/docs/)

### Steps

1. Clone the repository:

```bash
git clone
```

2. Change to the project directory:

```bash
cd FastAPI-DeliveryFeeCalculator
```

3. Install dependencies:

```bash
poetry install
```

4. Docker Compose:

```bash
docker-compose up
```
