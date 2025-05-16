# ITHub Autotest

## Required
- Docker desktop;
- python 3.10+;
- pip;
- Google Chrome и chromedriver;

## Setup
- `OPENCART_PORT=8081 PHPADMIN_PORT=8888 OPENCART_HOST=localhost docker compose up -d`;
- Откройте браузер по пути `localhost:8081`;
- `python3 -m venv ftai_venv && source ftai_venv/bin/activate`;
- `pip install --upgrade pip`;
- `pip install -r requirements.txt`;

## Run test
- `pytest`;