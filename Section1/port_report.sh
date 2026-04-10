#!/bin/bash

# Check if target IP is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

TARGET=$1
DATE=$(date +%Y-%m-%d)
OUTPUT="scan_${TARGET}_${DATE}.txt"

echo "===== PORT SCAN REPORT =====" > $OUTPUT
echo "Target: $TARGET" >> $OUTPUT
echo "Date: $(date)" >> $OUTPUT
echo "----------------------------" >> $OUTPUT

# Ports to scan
PORTS=(21 22 80 443 3306)

OPEN_COUNT=0

echo "Scanning ports..." 

for PORT in "${PORTS[@]}"
do
    timeout 1 bash -c "echo > /dev/tcp/$TARGET/$PORT" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "Port $PORT is OPEN" | tee -a $OUTPUT
        ((OPEN_COUNT++))
    else
        echo "Port $PORT is CLOSED" >> $OUTPUT
    fi
done

echo "----------------------------" >> $OUTPUT
echo "Total OPEN ports: $OPEN_COUNT" | tee -a $OUTPUT
echo "Report saved to: $OUTPUT"
