 Setup Process

### 1. Create the Django Project and App

# Install Django and Django REST Framework
pip install django
pip install djangorestframework 

# Create a new Django project
django-admin startproject social_media_api

# Navigate to the project directory
cd social_media_api

# Create a new app for user-related functionality
python manage.py startapp accounts

### 2. Configure Installed Apps

Add the following apps to `INSTALLED_APPS` in `social_media_api/settings.py`:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'accounts',
]


## Token Authentication Setup

### 1. Install SimpleJWT

pip install djangorestframework-simplejwt

### 2. Configure DRF to Use SimpleJWT

In `social_media_api/settings.py`, add the following to configure authentication classes:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

### 3. Generate and Use Tokens

#### Register Serializer

Create a serializer in `accounts/serializers.py` for user registration:

from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
```

#### Login Serializer

Create a login serializer to validate user credentials and generate tokens:

```python
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
```

#### Views

Create views to handle registration and login:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

#### URL Patterns

Add the endpoints to `accounts/urls.py`:

```python
from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
```

Include these URLs in the project-level `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
]
```

---

## Testing the API

### 1. Register a New User

- **URL**: `/api/accounts/register/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "testpassword"
  }
  ```

### 2. Login and Get Tokens

- **URL**: `/api/accounts/login/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
      "username": "testuser",
      "password": "testpassword"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "<REFRESH_TOKEN>",
      "access": "<ACCESS_TOKEN>"
  }
  ```


