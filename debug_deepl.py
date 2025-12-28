
import logging
import deepl
import os
import sys

# Setup logging
logging.basicConfig(level=logging.DEBUG)

def debug_deepl():
    print("Beginning DeepL Debug...")
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        # Fallback for local testing if env var not set, for user just say it's missing
        print("DEEPL_API_KEY missing!")
        return

    print(f"Key found: {api_key[:5]}...")
    
    server_url = None
    if api_key.endswith(':fx'):
        server_url = "https://api-free.deepl.com"
        print("Using Free API URL")
    else:
        print("Using Pro API URL")

    try:
        # Create translator manually to ensure we see what's happening
        if server_url:
            translator = deepl.Translator(auth_key=api_key, server_url=server_url)
        else:
            translator = deepl.Translator(auth_key=api_key)
            
        print("Translator created. Attempting usage call...")
        usage = translator.get_usage()
        print(f"Usage: {usage}")
        
        print("Attempting translation...")
        result = translator.translate_text("Hello World", target_lang="ZH")
        print(f"Translation result: {result.text}")
        
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_deepl()
