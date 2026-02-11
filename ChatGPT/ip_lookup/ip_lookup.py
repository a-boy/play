import socket
import ipwhois

def ip_info(ip):
    print(f"查询 IP: {ip}")

    # 反向解析（IP -> 域名）
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"反向解析域名: {hostname}")
    except Exception as e:
        print(f"反向解析失败: {e}")

    # Whois 查询
    try:
        obj = ipwhois.IPWhois(ip)
        res = obj.lookup_rdap()
        print("\n=== Whois 信息 ===")
        print(f"组织: {res.get('network', {}).get('name')}")
        print(f"国家: {res.get('network', {}).get('country')}")
        print(f"CIDR 段: {res.get('network', {}).get('cidr')}")
        print(f"描述: {res.get('network', {}).get('remarks')}")
    except Exception as e:
        print(f"Whois 查询失败: {e}")


if __name__ == "__main__":
    test_ip = "142.250.180.14"   # 你可以换成其他IP
    ip_info(test_ip)
