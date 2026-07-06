#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from patchright.sync_api import sync_playwright

print("Connecting to Chrome at port 9222...")
playwright = sync_playwright.start()

try:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    print("OK Connected!")
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    pages = context.pages
    print(f"Found {len(pages)} tabs")
    
    for page in pages:
        if "notebooklm.google.com" in page.url:
            print(f"OK Found NotebookLM: {page.url}")
            page.wait_for_load_state("networkidle")
            print("Automation ready!")
            break
    else:
        print("Opening NotebookLM...")
        page = context.new_page()
        page.goto("https://notebooklm.google.com", timeout=60000)
        print("OK Ready!")
        
except Exception as e:
    print(f"FAIL: {e}")
    print("Start Chrome with: chrome.exe --remote-debugging-port=9222")
finally:
    print("Press Ctrl+C to exit")
    try: input()
    except: playwright.stop()