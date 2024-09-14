# Anthropic Terminal Utility

This Python script provides an interactive terminal utility that integrates with the Anthropic AI API. It allows users to chat with the Claude AI model and execute terminal commands through the AI assistant.

## Prerequisites

- Python 3.x
- `anthropic` library (install via `pip install anthropic`)
- Anthropic API key

## Usage

1. Install the required dependencies:
   ```
   pip install anthropic
   ```

2. Run the script with your Anthropic API key:
   ```
   python terminal_claude.py --api_key YOUR_API_KEY
   ```

3. The script will start an interactive chat session with the Claude AI assistant. You can type your messages and press Enter to send them.

4. Claude will respond to your messages and can suggest terminal commands to execute. It will use the special token `
Command executed: ` followed by the command to indicate that a command should be executed.
Output: Error: /bin/sh: -c: line 1: unexpected EOF while looking for matching ``'



5. The script will execute the suggested commands and display the output within the chat session.

6. To exit the program, type 'exit' and press Enter.

## Example

```
Welcome to the Anthropic Terminal Utility. Type 'exit' to quit.
You: Hi, can you help me list the files in the current directory?
Claude: Sure! To list the files in the current directory, you can use the 'ls' command. Here's how:


Command executed: ls
Output: README.md
terminal_claude.py



This will display a simple list of files and directories in the current directory.
You: exit
```
