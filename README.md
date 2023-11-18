## Discord Bot Description
This bot integrates with OpenAI's GPT for generating responses to user queries. It maintains a conversation context within each channel, responds to specific commands, and handles long responses by splitting them into multiple messages. The bot also includes a reminder feature.

## Commands

### `!hello`
- **Description**: Replies with a simple "Hello" message.
- **Usage**: `!hello`

### `!ask [query]`
- **Description**: Sends a query to OpenAI's GPT and returns the response. If no query is provided, prompts the user to provide one.
- **Usage**: `!ask What is AI?`

### `!setcontext [number]`
- **Description**: Sets the number of messages to keep in context for each channel. If an invalid number is provided, prompts for a valid integer.
- **Usage**: `!setcontext 5`

### `!showcontext`
- **Description**: Displays the current context of the channel. If no context is set, prompts to set it first.
- **Usage**: `!showcontext`

### `!clearcontext`
- **Description**: Clears the stored context for the channel. If no context is set, prompts to set it first.
- **Usage**: `!clearcontext`

### `!usecontext [query]`
- **Description**: Uses the stored context along with the provided query to generate a response from OpenAI's GPT.
- **Usage**: `!usecontext Explain quantum computing`

### `!remindme [seconds]`
- **Description**: Sets a reminder for the specified number of seconds.
- **Usage**: `!remindme 10`

## Additional Features

- **Context Management**: Stores a specified number of recent messages per channel to maintain context.
- **Message Chunking**: Splits long responses into multiple messages to comply with Discord's message length limit.
- **Ignored Commands**: Commands like `!showcontext`, `!clearcontext`, `!usecontext`, and `!setcontext` are ignored when storing messages for context.
- **Reminder Feature**: Allows setting simple reminders that notify the user after a specified time.

This bot enhances Discord interactions with AI-driven responses and useful utilities, making it a versatile tool for information retrieval, conversation, and reminders.
