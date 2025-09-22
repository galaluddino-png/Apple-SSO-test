# Apple SSO Django Project

A standalone Django project configured for Apple Sign-In (SSO) authentication.

## Quick Start

### 1. Start the project with Docker:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

The app will be available at `http://localhost:8001`

### 2. Configure Apple SSO

Update these values in `apple_sso_project/settings.py`:

- `SOCIAL_AUTH_APPLE_ID_CLIENT`: Your Service ID from Apple
- `SOCIAL_AUTH_APPLE_ID_TEAM`: Your Team ID
- `SOCIAL_AUTH_APPLE_ID_KEY`: Your Key ID
- `SOCIAL_AUTH_APPLE_ID_SECRET`: Your private key content

### 3. Apple Developer Console Setup

1. Go to [Apple Developer](https://developer.apple.com)
2. Configure your Service ID with redirect URL:
   - For local testing with ngrok: `https://YOUR_NGROK_URL/social-auth/complete/apple-id/`
   - For staging: `https://YOUR_DOMAIN/social-auth/complete/apple-id/`

### 4. Testing with ngrok (for local HTTPS)

```bash
# Install ngrok
# Run ngrok to tunnel to your local server
ngrok http 8001

# Use the HTTPS URL provided by ngrok in Apple configuration
```

## Endpoints

- **Home**: `http://localhost:8001/` - Shows available endpoints
- **Start Login**: `http://localhost:8001/social-auth/login/apple-id/`
- **Callback**: `http://localhost:8001/social-auth/complete/apple-id/`
- **User Info**: `http://localhost:8001/auth/user/`
- **Logout**: `http://localhost:8001/auth/logout/`

## Testing

1. Visit `http://localhost:8001/templates/test.html` for a test interface
2. Click "Sign in with Apple" to test the authentication flow

## Project Structure

```
apple-sso-django/
├── apple_sso_project/
│   ├── settings.py      # Main settings with Apple SSO config
│   ├── urls.py          # URL routing
│   └── wsgi.py
├── authentication/      # Auth app with views and models
│   ├── views.py        # Authentication endpoints
│   ├── models.py       # User profile model
│   └── urls.py
├── templates/
│   └── test.html       # Test page for Apple SSO
├── docker-compose.dev.yml
├── Dockerfile
└── requirements.txt
```

## Troubleshooting

- **Invalid redirect_uri**: Make sure the URL in Apple Console exactly matches your callback URL
- **HTTPS required**: Apple requires HTTPS. Use ngrok for local testing
- **Key format**: The private key should include BEGIN/END markers

## Environment Variables

The project uses these database settings (configured in docker-compose):
- Database: `applesso_db`
- User: `applessouser`
- Password: `applessopass`
- Port: `5433` (external), `5432` (internal)