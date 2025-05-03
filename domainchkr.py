import whois
import time
import sys
import random
from colorama import init, Fore, Style
import string

# Initialize colorama for cross-platform colored output
init()

def terminal_flicker():
    """Simulate a 90s CRT terminal boot-up flicker with static"""
    chars = string.ascii_letters + string.digits + "/\\|+-*"
    width = 50
    for _ in range(5):
        for _ in range(4):
            line = ''.join(random.choice(chars) for _ in range(width))
            print(Fore.GREEN + Style.DIM + line + Style.RESET_ALL)
            time.sleep(0.02)
        print(Fore.BLACK + Style.BRIGHT + "[STATIC...]" + Style.RESET_ALL)
        time.sleep(0.08)
    print(Fore.GREEN + Style.BRIGHT + "[TRB CORE v95 BOOTED]" + Style.RESET_ALL)
    time.sleep(0.2)

def dial_up_sequence():
    """Simulate a 90s dial-up modem connection"""
    print(Fore.GREEN + "[INITIATING DIAL-UP...]")
    dial_sounds = ["BEEP...", "SCREEEEE...", "KSHHHH...", "CONNECT 28800 BPS"]
    for sound in dial_sounds:
        sys.stdout.write(Fore.GREEN + Style.DIM + sound)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 20 + "\r")
        sys.stdout.flush()
    print(Fore.GREEN + Style.BRIGHT + "[CONNECTED TO TRB NET]" + Style.RESET_ALL)
    time.sleep(0.15)

def glitch_text(text, repeat=3):
    """Display text with a glitchy, distorted 90s terminal effect"""
    for _ in range(repeat):
        sys.stdout.write("\r" + Fore.GREEN + "".join(random.choice([ seeding, random.choice(string.ascii_letters)]) for seeding in text))
        sys.stdout.flush()
        time.sleep(0.03)
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.flush()
    sys.stdout.write("\r" + Fore.GREEN + text + Style.RESET_ALL)
    time.sleep(0.1)

def scan_bar():
    """Display a blocky, 90s-style scan progress bar with flicker"""
    bar = "[          ]"
    for _ in range(2):
        for i in range(1, 11):
            sys.stdout.write(f"\r{Fore.GREEN}[{'#' * i}{' ' * (10 - i)}]{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.07)
            if random.random() < 0.2:  # Random flicker
                sys.stdout.write(f"\r{Fore.GREEN + Style.DIM}[{'#' * i}{' ' * (10 - i)}]{Style.RESET_ALL}")
                sys.stdout.flush()
                time.sleep(0.02)
        for i in range(9, -1, -1):
            sys.stdout.write(f"\r{Fore.GREEN}[{'#' * i}{' ' * (10 - i)}]{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.07)
    print()

def hex_dump():
    """Simulate a 90s-style hex data dump animation"""
    hex_chars = "0123456789ABCDEF"
    for _ in range(3):
        line = " ".join("".join(random.choice(hex_chars) for _ in range(2)) for _ in range(8))
        print(Fore.GREEN + Style.DIM + f"0x{random.randint(1000, 9999):04X}: {line}" + Style.RESET_ALL)
        time.sleep(0.05)
    print(Fore.GREEN + "[HEX DUMP COMPLETE]" + Style.RESET_ALL)
    time.sleep(0.1)

def blinking_cursor(text, cycles=3):
    """Display text with a blinking cursor effect"""
    for _ in range(cycles):
        sys.stdout.write("\r" + Fore.GREEN + text + "_" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\r" + Fore.GREEN + text + " " + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r" + Fore.GREEN + text + Style.RESET_ALL)
    sys.stdout.flush()

def hacker_banner():
    """Display a raw, 90s-style hacker banner with animations"""
    terminal_flicker()
    dial_up_sequence()
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)
    blinking_cursor(" " * 10 + "DOMAIN CHECKER")
    glitch_text(" " * 10 + "TOOL BY ALI HACKER 95")
    blinking_cursor(" " * 10 + "POWER BY TRB")
    print(Fore.GREEN + Style.BRIGHT + "=" * 50)
    print(Fore.GREEN + """
       ________________________
      /  DROP A DOMAIN TO HACK  \\
      \  TRB CORE v95 LOADED  /
       ------------------------
    """ + Style.RESET_ALL)
    time.sleep(0.2)

def get_domain_info(domain):
    """Fetch and display domain info with 90s hacker animations"""
    try:
        print(Fore.GREEN + "\n[TRB SCANNING TARGET...]")
        scan_bar()
        print(Fore.GREEN + "[TARGET ACQUIRED]")
        hex_dump()
        
        domain_info = whois.whois(domain)
        print(Fore.GREEN + Style.BRIGHT + "\n[EXTRACTING RAW DATA]" + Style.RESET_ALL)
        print(Fore.GREEN + "-" * 40)
        
        # Random hacker phrases with blinking cursor
        hacker_phrases = ["[TRB BREACH EXECUTED]", "[DATA RIP INITIATED]", "[CORE HACK DEPLOYED]"]
        blinking_cursor(random.choice(hacker_phrases))
        
        # ASCII art for output
        print(Fore.GREEN + """
        +-------------------+
        | TRB DATA DUMP     |
        +-------------------+
        """)
        
        for key, value in domain_info.items():
            if value:  # Only display non-empty values
                glitch_text(f"[{key.upper()}]: {value}")
        print(Fore.GREEN + "-" * 40)
        
    except Exception as e:
        print(Fore.GREEN + f"\n[TRB ERROR]: {e}")
        glitch_text("[SYSTEM CRASH DETECTED]", repeat=2)
        print(Fore.GREEN + """
        +-------------------+
        |  CORE FAILURE     |
        +-------------------+
        """)

def main():
    hacker_banner()
    while True:
        domain = input(Fore.GREEN + Style.BRIGHT + ">> TARGET DOMAIN: " + Style.RESET_ALL).strip()
        if not domain:
            blinking_cursor("[ERROR]: NO TARGET DETECTED")
            continue
        get_domain_info(domain)
        retry = input(Fore.GREEN + "\n[REBOOT TRB CORE? (y/n)]: " + Style.RESET_ALL).lower()
        if retry != 'y':
            print(Fore.GREEN + "[SHUTTING DOWN TRB...]")
            glitch_text("[SYSTEM TERMINATED]", repeat=2)
            print(Fore.GREEN + """
            +-------------------+
            | TRB CORE OFFLINE  |
            +-------------------+
            """)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n[TRB ALERT]: CTRL+C DETECTED...")
        blinking_cursor("[EMERGENCY SHUTDOWN]")
        print(Fore.GREEN + """
        +-------------------+
        | TRB CORE HALTED   |
        +-------------------+
        """)
