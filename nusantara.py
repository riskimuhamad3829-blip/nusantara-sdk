import sys
from nusantara_lexer import Lexer
from nusantara_parser import Parser
from nusantara_core import Interpreter

RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'

def execute_code(text, interpreter):
    try:
        lexer = Lexer(text)
        tokens = lexer.get_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        result = interpreter.run(ast)
        if result is not None and not text.startswith("tulis") and not text.startswith("tanya"):
            print(f"{WHITE}=> {result}{RESET}")
    except Exception as e:
        print(f"{RED}Galat Sistem: {e}{RESET}")

def main():
    print(f"{RED}============================================={RESET}")
    print(f"{WHITE}      Nusantara SDK by Anak Bangsa Indo      {RESET}")
    print(f"{RED}============================================={RESET}")
    print(f"{WHITE}Selamat datang! SDK ini berfokus pada AI.{RESET}")
    print(f"{WHITE}Perintah tersedia:{RESET}")
    print(f"  {RED}- tulis_merah(\"teks\"){RESET}")
    print(f"  {WHITE}- tulis_putih(\"teks\"){RESET}")
    print(f"  {RED}- tanya_claude(\"teks\"){RESET}")
    print(f"  {WHITE}- tanya_gemini(\"teks\"){RESET}")
    print(f"{WHITE}Ketik 'keluar' untuk menghentikan program.{RESET}\n")
    
    interpreter = Interpreter()
    
    while True:
        try:
            text = input(f"{RED}Nusantara{WHITE} > {RESET}")
        except EOFError:
            break
            
        if not text.strip():
            continue
            
        if text.strip().lower() == 'keluar':
            print(f"{RED}Maju Terus{WHITE} Bangsa Indonesia!{RESET}")
            break
            
        execute_code(text, interpreter)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
            interpreter = Interpreter()
            execute_code(code, interpreter)
    else:
        main()
