from fastapi import FastAPI


app = FastAPI(
    title="CPM MALIK API",
    version="1.0.0"
)


@app.get("/")
async def home():

    return {
        "success": True,
        "message": "CPM MALIK API is online."
    }


@app.get("/health")
async def health():

    return {
        "success": True,
        "status": "online"
    }


@app.get("/services")
async def services():

    return {
        "success": True,
        "services": [
            "set_coins",
            "set_money",
            "change_password",
            "change_email",
            "change_id",
            "change_name",
            "race_win_lose",
            "unlock_smoke",
            "unlock_w16",
            "unlock_horns",
            "wardrobe",
            "no_damage",
            "unlimited_fuel",
            "premium_wheels",
            "animations",
            "fix_account"
        ]
    }