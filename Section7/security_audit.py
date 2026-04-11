import socket
import time
from datetime import datetime

# Simple vulnerability database
vulnerabilities = {
    21: "FTP may allow anonymous login",
    22: "SSH may be vulnerable to brute-force attacks",
    80: "HTTP may be vulnerable to XSS or outdated server",
    443: "HTTPS may have SSL/TLS misconfigurations"
}

# Service mapping
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

def scan_ports(target, ports):
    results = []
    print(f"\nScanning {target}...\n")

    start_time = time.time()

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"

        service = services.get(port, "Unknown")
        vuln = vulnerabilities.get(port, "No known issues")

        print(f"Port {port} ({service}): {status}")

        results.append({
            "port": port,
            "service": service,
            "status": status,
            "vulnerability": vuln if status == "OPEN" else "-"
        })

        s.close()

    duration = time.time() - start_time
    return results, duration


def generate_html(target, results, duration):
    filename = f"audit_report_{target}.html"

    with open(filename, "w") as f:
        f.write(f"""
        <html>
        <head>
            <title>Security Audit Report</title>
            <style>
                body {{ font-family: Arial; }}
                table {{ border-collapse: collapse; width: 80%; }}
                th, td {{ border: 1px solid black; padding: 8px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h2>Security Audit Report</h2>
            <p><b>Target:</b> {target}</p>
            <p><b>Date:</b> {datetime.now()}</p>
            <p><b>Scan Duration:</b> {duration:.2f} seconds</p>

            <table>
                <tr>
                    <th>Port</th>
                    <th>Service</th>
                    <th>Status</th>
                    <th>Vulnerability</th>
                </tr>
        """)

        for r in results:
            f.write(f"""
                <tr>
                    <td>{r['port']}</td>
                    <td>{r['service']}</td>
                    <td>{r['status']}</td>
                    <td>{r['vulnerability']}</td>
                </tr>
            """)

        f.write("""
            </table>
        </body>
        </html>
        """)

    print(f"\nReport saved as {filename}")


# ---- Main ----
target = input("Enter target IP: ")
ports = [21, 22, 80, 443]

results, duration = scan_ports(target, ports)
generate_html(target, results, duration)
