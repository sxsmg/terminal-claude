import os
import subprocess
import anthropic
import argparse

SYSTEM_PROMPT = """You are an AI assistant integrated with a terminal utility on the user's local machine. You can execute commands by using the special token '{{EXECUTE}}' followed by the command. For example: '{{EXECUTE}}ls -la'. Always explain what a command does before suggesting it. Be cautious with system-modifying commands and ask for confirmation. Prioritize the security and integrity of the user's system. If you're unsure about a command's effects, express your uncertainty. For complex tasks, break them down into steps. Remember, you don't have persistent memory of the system state between messages."""

class AnthropicTerminalUtil:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.conversation_history = []

    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def chat_with_claude(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text
        processed_message = self.process_claude_response(assistant_message)
        self.conversation_history.append({"role": "assistant", "content": processed_message})
        
        return processed_message

    def process_claude_response(self, response):
        parts = response.split('{{EXECUTE}}')
        result = [parts[0]]
        
        for part in parts[1:]:
            command_end = part.find('\n')
            if command_end == -1:
                command_end = len(part)
            
            command = part[:command_end].strip()
            output = self.execute_command(command)
            
            result.append(f"Command executed: {command}")
            result.append(f"Output: {output}")
            result.append(part[command_end:])
        
        return '\n'.join(result)

def main():
    parser = argparse.ArgumentParser(description="Anthropic Terminal Utility")
    parser.add_argument("--api_key", required=True, help="Anthropic API Key")
    args = parser.parse_args()

    util = AnthropicTerminalUtil(args.api_key)

    print("Welcome to the Anthropic Terminal Utility. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        claude_response = util.chat_with_claude(user_input)
        print(f"Claude: {claude_response}")

if __name__ == "__main__":
    main()