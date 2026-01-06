# Level 1: Networking Basics

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Understand network fundamentals and protocols
- Work with IP addresses and subnetting
- Configure and troubleshoot DNS
- Understand HTTP/HTTPS protocols
- Use network diagnostic tools
- Configure basic firewall rules
- Troubleshoot network connectivity issues
- Understand ports and services

## 📚 Topics Covered

### 1. Network Fundamentals
- What is a network?
- Network types (LAN, WAN, Internet)
- Network topology
- Network devices (routers, switches, hubs)
- Packet switching concepts

### 2. OSI and TCP/IP Models
- OSI 7-layer model overview
- TCP/IP 4-layer model
- Layer functions and protocols
- How data flows through layers
- Practical understanding

### 3. IP Addressing
- IPv4 addressing
- IP address structure (32 bits)
- Network and host portions
- Subnet masks
- Private vs. public IPs
- CIDR notation
- IPv6 basics (introduction)

### 4. Subnetting
- Why subnetting?
- Calculating subnets
- Subnet mask calculation
- Network and broadcast addresses
- Host addresses per subnet
- Practical subnetting examples

### 5. DNS (Domain Name System)
- What is DNS?
- How DNS works
- DNS record types (A, AAAA, CNAME, MX, TXT)
- DNS resolution process
- DNS servers (recursive, authoritative)
- Configuring DNS
- Troubleshooting DNS issues

### 6. HTTP and HTTPS
- HTTP protocol basics
- HTTP methods (GET, POST, PUT, DELETE)
- HTTP status codes
- HTTP headers
- HTTPS and SSL/TLS
- Certificate concepts
- Secure connections

### 7. Ports and Services
- What are ports?
- Well-known ports (20, 21, 22, 23, 25, 53, 80, 443, etc.)
- Port ranges (0-65535)
- TCP vs. UDP ports
- Common services and their ports
- Port scanning basics

### 8. Network Tools
- **ping**: Test connectivity
- **curl**: HTTP requests
- **wget**: Download files
- **netstat**: Network connections
- **ss**: Socket statistics (modern netstat)
- **nslookup/dig**: DNS queries
- **traceroute**: Path discovery
- **telnet/nc**: Port testing

### 9. Network Configuration
- Network interfaces
- IP configuration (static vs. DHCP)
- Routing tables
- Gateway configuration
- Network configuration files (Linux)

### 10. Firewall Basics
- What is a firewall?
- Firewall types (packet filter, stateful)
- Common firewall rules
- Port blocking/allowing
- UFW basics (Uncomplicated Firewall)
- iptables introduction

### 11. Network Troubleshooting
- Connectivity issues
- DNS resolution problems
- Port accessibility
- Firewall blocking
- Network latency
- Packet loss
- Systematic troubleshooting approach

## 🎯 Exercises

### Exercise 1: Network Information
1. Find your system's IP address
2. Display network interfaces
3. Show routing table
4. Display active network connections
5. Find your default gateway

### Exercise 2: DNS Resolution
1. Use `nslookup` to resolve a domain
2. Use `dig` to query DNS records
3. Find A, AAAA, and MX records
4. Test DNS resolution speed
5. Troubleshoot a non-resolving domain

### Exercise 3: Connectivity Testing
1. Ping localhost
2. Ping your gateway
3. Ping external IP (8.8.8.8)
4. Ping a domain name
5. Test HTTP connectivity with curl
6. Test HTTPS connectivity

### Exercise 4: Port and Service Discovery
1. List listening ports on your system
2. Identify services on common ports
3. Test if a port is open
4. Check if a service is running
5. Find processes using specific ports

### Exercise 5: Network Configuration
1. Display current IP configuration
2. Show DNS servers
3. Display network statistics
4. Monitor network traffic
5. Test network speed

## 🚀 Projects

### Project 1: Network Configuration Script
Create a script that:
- Displays all network interfaces
- Shows IP addresses and netmasks
- Lists active connections
- Displays routing table
- Shows DNS servers
- Provides network statistics

**Requirements:**
- Use bash or Python
- Format output clearly
- Handle errors gracefully
- Add comments

### Project 2: DNS Resolver Tool
Create a tool that:
- Takes a domain name as input
- Resolves to IP address(es)
- Shows all DNS record types
- Tests DNS resolution time
- Handles errors (invalid domains)
- Can resolve multiple domains

### Project 3: Network Monitor
Create a monitoring script that:
- Checks connectivity to multiple hosts
- Monitors DNS resolution
- Tests HTTP/HTTPS availability
- Checks specific ports
- Logs results
- Sends alerts on failures

## 📝 Example Scripts

### Example 1: Network Information Display
```bash
#!/bin/bash
# Display network information

echo "=== Network Interfaces ==="
ip addr show
# or: ifconfig

echo -e "\n=== Routing Table ==="
ip route show
# or: route -n

echo -e "\n=== Active Connections ==="
ss -tunap
# or: netstat -tunap

echo -e "\n=== DNS Servers ==="
cat /etc/resolv.conf
```

### Example 2: Connectivity Tester
```bash
#!/bin/bash
# Test network connectivity

hosts=("8.8.8.8" "google.com" "github.com")

for host in "${hosts[@]}"; do
    echo "Testing connectivity to $host..."
    if ping -c 3 "$host" > /dev/null 2>&1; then
        echo "✓ $host is reachable"
    else
        echo "✗ $host is not reachable"
    fi
done
```

### Example 3: Port Scanner (Basic)
```bash
#!/bin/bash
# Basic port scanner

host=$1
ports=(22 80 443 3306 5432)

echo "Scanning $host..."

for port in "${ports[@]}"; do
    if timeout 1 bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null; then
        echo "Port $port: OPEN"
    else
        echo "Port $port: CLOSED"
    fi
done
```

## 🔍 Key Concepts

### IP Address Classes
- **Class A**: 1.0.0.0 to 126.255.255.255 (large networks)
- **Class B**: 128.0.0.0 to 191.255.255.255 (medium networks)
- **Class C**: 192.0.0.0 to 223.255.255.255 (small networks)
- **Private IPs**: 
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16

### Common Ports
- **20/21**: FTP
- **22**: SSH
- **23**: Telnet
- **25**: SMTP
- **53**: DNS
- **80**: HTTP
- **443**: HTTPS
- **3306**: MySQL
- **5432**: PostgreSQL

### DNS Resolution Process
1. Check local cache
2. Query local hosts file
3. Query DNS server (usually router)
4. Query ISP DNS servers
5. Query root DNS servers
6. Query TLD servers
7. Query authoritative servers
8. Return IP address

### HTTP Status Codes
- **2xx**: Success (200 OK, 201 Created)
- **3xx**: Redirection (301 Moved, 302 Found)
- **4xx**: Client Error (404 Not Found, 403 Forbidden)
- **5xx**: Server Error (500 Internal Error, 502 Bad Gateway)

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Understand network fundamentals
- [ ] Work with IP addresses and subnetting
- [ ] Configure and troubleshoot DNS
- [ ] Understand HTTP/HTTPS protocols
- [ ] Use network diagnostic tools
- [ ] Configure basic firewall rules
- [ ] Troubleshoot network connectivity
- [ ] Identify common ports and services
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

- [Linux Network Administration](https://www.linux.org/)
- [TCP/IP Guide](http://www.tcpipguide.com/)
- [DNS Explained](https://www.cloudflare.com/learning/dns/)
- `man` pages: `man ping`, `man curl`, `man netstat`, `man ss`

## 🛠️ Useful Commands

```bash
# Network information
ip addr show
ip route show
ss -tunap

# Connectivity
ping -c 4 hostname
curl -I https://example.com
wget --spider https://example.com

# DNS
nslookup domain.com
dig domain.com
host domain.com

# Port testing
nc -zv hostname port
telnet hostname port
timeout 1 bash -c "echo >/dev/tcp/host/port"

# Firewall
sudo ufw status
sudo ufw allow port
sudo iptables -L
```

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different network scenarios
2. Set up a test network environment
3. Experiment with firewall rules
4. Move to **02-infrastructure** module

---

**Remember**: Networking is fundamental to DevOps. Understanding how networks work is crucial for infrastructure management!
