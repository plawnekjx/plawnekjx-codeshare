# Plawnekjx Codeshare

## Description

Plawnekjx Codeshare is allows users to share and discover Plawnekjx scripts. It provides a platform for developers to collaborate, learn, and enhance their skills in reverse engineering and dynamic instrumentation using Plawnekjx.

## Development

### Prerequisites
- Python 3.12 or higher
- pip or uv (I use uv in the below setup)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/plawnekjx/plawnekjx-codeshare
   cd plawnekjx-codeshare
    ```
2. Create a virtual environment:
   ```bash
   uv venv
   source venv/bin/activate
   ```

3. Create an environment file:
   ```bash
    SECRET_KEY="aaaa"
    AUTH0_CLIENT_SECRET="aaaa"
    DEBUG=True
   ```

3. Install the required packages:
   ```bash
   uv pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
    uv run manage.py runserver
   ```

5. Open your web browser and navigate to `http://localhost:8000` to access the Plawnekjx Codeshare web application.

## Fixtures
To load the fixtures, run the following command:

```bash
uv run manage.py loaddata plawnekjxsnippets/apps/fixtures/fixtures.json
```
