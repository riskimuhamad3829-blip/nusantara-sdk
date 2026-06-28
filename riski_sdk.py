#!/usr/bin/env python3
import sys
import os
import urllib.request
import urllib.parse
import json
import argparse

def create_lang(name):
    print(f"Membuat struktur bahasa pemrograman baru: {name}...")
    os.makedirs(name, exist_ok=True)
    
    # Template Lexer
    lexer_code = f'''class Lexer:
    def __init__(self, text):
        self.text = text
    def get_tokens(self):
        # TODO: Implementasikan logika pemecahan token di sini
        return []
'''
    with open(f"{name}/lexer.py", "w") as f: 
        f.write(lexer_code)
    
    # Template Parser
    parser_code = f'''class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
    def parse(self):
        # TODO: Implementasikan logika parsing AST di sini
        return None
'''
    with open(f"{name}/parser.py", "w") as f: 
        f.write(parser_code)
    
    # Template Interpreter
    interpreter_code = f'''class Interpreter:
    def run(self, ast):
        # TODO: Implementasikan eksekusi AST di sini
        pass
'''
    with open(f"{name}/interpreter.py", "w") as f: 
        f.write(interpreter_code)

    # Template Main (Entry point)
    main_code = f'''import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run(text):
    lexer = Lexer(text)
    parser = Parser(lexer.get_tokens())
    interpreter = Interpreter()
    return interpreter.run(parser.parse())

if __name__ == "__main__":
    print("Selamat datang di {name}!")
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            run(f.read())
    else:
        while True:
            try:
                text = input("{name} > ")
                if text.strip().lower() in ["exit", "keluar"]: 
                    break
                if text.strip():
                    run(text)
            except EOFError:
                break
'''
    with open(f"{name}/main.py", "w") as f: 
        f.write(main_code)
        
    print(f"Berhasil! Direktori '{name}' telah dibuat dengan file-file dasar.")
    print("Masuk ke direktori tersebut dan edit file-filenya untuk mengembangkan bahasa baru Anda.")

def ai_chat(prompt, session="oiNkyZ6"):
    print(f"Mengirim permintaan ke AI Coder (Session: {session})...")
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://api.synoxcloud.xyz/ai-chat/ai-coder?prompt={encoded_prompt}&session={session}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (RiskiSDK)'})
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            try:
                json_data = json.loads(data)
                # Bergantung pada format respons API:
                if "result" in json_data:
                    print("\n[Riski AI]:\n", json_data["result"])
                elif "message" in json_data:
                    print("\n[Riski AI]:\n", json_data["message"])
                elif "response" in json_data:
                    print("\n[Riski AI]:\n", json_data["response"])
                else:
                    print("\n[Riski AI]:\n", json.dumps(json_data, indent=2))
            except json.JSONDecodeError:
                print("\n[Riski AI]:\n", data)
    except urllib.error.HTTPError as e:
        print(f"Error dari API: {e.code} - {e.reason}")
        error_msg = e.read().decode('utf-8')
        try:
            print("Detail Error:", json.dumps(json.loads(error_msg), indent=2))
        except:
            print("Detail Error:", error_msg)
    except Exception as e:
        print(f"Terjadi kesalahan saat menghubungi AI: {e}")

def main():
    parser = argparse.ArgumentParser(description="Riski SDK - Tool canggih untuk membuat bahasa pemrograman baru & AI Coder Assistant")
    subparsers = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

    # Sub-command: create-lang
    parser_create = subparsers.add_parser("create-lang", help="Buat struktur dasar (boilerplate) untuk bahasa pemrograman baru")
    parser_create.add_argument("name", help="Nama bahasa pemrograman baru yang ingin dibuat")

    # Sub-command: ai
    parser_ai = subparsers.add_parser("ai", help="Minta bantuan dari sistem AI Coder API")
    parser_ai.add_argument("prompt", help="Pertanyaan, instruksi, atau prompt untuk AI")
    parser_ai.add_argument("--session", default="oiNkyZ6", help="ID Session untuk AI API (opsional)")

    args = parser.parse_args()

    if args.command == "create-lang":
        create_lang(args.name)
    elif args.command == "ai":
        ai_chat(args.prompt, args.session)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
