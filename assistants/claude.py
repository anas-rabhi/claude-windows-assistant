import boto3
import json
import os
from typing import List, Dict
import boto3, json, math
from colorama import init, Fore, Style
TOOL_COLOR = Fore.YELLOW


class Claude:
    def __init__(self, system_message: str, prefix_message="", max_tokens=2000):
        
        session = boto3.Session()
        self.bedrock = session.client(service_name='bedrock-runtime')
        self.history = []
        self.tools_list = []
        self.prefix_message = prefix_message
        self.system_message = system_message
        self.max_tokens = max_tokens

    def add_tool(self, name: str, 
                 description: str, 
                 properties: Dict[str, str]):

        tool = {
        "toolSpec": {
            "name": name,
            "description": description,
            "inputSchema": {
                "json": properties
                }
            }
        }
            
        self.tools_list.append(tool)
        # print("Added tool, name: {0}".format(name))

    def user_message(self, message):
        message = {
                        "role": "user",
                        "content": [
                            { "text": self.prefix_message + message} 
                        ]}

        self.history.append(message)

    def chat(self, message, history=None):

        if history:
            self.history = history
        
        if len(message)>0:
            self.user_message(message)
        
        if len(self.tools_list)>0:
            response = self.bedrock.converse(
                modelId="anthropic.claude-3-sonnet-20240229-v1:0",
                messages=self.history,
                inferenceConfig={
                    "maxTokens": self.max_tokens,
                    "temperature": 0,
                    "stopSequences": ["\nObservation"]
                },
                toolConfig={
                    "tools": self.tools_list
                },
                system=[{"text": self.system_message}]
            )
            self.history.append(response['output']['message'])
        else:
            response = self.bedrock.converse(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            messages=self.history,
            inferenceConfig={
                "maxTokens": self.max_tokens,
                "temperature": 0
            },
            system=[{"text": self.system_message}]
            )
            self.history.append(response['output']['message'])

        return self.parsed_answer(response)
    
    def parsed_answer(self, response):
        
        text = ""
        resp = response['output']['message']['content']
        
        parsed = {"tool_use": False, "tool_response": "", "text": ""}

        for idx in resp:
            if "toolUse" in idx:
                parsed = {"tool_use": True, "tool_response": idx["toolUse"], "text": ""}
            elif "text" in idx:
                text = idx['text']
        
        parsed['text'] = text

        print(TOOL_COLOR + f"Using Tool : {parsed['tool_use']}"   + Style.RESET_ALL)

        return parsed

    def add_tool_response(self, response: str, tool_use_id: str):

        tool_result = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [
                {
                    "json": {
                        "result": response
                    }
                }
            ]
        }
        }
        

        self.history.append({
        "role": "user",
        "content": [tool_result],
        }) 
        return self.chat('')

    def __call__(self, message, history=None):
        return self.chat(message, history)
    