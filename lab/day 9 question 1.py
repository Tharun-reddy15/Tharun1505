# =========================
# BASIC PYTHON AUTOMATION FRAMEWORK (SINGLE FILE)
# =========================

# ---------- Configuration ----------
class Config:
    ENVIRONMENT = "QA"
    APP_NAME = "Python Automation Framework"


# ---------- Utilities ----------
def add(a, b):
    return a + b


# ---------- Test Cases (pytest) ----------
def test_addition():
    assert add(4, 6) == 10