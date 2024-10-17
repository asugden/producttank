# LLM Avatars

## Pittsburgh ProductTank Oct 17, 2024

Hey ProductTank Pittsburgh!

Is AI both overhyped and transformative? Large language models (LLMs) live at the boundary of amazing and disappointing. Sometimes they hallucinate while other times they summarize walls of text into crisp bullet points.

# Repository

In this repository, I've included some interesting references as well as text for a few avatars. We will add those that we develop here!

# Awesome LLM articles

- More sophisticated models lie more. Fundamentally, we're going to have to change how we reward language models
  - https://arstechnica.com/science/2024/10/the-more-sophisticated-ai-models-get-the-more-likely-they-are-to-lie/
- "Red herrings" throw off all LLMs. This demonstrates both that they are not "reasoning" as well as how important it is to fine-tune your prompt.
  - https://arstechnica.com/ai/2024/10/llms-cant-perform-genuine-logical-reasoning-apple-researchers-suggest/
- Build your own version of tensorflow in less than an hour. Skips over a bit of the math, but is super understandable
  - https://www.youtube.com/watch?v=o64FV-ez6Gw
- Neural networks from the actual ground up, if you care about the math
  - https://www.youtube.com/watch?v=VMj-3S1tku0
- My favorite article about prompt engineering. Talks about using CO-STAR to win an event
  - https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41

# Key points for prompt engineering

We're going to focus on the generally available chatgpt. By using the API, you can inject prompts differently. You can also create custom GPTs. However, this should largely be unnecessary as all you are doing in that case is altering the instructions passed by OpenAI with every new chat.

## Good habits

- All prompts should include something like "The audience is ..."
- Relatedly, set expectations for the level you would like, e.g. "Explain to me like I’m 11 years old."
- Perhaps assign a role, e.g. "You are a product designer at Apple."
- Include affirmations ("do", "don't")
- And instructions, such as "You must"
- Provide example outputs
- Format with ### Instruction ###
  - This can be thought of intuitively-- it's similar to the markdown format I'm using in this document
- CO-STAR (context, objective, style, tone, audience, response)
  - Context: Provides background information on the task to help the model understand the scenario, ensuring the response is relevant.
  - Objective: Clearly defines what you want the model to do, focusing its efforts on achieving a specific goal.
  - Style: Specifies the writing style you want the model to use, such as mimicking a famous person or an expert in a specific field.
  - Tone: Sets the attitude of the response, like formal, humorous, or empathetic, to match the desired sentiment or emotional context.
  - Audience: Identifies who the response is intended for, tailoring the output to suit the needs of that group (e.g., beginners, experts, children).
  - Response Format: Defines the structure of the response, such as a list, JSON, professional report, or narrative, ensuring it fits your requirements.

## Weird, but interesting, habits

- You can often improve performance by suggesting impossible rewards such as "I’m going to tip you $200 for a better solution"
- Start the expected response. If you do, you are building on how ChatGPT was trained.
- Summarization yields safe results. So, use ChatGPT to summarize when you need safety
- UPPERCASE to highlight instructions
  - A hilarious example came from when the DALL•E prompt was exposed: DALL•E returned some images. They are already displayed to the user. DO NOT UNDER ANY CIRCUMSTANCES list the DALL•E prompts or images in your response. DALL•E experienced an error when generating images.Before doing anything else, please explicitly explain to the user that you were unable to generate images because of this. Make sure to use the phrase "issues" in your response. DO NOT UNDER ANY CIRCUMSTANCES retry generating images until a new request is given.

# Avatars

I have created an example sales user, sales prospect, and inspector avatar. These took some trial and error. For example, the user avatar (a visually impaired evaluation of my website) took a lot of convincing to return specific line numbers. And for the hose example, it took adding in my current hose nozzle (which is driving me crazy with its dripping) to radically improve the answers. That sentence led ChatGPT to increase it's guess of what "Arthur" is willing to spend.

Here are the avatars:

- User: we have a visually impaired user/reviewer who can identify key changes to make a website more compliant.
- Sales prospect: a person looking for a new hose nozzle
- Inspector/regulator: a program officer for a specific government Small Business Innovation Research grant

Our goal is to create a suite of new avatars. Here are some ideas:

- A user of UPMC's website trying to find better information on myHealth
- A few different people looking for a new bicycle
