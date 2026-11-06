import urllib.request, json, asyncio
import urllib.parse

# Let's find the WebSocket URL for the page target
res = urllib.request.urlopen('http://localhost:9222/json')
targets = json.loads(res.read())
page_target = None
for t in targets:
    if t.get('type') == 'page' and 'localhost:3344' in t.get('url', ''):
        page_target = t
        break

if not page_target:
    print("Page target not found")
    exit(1)

ws_url = page_target['webSocketDebuggerUrl']
print(f"Connecting to CDP: {ws_url}")

# We can use standard library or a simple script to evaluate JS via CDP
# Since websockets might or might not be installed, let's check if 'websockets' module exists
try:
    import websockets
except ImportError:
    print("Installing websockets via pip or using node script...")
    exit(2)
