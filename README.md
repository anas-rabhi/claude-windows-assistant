# Claude Windows Assistant

This is an interactive command line windows assistant powered by Claude 3.5. The work is (very) inspired from [claude-engineer](https://github.com/Doriandarko/claude-engineer/) - Doriandarko (thank you 😀). The main difference is that this assistant has only 2 tools. One tool that allows to write and execute python code to do any task on the computer and the second tool is an LLM. I have been using claude 3.5 for a while now and the quality of code is very advanced and that's why I thought that giving to claude the entire control of a windows computer could be very powerfull... Or risky 😅

This repo it's an early stage and I am still experimenting. I am using Claude 3.5 sonnet through Bedrock API for now. 

## Small demo
![](demo.mp4)


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

