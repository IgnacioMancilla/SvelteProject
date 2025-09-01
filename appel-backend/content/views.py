from datetime import timedelta, datetime, timezone
import jwt

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

JWT_ALG = "HS256"
JWT_EXP_MINUTES = 60  # expira en 60 min

def _make_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=JWT_EXP_MINUTES)).timestamp()),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=JWT_ALG)

def _decode_access(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[JWT_ALG])

# --- LOGIN ---
@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])  # sin SessionAuth (evita CSRF aquí)
def login_view(request):
    # Soporta JSON o form-data
    username = (request.data.get("username") or "").strip()
    password = request.data.get("password") or ""

    if not username or not password:
        return Response({"error": "username and password required"}, status=400)

    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({"error": "invalid credentials"}, status=400)

    token = _make_access_token(user.id)

    resp = Response({"ok": True}, status=200)
    resp.set_cookie(
        "access",
        token,
        httponly=True,
        samesite="Lax",   # para http://localhost front/back
        secure=False,     # en producción ponlo True si usas HTTPS
        path="/",
        max_age=JWT_EXP_MINUTES * 60,
    )
    return resp

# --- ME ---
@api_view(["GET"])
@permission_classes([AllowAny])
@authentication_classes([])   # nosotros validamos el token manualmente
def me_view(request):
    token = request.COOKIES.get("access")
    if not token:
        return Response({"detail": "unauthorized"}, status=401)

    try:
        data = _decode_access(token)
    except jwt.ExpiredSignatureError:
        return Response({"detail": "token expired"}, status=401)
    except jwt.InvalidTokenError:
        return Response({"detail": "invalid token"}, status=401)

    user_id = data.get("sub")
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "user not found"}, status=401)

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }, status=200)

# --- LOGOUT ---
@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def logout_view(request):
    resp = Response({"ok": True}, status=200)
    resp.delete_cookie("access", path="/")
    return resp
