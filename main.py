
import os
from datetime import datetime
import json
from colorama import init, Fore, Style
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
import pygments.util
import base64
from PIL import Image
import io
import re
import difflib


from assistants.master import Master
from assistants.worker import CSAgent
import io
from contextlib import redirect_stdout

def extract_code(text):
    if "```python" in text:
        text = text.replace("```python", "").replace("```", "")
    return text


def exec_python(code):
    f = io.StringIO()
    try: 
        try :
            with redirect_stdout(f):
                exec(extract_code(code))
            out = f.getvalue()
            out = f"PYTHON CODE : {code} \n" + "RESULT : " + out
        except Exception as e:
            with redirect_stdout(f):
                print(e)
            out = "ERROR : " + f.getvalue()
        out
    except Exception as e:
        print(e)
        out = f"PYTHON CODE : {code} \n" 

    return out
    
master = Master()
worker = CSAgent()


USER_COLOR = Fore.RED
CLAUDE_COLOR = Fore.BLUE
TOOL_COLOR = Fore.YELLOW
RESULT_COLOR = Fore.GREEN

print(Fore.GREEN + "Welcome to Claude Assistant, how can I serve you sir ?" + Style.RESET_ALL)
def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

MAX_CONTINUATION_ITERATIONS = 25

def main():
    
    while True:
        user_input = input(f"\n{USER_COLOR}" + f"You: {Style.RESET_ALL}")
        
        if user_input.lower() == 'exit':
            print_colored("Thank you for chatting. Goodbye!", CLAUDE_COLOR)
            break

        elif user_input == "":
            print_colored(f"Please write something", RESULT_COLOR)
        
        else:
            answer = master(user_input)

            print_colored(f"Master response : {answer['text'].split('<step')[-1]}", CLAUDE_COLOR)

            for _ in range(10):

                if _==9:
                    print("This is my last step : ", _+1)
                else :
                    print("STEP : ", _+1)
                    
                if answer['tool_use'] == True:

                    if answer['tool_response']['name'] == "create_function":
                        print_colored("Using  create_function ", CLAUDE_COLOR)

                        out = exec_python(answer['tool_response']['input']['python_code'])
                        
                    elif answer['tool_response']['name'] == "analyzer":
                        print_colored("Using  analyzer ", CLAUDE_COLOR)

                        out = worker(f"{answer['tool_response']['order']} the following text, be cocise : {answer['tool_response']['text']} ")['text']

                        print_colored(f"Analyser response {out}", CLAUDE_COLOR)
                    
                    answer = master.add_tool_response(response=out, tool_use_id=answer['tool_response']['toolUseId'])
                    print_colored(f"Master response : {answer['text'].split('<step')[-1]}", CLAUDE_COLOR)

                else:
                    
                    print_colored(f"Everything is done", RESULT_COLOR)
                    break

        

if __name__ == "__main__":
    main()