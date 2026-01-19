from playwright.sync_api import sync_playwright
import json

def test_get_all_products():
    with sync_playwright() as p:
        # Launch a browser (not really needed for API, but required to start context)
        browser = p.chromium.launch()
        context = browser.new_context()

        # Make API request
        response = context.request.get("https://automationexercise.com/api/productsList")

        # Check status code
        print("Status Code:", response.status)
        assert response.status == 200, "Expected status code 200"

        # Parse response JSON
        data = response.json()
        print("Response JSON:", json.dumps(data, indent=2))

        # Simple validation: check "products" key exists
        assert "products" in data, "Expected 'products' key in response"

        browser.close()

if __name__ == "__main__":
    test_get_all_products()
