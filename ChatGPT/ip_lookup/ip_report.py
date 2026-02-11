import socket
from ipwhois import IPWhois
import datetime

def ip_info(ip):
    """查询单个IP的反向解析和Whois信息"""
    info = {"ip": ip, "hostname": "-", "org": "-", "country": "-", "cidr": "-", "desc": "-"}

    # 反向解析
    try:
        info["hostname"] = socket.gethostbyaddr(ip)[0]
    except Exception:
        pass

    # Whois 查询
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        net = res.get("network", {})
        info["org"] = net.get("name", "-")
        info["country"] = net.get("country", "-")
        info["cidr"] = net.get("cidr", "-")
        info["desc"] = str(net.get("remarks", "-"))
    except Exception:
        pass

    return info


def generate_html(results, filename="ip_report.html"):
    """生成HTML报告"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>IP 情报报告</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>IP 情报报告</h1>
        <p>生成时间: {now}</p>
        <table>
            <tr>
                <th>IP</th>
                <th>反向解析域名</th>
                <th>组织</th>
                <th>国家</th>
                <th>CIDR</th>
                <th>描述</th>
            </tr>
    """

    for r in results:
        html += f"""
            <tr>
                <td>{r['ip']}</td>
                <td>{r['hostname']}</td>
                <td>{r['org']}</td>
                <td>{r['country']}</td>
                <td>{r['cidr']}</td>
                <td>{r['desc']}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[+] 报告已生成: {filename}")


if __name__ == "__main__":
    # 你可以在这里批量放IP
    ip_list = [
        "142.250.180.14",  # Google
        "8.8.8.8",         # Google DNS
        "1.1.1.1",         # Cloudflare DNS
        "208.67.222.222"   # OpenDNS
    ]

    results = [ip_info(ip) for ip in ip_list]
    generate_html(results)
