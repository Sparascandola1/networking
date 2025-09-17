import socket
import pandas as pd

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host,port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        #print(f"[+] Port {port} is OPEN\n    Banner: {banner}")            
        return [port, banner]
    except (socket.timeout, ConnectionRefusedError):
        pass
        # print(f"[-] Port {port} is CLOSED")
    finally:
        s.close()

def scan_host(host, start_port, end_port):
    arr = []
    print(f"Scanning {host} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        if port % 5 == 0:
            print(f"Scanning port {port}...")
        arr.append(scan_port(host, port))
    arr = [x for x in arr if x is not None]
    print_frame(arr)

def print_frame(data):
    df = pd.DataFrame(data, columns=["Port", "Banner"])
    print(df)

if __name__ == "__main__":
    target_host = "scanme.nmap.org"
    scan_host(target_host, 20, 25)
