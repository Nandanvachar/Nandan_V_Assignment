import socket
import time

def scan_ports(target, ports):
    results = []
    open_count = 0

    print(f"\nScanning Target: {target}")
    print("Scanning ports...\n")

    start_time = time.time()

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            status = "OPEN"
            open_count += 1
        else:
            status = "CLOSED"

        print(f"Port {port}: {status}")
        results.append(f"Port {port}: {status}")

        s.close()

    end_time = time.time()
    duration = end_time - start_time

    # Save results to file
    with open("scan_results.txt", "w") as f:
        f.write(f"Target: {target}\n")
        f.write("Scan Results:\n")
        for line in results:
            f.write(line + "\n")
        f.write(f"\nTotal OPEN ports: {open_count}\n")
        f.write(f"Scan Duration: {duration:.2f} seconds\n")

    print("\nScan completed!")
    print(f"Total OPEN ports: {open_count}")
    print(f"Scan Duration: {duration:.2f} seconds")
    print("Results saved to scan_results.txt")


# ---- Main Program ----
target = input("Enter target IP: ")

ports_input = input("Enter ports (comma-separated, e.g., 21,22,80): ")
ports = [int(p.strip()) for p in ports_input.split(",")]

scan_ports(target, ports)
