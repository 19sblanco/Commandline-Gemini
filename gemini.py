import sys
import threading
import time
import os
import argparse
from google import genai
from google.genai.types import HttpOptions
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

context_path = os.path.dirname(os.path.abspath(__file__)) + "/context.txt"

parser = argparse.ArgumentParser(description="Command-line Gemini Agent")
parser.add_argument("-s", action="store_true", help="Custom flag for your functionality")
parser.add_argument("-f", type=str, help="File to ingest")
parser.add_argument("prompt", nargs="*", help="The prompt to send")

if len(sys.argv) < 2:
    print("please provide a prompt or a file")
    sys.exit(1)

args = parser.parse_args()

s_flag_active = args.s
f_flag_value = args.f
user_prompt = " ".join(args.prompt)


file = open(context_path, "r", encoding="utf-8")
context = file.read()
file.close()

if f_flag_value:
    try:
        with open(f_flag_value, "r", encoding="utf-8") as f:
            context += "\n\n" + f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {f_flag_value}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if s_flag_active:
    context += "\n\n make your response short"

content = context + "\n\n" + user_prompt
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

