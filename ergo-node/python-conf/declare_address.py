import requests
from Operations import write_declared_address


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')

        if response.status_code == 200:
            public_ip = response.text
            return public_ip
        else:
            print(f"Failed to get public IP: {response.status_code}")
            return None
    except requests.exceptions.RequestException as error:
        print(f"Error occurred: {error}")
        return None


def update_config_file():
    public_ip = get_public_ip()

    if public_ip:
        address = public_ip + ':9030'

        write_declared_address(address, 'ergo.conf')
    else:
        print("Public IP is not available. Configuration file is not updated.")


if __name__ == "__main__":
    update_config_file()
