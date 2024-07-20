# Claude Windows Assistant

This is an interactive command line Windows assistant powered by Claude 3.5. The work is heavily inspired by [claude-engineer (Doriandarko)](https://github.com/Doriandarko/claude-engineer/) (thank you 😀). The main difference is that this assistant has only two tools: one tool allows writing and executing Python code to perform any task on the computer, and the second tool is an LLM. I have been using Claude 3.5 for a while now, and the quality of its code is very advanced. That's why I thought that giving Claude full control of a Windows computer could be very powerful... or risky 😅

This repo is in an early stage, and I am still experimenting. I am using Claude 3.5 sonnet through the Bedrock API for now.

## Small demo

https://github.com/user-attachments/assets/abe5e599-f30f-45ee-9078-c2d463cfcc3c

## Quick start

Install a new python env : 
 
```sh
python -m venv ./venv
``` 

Activate it : 

```sh
.\.venv\Scripts\activate
``` 

Run `main.py` :

```sh
python main.py
``` 

