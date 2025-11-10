#!/usr/bin/env python3
import requests

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"


def fetch_joke():
    """
    Interroge JokeAPI et renvoie une blague formatée (str).
    Lève une RuntimeError en cas de problème.
    """
    try:
        response = requests.get(
            JOKE_API_URL,
            params={
                "safe-mode": "false",
            },
            timeout=5,
        )
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erreur réseau lors de l'appel à JokeAPI : {e}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Réponse invalide de JokeAPI (code HTTP {response.status_code})"
        )

    data = response.json()

    if data.get("error"):
        # JokeAPI renvoie "error": true en cas de problème
        raise RuntimeError(f"Erreur renvoyée par JokeAPI : {data}")

    joke_type = data.get("type")

    if joke_type == "single":
        # Blague en une seule partie
        joke = data.get("joke", "").strip()
        if not joke:
            raise RuntimeError("Format de blague 'single' invalide.")
        return joke

    elif joke_type == "twopart":
        # Blague en deux parties : setup + delivery
        setup = data.get("setup", "").strip()
        delivery = data.get("delivery", "").strip()
        if not setup or not delivery:
            raise RuntimeError("Format de blague 'twopart' invalide.")
        return f"{setup}\n{delivery}"

    else:
        raise RuntimeError(f"Type de blague inconnu : {joke_type}")


def main():
    print("=== JokeAPI client (Python) ===")
    try:
        joke = fetch_joke()
    except RuntimeError as e:
        print(f"Erreur : {e}")
        return

    print("\nVoici une blague pour toi :\n")
    print(joke)


if __name__ == "__main__":
    main()
