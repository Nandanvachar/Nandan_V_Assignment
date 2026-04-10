#include <stdio.h>

int main() {
    // Create an integer variable
    int port = 80;

    // Create a pointer to port
    int *ptr = &port;

    // Print port value using variable
    printf("Port value (using variable): %d\n", port);

    // Print port value using pointer
    printf("Port value (using pointer): %d\n", *ptr);

    // Change port to 443 using pointer
    *ptr = 443;

    // Print new value
    printf("Updated port value: %d\n", port);

    return 0;
}
