#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

// Function to scan a single port
void scan_port(char *ip, int port) {
    int sock;
    struct sockaddr_in target;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        printf("Socket creation failed\n");
        return;
    }

    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr(ip);

    // Try to connect
    int result = connect(sock, (struct sockaddr *)&target, sizeof(target));

    if (result == 0) {
        printf("Port %d: OPEN\n", port);
    } else {
        printf("Port %d: CLOSED\n", port);
    }

    close(sock);
}

int main() {
    char *target_ip = "127.0.0.1";

    int ports[] = {22, 80, 443, 3306};
    int num_ports = sizeof(ports) / sizeof(ports[0]);

    printf("Scanning localhost (%s)...\n\n", target_ip);

    for (int i = 0; i < num_ports; i++) {
        scan_port(target_ip, ports[i]);
    }

    return 0;
}
