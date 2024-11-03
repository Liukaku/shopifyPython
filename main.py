from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Union
from dotenv import load_dotenv

import os
import random
import math

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/callback", response_class=RedirectResponse)
def read_callback(q: Union[str, None] = None):
    print(q)

    def generateState(maxLength: int):
        text = ""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        for x in range(maxLength):
            text += chars[random.randrange(len(chars))]
        return text

    clientId = os.getenv("CLIENT_ID")
    scope = "user-top-read user-read-recently-played user-follow-read"
    redirect = "spotify.mattstarkey.dev"
    query = f"response_type=code&client_id={clientId}&scope={scope}&redirect_uri=https://{redirect}/callback&state={generateState(16)}"
    redirectUrl = f"https://accounts.spotify.com/en/authorize?{query}"
    return redirectUrl