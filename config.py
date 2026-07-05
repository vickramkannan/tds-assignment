# ==========================================
# MASTER CONFIGURATION CHEAT SHEET
# Fill these in with your unique assigned values from the Exam Portal!
# ==========================================

# 1. Your IITM Email
EMAIL = "22f3000616@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-8yzo4n.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-jqikaik5.apps.exam.local"

PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY------"""

# 4. Q3: 12-Factor Config
Q3_PORT = 8732
Q3_WORKERS = 13
Q3_DEBUG = False
Q3_LOG_LEVEL = "warning"

# 5. Q5: Analytics API Key
Q5_API_KEY = "ak_45rln8w59kkg9sgnszl8ogsj"

# 6. Q9: Idempotency & Rate Limit
Q9_TOTAL_ORDERS = 57
Q9_RATE_LIMIT = 18

# 7. Q10: Middleware Rate Limit
Q10_ALLOWED_ORIGIN = "https://app-bzua3r.example.com"
Q10_RATE_LIMIT = 9  # requests per 10 seconds

# ==========================================
# FIXED VARIABLE (Do NOT change)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
