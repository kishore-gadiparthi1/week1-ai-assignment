import json
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

API_URL = "https://official-joke-api.appspot.com/jokes/random"


def fetch_joke():
    print("\n" + "=" * 50)
    print("   😂  Random Joke Fetcher — Joke API Task")
    print("=" * 50)

    try:
        print("\n🔄 Fetching joke from API...")
        request = Request(API_URL, headers={"User-Agent": "Python urllib"})
        with urlopen(request, timeout=10) as response:
            data = json.load(response)
            status_code = response.getcode()

        print("\n✅ API Response received successfully!")
        print(f"\n📦 Raw JSON Response:\n{json.dumps(data, indent=4)}")

        print("\n" + "-" * 50)
        print("🎤 Here's your joke:")
        print(f"   Setup    : {data.get('setup', '<missing>')}")
        print(f"   Punchline: {data.get('punchline', '<missing>')}")
        print("-" * 50)

        with open("api_output.txt", "w", encoding="utf-8") as f:
            f.write(f"API Task Output — {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write("=" * 50 + "\n")
            f.write(f"Endpoint: {API_URL}\n")
            f.write(f"Status Code: {status_code}\n\n")
            f.write("Raw JSON Response:\n")
            f.write(json.dumps(data, indent=4))
            f.write("\n\nFormatted Output:\n")
            f.write(f"  Type     : {data.get('type', '<missing>')}\n")
            f.write(f"  Setup    : {data.get('setup', '<missing>')}\n")
            f.write(f"  Punchline: {data.get('punchline', '<missing>')}\n")

        print("\n💾 Output saved to api_output.txt")

    except HTTPError as e:
        print(f"\n❌ HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        print("\n❌ Network Error: Could not connect to API.")
        print("   Ensure you have an active internet connection.")
        print(f"   Details: {e.reason}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    fetch_joke()
