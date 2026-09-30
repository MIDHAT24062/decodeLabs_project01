# Rule-Based Chatbot ( project 01 )

A simple command-line chatbot built for DecodeLabs AI Project 1. It answers from a dictionary of predefined responses, no ML involved.

## Run

```
python rule_based_chatbot.py
```

Needs Python 3 only.

## What it does

- Runs in a loop until you type `bye`, `exit`, `quit`, `goodbye` or `q`
- Ignores case, extra spaces and punctuation
- Replies to greetings, a few questions, `time` and `date`
- Type `help` to see examples
- Unknown input gets a default reply

## Add a reply

Add a lowercase key to `RESPONSES` in the script:

```python
RESPONSES["what is python"] = "A programming language."
```

Matching is exact, so `hello there` won't match `hello`.
