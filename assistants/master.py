from assistants.claude import Claude
from assistants.config import master_sys_prompt

class Master(Claude):
    def __init__(self):
        system_message = master_sys_prompt
        super(Master, self).__init__(system_message)
        self.add_tool(
            name="create_function",
            description="""Create python code to access files, retrieve content from files or navigate windows computer using libraries like PyAutoGUI, PyWin32, os or other python libraries. You have to choose the most efficient ones.
                           """,
            properties={
                    "type": "object",
                    "properties": {
                        "python_code": {
                            "type": "string",
                            "description": "The code to execute to accomplish the task."
                        }
                    },
                    "required": ["python_code"]
                }
        )
        self.add_tool(
            name="analyzer",
            description="Summarize or analyze text.",
            properties={
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "Text to be analyzed or summarized"
                        },
                    "order": {
                            "type": "string",
                            "description": "The task or order to give to the summarizer"
                        }
                    },
                    "required": ["text", "order"]
                }
        )
