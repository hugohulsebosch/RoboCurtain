import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from logger import get_logger

log = get_logger(__name__)

AMSTERDAM_LAT = 52.3676
AMSTERDAM_LNG = 4.9041
TIMEZONE = "Europe/Amsterdam"
API_URL = "https://api.sunrise-sunset.org/json"


def _fetch_sun_times() -> dict:
    response = requests.get(API_URL, params={
        "lat": AMSTERDAM_LAT,
        "lng": AMSTERDAM_LNG,
        "formatted": 0,
        "tzid": TIMEZONE,
    })
    response.raise_for_status()
    data = response.json()

    if data.get("status") != "OK":
        raise RuntimeError(
            f"Sunrise-sunset API returned status: {data.get('status')}")

    return data["results"]


def get_sunrise() -> datetime:
    results = _fetch_sun_times()
    sunrise = datetime.fromisoformat(results["sunrise"])
    log.info(f"Sunrise today: {sunrise.strftime('%H:%M %Z')}")
    return sunrise


def get_sunset() -> datetime:
    results = _fetch_sun_times()
    sunset = datetime.fromisoformat(results["sunset"])
    log.info(f"Sunset today: {sunset.strftime('%H:%M %Z')}")
    return sunset


def get_sunrise_and_sunset() -> tuple[datetime, datetime]:
    """Fetch both in a single API call."""
    results = _fetch_sun_times()
    sunrise = datetime.fromisoformat(results["sunrise"])
    sunset = datetime.fromisoformat(results["sunset"])
    log.info(
        f"Sunrise: {sunrise.strftime('%H:%M %Z')}, Sunset: {sunset.strftime('%H:%M %Z')}")
    return sunrise, sunset


if __name__ == "__main__":
    sunrise, sunset = get_sunrise_and_sunset()
    print(f"Sunrise: {sunrise}")
    print(f"Sunset:  {sunset}")
