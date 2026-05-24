from user_agents import parse
import ipinfo

ACCESS_TOKEN = ""

handler = ipinfo.getHandler(ACCESS_TOKEN)

def get_device_info(user_agent_string):

    user_agent = parse(user_agent_string)

    return {
        "browser": user_agent.browser.family,
        "os": user_agent.os.family,
        "device": user_agent.device.family
    }

def get_ip_details(ip):
    if not ip:
        return {
            "city": "Unknown",
            "country": "Unknown",
            "org": "Unknown"
        }

    # Handle local loopback and private networks locally
    if ip in ("127.0.0.1", "::1"):
        return {
            "city": "Localhost",
            "country": "Local Loopback",
            "org": "Internal Loopback Interface"
        }

    # Check for private IP spaces
    parts = ip.split(".")
    if len(parts) == 4:
        try:
            p1, p2 = int(parts[0]), int(parts[1])
            if p1 == 10 or (p1 == 192 and p2 == 168) or (p1 == 172 and 16 <= p2 <= 31):
                return {
                    "city": "Internal IP",
                    "country": "Private Network",
                    "org": "Local Area Network"
                }
        except ValueError:
            pass

    try:
        details = handler.getDetails(ip)
        return {
            "city": details.city or "Unknown",
            "country": details.country_name or "Unknown",
            "org": details.org or "Unknown"
        }
    except:
        return {
            "city": "Unknown",
            "country": "Unknown",
            "org": "Unknown"
        }