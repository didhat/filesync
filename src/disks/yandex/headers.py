

def get_header_for_request(token: str):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"OAuth {token}",
    }
    return headers
