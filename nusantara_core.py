import urllib.request
import urllib.parse
import json

# Warna Merah Putih
RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'

class Interpreter:
    def __init__(self):
        self.memory = {}

    def evaluate(self, node):
        if node[0] == 'STRING':
            return node[1]
        elif node[0] == 'NUMBER':
            return node[1]
        elif node[0] == 'VAR':
            var_name = node[1]
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise RuntimeError(f"Variabel tidak ditemukan: {var_name}")
        elif node[0] == 'ASSIGN':
            var_name = node[1]
            value = self.evaluate(node[2])
            self.memory[var_name] = value
            return value
        elif node[0] == 'CALL':
            func_name = node[1]
            arg = self.evaluate(node[2])
            return self.call_function(func_name, arg)
        else:
            raise RuntimeError(f"Node tidak dikenal: {node}")

    def call_function(self, func_name, arg):
        if func_name == 'tulis_merah':
            print(f"{RED}{arg}{RESET}")
            return None
        elif func_name == 'tulis_putih':
            print(f"{WHITE}{arg}{RESET}")
            return None
        elif func_name == 'tanya_claude':
            return self.fetch_claude(arg)
        elif func_name == 'tanya_gemini':
            return self.fetch_gemini(arg)
        else:
            raise RuntimeError(f"Fungsi tidak tersedia di Nusantara SDK: {func_name}")

    def fetch_claude(self, prompt):
        print(f"{WHITE}Memproses pertanyaan ke Claude AI...{RESET}")
        encoded_prompt = urllib.parse.quote(str(prompt))
        url = f"https://api-nanzz.my.id/docs/api/ai/chatday.php?prompt={encoded_prompt}&model=anthropic/claude-sonnet-4.6"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                reply = data.get('result', {}).get('response', 'Respons tidak ditemukan.')
                print(f"{RED}[Nusantara SDK - Claude]{RESET}\n{WHITE}{reply}{RESET}\n")
                return reply
        except Exception as e:
            err = f"Gagal menghubungi Claude: {e}"
            print(f"{RED}{err}{RESET}")
            return err

    def fetch_gemini(self, prompt):
        print(f"{WHITE}Memproses pertanyaan ke Gemini AI...{RESET}")
        encoded_prompt = urllib.parse.quote(str(prompt))
        url = f"https://api.synoxcloud.xyz/ai-chat/gemini-3.1-pro?pesan={encoded_prompt}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                reply = data.get('result', {}).get('reply', 'Respons tidak ditemukan.')
                print(f"{RED}[Nusantara SDK - Gemini]{RESET}\n{WHITE}{reply}{RESET}\n")
                return reply
        except Exception as e:
            err = f"Gagal menghubungi Gemini: {e}"
            print(f"{RED}{err}{RESET}")
            return err

    def run(self, ast):
        result = None
        for statement in ast:
            result = self.evaluate(statement)
        return result
