import json

import aiohttp
import requests
from decouple import config


async def query_external_service_async(
    url: str,
    headers: dict = None,
    params: dict = None,
) -> dict:
    """
    An asynchrnous function for getting a btc wallet's balance.
    It is important that this is done asynchronously because a user
    might run this query against thousands of wallet addresses
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                if response.headers["Content-Type"] == "application/json":
                    response = await response.json()
                else:
                    response = await response.text()
                return response

    except Exception as e:
        error = f"erro: {e}"
        response: dict = {"error": error}
        return response


async def convert_between_currencies(
    amount: float, from_currency: str, to_currency: str
) -> float:
    URL: str = config("EXCHANGE_URL")
    query_params: dict = {"from": from_currency, "to": to_currency}
    headers: dict = {"x-rapidapi-key": config("RAPID_API_KEY")}

    exchange_rate: str = await query_external_service_async(
        URL, headers=headers, params=query_params
    )

    converted_amount: float = float(amount) * float(exchange_rate)
    return converted_amount


def query_external_service_sync(
    url: str,
    http_method: str = "get",
    headers: dict = None,
    body: dict = None,
    params: dict = None,
) -> json:
    """
    A flexible resubale function that talks to third-party services synchronously.
    A service here, is usually a centralized API service
    """

    try:
        response = requests.request(
            http_method, url, data=body, headers=headers, params=params
        )
        if response.headers["content-type"] == "text/plain":
            return response.text
        else:
            return response.json()

    except Exception as e:
        return e
