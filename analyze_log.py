"""
analyze_log.py
Simple Failed Login Analyzer.

Usage:
    python3 analyze_log.py --input auth.log.sample --csv results.csv --top 20

It parses common OpenSSH auth.log failed login lines and outputs:
- summary printed to console
- CSV with columns: type, identifier, count
"""

import re
import argparse
import csv
from collections import Counter

# regex patterns for common sshd failed-auth lines
# examples:
# "Failed password for invalid user admin from 192.0.2.10 port 42312 ssh2"
# "Failed password for root from 198.51.100.5 port 51412 ssh2"
FAILED_REGEX = re.compile(
    r"Failed password for (?:(invalid user )?)(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

def parse_log(path):
    users = Counter()
    ips = Counter()
    total_failed = 0

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = FAILED_REGEX.search(line)
            if m:
                total_failed += 1
                user = m.group("user")
                ip = m.group("ip")
                users[user] += 1
                ips[ip] += 1

    return total_failed, users, ips

def write_csv(path, users, ips):
    with open(path, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["type", "identifier", "count"])
        for user, cnt in users.most_common():
            writer.writerow(["user", user, cnt])
        for ip, cnt in ips.most_common():
            writer.writerow(["ip", ip, cnt])

def print_summary(total_failed, users, ips, top=10):
    print(f"Total failed login attempts detected: {total_failed}")
    print("\nTop users with failed logins:")
    for user, cnt in users.most_common(top):
        print(f"  {user} : {cnt}")
    print("\nTop IPs with failed logins:")
    for ip, cnt in ips.most_common(top):
        print(f"  {ip} : {cnt}")

def main():
    parser = argparse.ArgumentParser(description="Simple Failed Login Analyzer")
    parser.add_argument("--input", "-i", required=True, help="Path to auth.log (or sample file)")
    parser.add_argument("--csv", "-c", default="results.csv", help="Output CSV file")
    parser.add_argument("--top", "-t", type=int, default=10, help="Top N to display")
    args = parser.parse_args()

    total_failed, users, ips = parse_log(args.input)
    print_summary(total_failed, users, ips, top=args.top)
    write_csv(args.csv, users, ips)
    print(f"\nCSV written to: {args.csv}")

if __name__ == "__main__":
    main()
