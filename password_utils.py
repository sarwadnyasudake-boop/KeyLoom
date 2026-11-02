import secrets
import string
import re

COMMON_WORDS = (
    "admin", "password", "passwd", "pass", "qwerty", "welcome",
    "login", "user", "root", "letmein", "hello", "test", "guest",
    "master", "india", "love", "dragon", "monkey", "secret", "abc", "asdf",
)

LEET_MAP = {"@": "a", "4": "a", "3": "e", "1": "i", "!": "i",
            "0": "o", "$": "s", "5": "s", "7": "t"}

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"


def _has_common_word(password):
    lowered = password.lower()
    normalized = "".join(LEET_MAP.get(char, char) for char in lowered)
    return any(word in lowered or word in normalized for word in COMMON_WORDS)


def _has_sequence(password):
    value = password.lower()
    for index in range(len(value) - 2):
        a, b, c = value[index:index + 3]
        same_type = (
            (a.isdigit() and b.isdigit() and c.isdigit())
            or (a.isalpha() and b.isalpha() and c.isalpha())
        )
        if same_type:
            x, y, z = ord(a), ord(b), ord(c)
            if (y - x == 1 and z - y == 1) or (x - y == 1 and y - z == 1):
                return True
    return False


def _is_trailing_pattern(password):
    return bool(
        re.fullmatch(r"[A-Za-z]+[^A-Za-z0-9]*[0-9]*", password)
        or re.fullmatch(r"[A-Za-z]+[0-9]*[^A-Za-z0-9]*", password)
    )


def rate_password(password):
    """Return a simple educational strength rating and improvement tips."""
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() and not char.isspace() for char in password)
    variety = sum((has_lower, has_upper, has_digit, has_symbol))

    common = _has_common_word(password)
    sequence = _has_sequence(password)
    repeated = bool(re.search(r"(.)\1\1", password))
    trailing = _is_trailing_pattern(password)

    if common or sequence or repeated or len(password) < 6 or variety < 2:
        level = "Easy"
    elif len(password) >= 8 and variety == 4 and not trailing:
        level = "Difficult"
    else:
        level = "Medium"

    tips = []
    if common:
        tips.append("Avoid common words such as password or admin, even when characters are substituted.")
    if sequence:
        tips.append("Avoid predictable sequences such as 123 or abc.")
    if repeated:
        tips.append("Avoid repeating the same character three or more times.")
    if len(password) < 12:
        tips.append("Use 12 or more characters where possible.")
    missing = []
    if not has_upper:
        missing.append("uppercase letters")
    if not has_lower:
        missing.append("lowercase letters")
    if not has_digit:
        missing.append("numbers")
    if not has_symbol:
        missing.append("symbols")
    if missing and len(tips) < 4:
        tips.append("Consider adding " + ", ".join(missing[:2]) + ".")
    if trailing and len(tips) < 4:
        tips.append("Mix character types throughout the password instead of putting numbers or symbols only at the end.")
    if len(tips) < 4:
        tips.append("Use a unique password for every account.")

    return {"level": level, "tips": tips[:4]}


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, symbols=True):
    """Generate a password using Python's cryptographically secure secrets module."""
    pools = []
    if uppercase:
        pools.append(string.ascii_uppercase)
    if lowercase:
        pools.append(string.ascii_lowercase)
    if digits:
        pools.append(string.digits)
    if symbols:
        pools.append(SYMBOLS)

    if not pools:
        raise ValueError("Select at least one character type.")
    if length < len(pools):
        raise ValueError("Password length is too short for the selected character types.")

    # Ensure at least one character from every selected pool.
    password_chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    password_chars.extend(secrets.choice(all_chars) for _ in range(length - len(password_chars)))

    # Securely shuffle so the required characters do not appear in predictable positions.
    for index in range(len(password_chars) - 1, 0, -1):
        swap_index = secrets.randbelow(index + 1)
        password_chars[index], password_chars[swap_index] = password_chars[swap_index], password_chars[index]

    return "".join(password_chars)
