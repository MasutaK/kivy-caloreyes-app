import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# Hugging Face
HUGGINGFACE_API = "https://api-inference.huggingface.co/models/dima806/food-classification"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

HF_HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"} if HUGGINGFACE_TOKEN else {}


# Nutritionix
NUTRI_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRI_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

def analyze_image(img_path):
    try:
        # Étape 1 : Classification d'image via Hugging Face
        with open(img_path, "rb") as f:
            img_bytes = f.read()

        hf_resp = requests.post(HUGGINGFACE_API, headers=HF_HEADERS, data=img_bytes)
        hf_resp.raise_for_status()
        prediction = hf_resp.json()[0]["label"].lower()

        # Étape 2 : Nutritionix pour détails nutritionnels
        nutri_headers = {
            "x-app-id": NUTRI_APP_ID,
            "x-app-key": NUTRI_API_KEY,
            "Content-Type": "application/json"
        }

        data = {"query": prediction}
        nutri_resp = requests.post(
            "https://trackapi.nutritionix.com/v2/natural/nutrients",
            headers=nutri_headers,
            json=data
        )

        if nutri_resp.status_code == 200:
            food = nutri_resp.json()["foods"][0]
            name = food["food_name"]
            kcal = food["nf_calories"]
            prot = food["nf_protein"]
            fat = food["nf_total_fat"]
            carb = food["nf_total_carbohydrate"]

            return f"{name.title()}\n{round(kcal)} kcal\nProtéines: {prot}g\nLipides: {fat}g\nGlucides: {carb}g"
        else:
            return "Erreur Nutritionix"

    except Exception as e:
        return f"Erreur : {str(e)}"


