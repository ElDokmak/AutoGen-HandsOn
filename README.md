#  **AutoGen**
<img src="https://microsoft.github.io/autogen/assets/images/autogen_agentchat-250ca64b77b87e70d34766a080bf6ba8.png">
AutoGen offers a unified multi-agent conversation framework as a high-level abstraction of using foundation models. It features capable, customizable and conversable agents which integrate LLM, tool and human via automated agent chat. By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code.

This framework simplifies the orchestration, automation and optimization of a complex LLM workflow. It maximizes the performance of LLM models and overcome their weaknesses. It enables building next-gen LLM applications based on multi-agent conversations with minimal effort.

## Agents 
AutoGen abstracts and implements conversable agents designed to solve tasks through inter-agent conversations. Specifically, the agents in AutoGen have the following notable features:

* Conversable: Agents in AutoGen are conversable, which means that any agent can send and receive messages from other agents to initiate or continue a conversation
* Customizable: Agents in AutoGen can be customized to integrate LLMs, humans, tools, or a combination of them.

The figure below shows the built-in agents in AutoGen.
<img src="https://microsoft.github.io/autogen/assets/images/autogen_agents-b80434bcb15d46da0c6cbeed28115f38.png">

* The AssistantAgent is designed to act as an AI assistant, using LLMs by default but not requiring human input or code execution. It could write Python code (in a Python coding block) for a user to execute when a message (typically a description of a task that needs to be solved) is received. Under the hood, the Python code is written by LLM (e.g., GPT-4). It can also receive the execution results and suggest corrections or bug fixes. Its behavior can be altered by passing a new system message. The LLM inference configuration can be configured via llm_config.

* The UserProxyAgent is conceptually a proxy agent for humans, soliciting human input as the agent's reply at each interaction turn by default and also having the capability to execute code and call functions. The UserProxyAgent triggers code execution automatically when it detects an executable code block in the received message and no human user input is provided. Code execution can be disabled by setting the code_execution_config parameter to False. LLM-based response is disabled by default. It can be enabled by setting llm_config to a dict corresponding to the inference configuration. When llm_config is set as a dictionary, UserProxyAgent can generate replies using an LLM when code execution is not performed.

> NOTE: **human_input_mode**:
>> 1. **ALWAYS:** the agents prompt for human input every time a message is recieved, the conversation stops when the human input is exit or when is_termination_msg is True and there is no human input.
>> 2. **TERMINATE:** the agent only prompts for human input only whet a termination message is recieved or the number of auto reply reaches the max_consecutive_auto_reply.
>> 3. **NEVER:** the agent will never prompt for human input, the conversation stops when the number of auto reply reaches the max_consecutive_auto_reply or when is_temination_msg is True.

> [Source](https://microsoft.github.io/autogen/docs/Getting-Started)
