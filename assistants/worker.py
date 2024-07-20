from assistants.claude import Claude
from assistants.config import worker_sys_prompt

class CSAgent(Claude):
    def __init__(self):
        system_message = worker_sys_prompt
        super(CSAgent, self).__init__(system_message, 
                                      prefix_message="Task description : ", 
                                      max_tokens=4000)
