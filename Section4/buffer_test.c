#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];   // Buffer of size 16
    char input[100];   // Larger input buffer

    printf("Enter some text: ");
    gets(input);   // Taking user input (unsafe)

    // Unsafe copy using strcpy()
    strcpy(buffer, input);

    printf("You entered: %s\n", buffer);

    return 0;
}

/*
==================== ANSWERS ====================

1. What happens with long input?
--------------------------------
If the user enters more than 16 characters (e.g., 30+ characters),
the extra data overflows the buffer and overwrites adjacent memory.
This can cause:
- Program crash (segmentation fault)
- Unexpected behavior
- Corruption of data

2. Why is this dangerous?
-------------------------
Buffer overflow is dangerous because:
- It can overwrite important memory (like return addresses)
- Attackers can exploit it to execute malicious code
- It leads to security vulnerabilities in programs

3. How would you fix it?
------------------------
Use safer alternatives that limit input size:
- fgets(input, sizeof(input), stdin);
- strncpy(buffer, input, sizeof(buffer) - 1);
- Avoid using strcpy() and gets()

Example fix:
    fgets(input, sizeof(input), stdin);
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[15] = '\0';

================================================
*/
