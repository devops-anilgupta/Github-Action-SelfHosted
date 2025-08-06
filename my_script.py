import socket
import requests

def get_private_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_public_ip():
    try:
        return requests.get("https://ifconfig.me", timeout=3).text.strip()
    except Exception as e:
        return f"Error getting public IP: {e}"

if __name__ == "__main__":
    print("✅ Running Python script on EC2 GitHub Actions Runner...")
    
    private_ip = get_private_ip()
    print(f"🌐 Private IP Address: {private_ip}")
    
    public_ip = get_public_ip()
    print(f"🌍 Public IP Address: {public_ip}")
