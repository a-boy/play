import socket
import argparse
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
    print("Example:$ python ip_lookup_cli.py 142.250.180.14 8.8.8.8 1.1.1.1 -o my_report.html")
    parser = argparse.ArgumentParser(description="IP 情报收集器 (白金版 CLI)")
    parser.add_argument("ips", nargs="+", help="要查询的IP地址，可以输入多个")
    parser.add_argument("-o", "--output", default="ip_report.html", help="输出HTML文件名 (默认: ip_report.html)")
    args = parser.parse_args()
    
       

    results = [ip_info(ip) for ip in args.ips]
    generate_html(results, args.output)
