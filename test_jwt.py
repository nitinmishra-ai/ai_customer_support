from app.core.jwt import create_access_token

token = create_access_token({
    "sub": "john@gmail.com",
    "user_id": 1
})

print(token)

