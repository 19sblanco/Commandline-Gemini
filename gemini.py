import sys
import threading
import time
import os
from google import genai
from google.genai.types import HttpOptions
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

context_path = os.path.dirname(os.path.abspath(__file__)) + "/context.txt"

if len(sys.argv) < 2:
    print("please provide a prompt")
    sys.exit(1)

file = open(context_path, "r", encoding="utf-8")
context = file.read()
file.close()

content = context + sys.argv[1]
is_waiting = True

def run_spinner():
    symbols = ["|", "/", "-", "\\"]
    sys.stdout.write("Thinking...")
    while is_waiting:
        for symbol in symbols:
            if not is_waiting:
                break
            sys.stdout.write(symbol)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
    # clear the "Thinking..." text when finished
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

spinner_thread = threading.Thread(target=run_spinner)
spinner_thread.start()

console = Console()

try:
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=content,
    )

    response_iter = iter(response)

    try:
        first_chunk = next(response_iter)
        
        is_waiting = False
        spinner_thread.join()

        full_text = first_chunk.text or ""

        # Use Rich's Live feature to update the markdown render continuously
        with Live(Markdown(full_text), console=console, refresh_per_second=15) as live:
            for chunk in response_iter:
                if chunk.text:
                    full_text += chunk.text
                    live.update(Markdown(full_text))

    except StopIteration:
        is_waiting = False
        spinner_thread.join()
                
except Exception as e:
    is_waiting = False
    spinner_thread.join()
    print(f"\nError: {e}")

