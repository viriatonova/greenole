# Measurement Sensors POC

## Content

1. [Dependencies](#dependencies)
2. [Setup](#setup)
3. [Usage](@usage)

## Dependencies

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Setup

- Development setup:

    - Create `.env` file in root dir:

        ```text
            DEBUG=<True>
            RELOAD=<True>
            API_HOST=<0.0.0.0>
            API_PORT=<80>
            DB_USER=<user>
            DB_PASSWORD=<pass>
        ```

    - run `docker-compose up`

## Usage

- Sensor Api endpoints in : `http://localhost:<API_PORT>/api/v1/dosc`

- Load test UI available in: `http://localhost:8089`
    - To configure load tests send request to: `http://api:<API_PORT>`

- Api tests are executed docker compose log on up. 