# Text to Math Problem Solver

This project is a **Streamlit-based AI-powered math problem solver** that uses **Hugging Face's Gemma-2-2b-it model** to process natural language math problems and generate step-by-step solutions. It also includes reasoning capabilities and Wikipedia search integration for enhanced assistance.

## Features

- **Natural Language to Math Problem Solving**: Converts user-inputted math problems into structured solutions.
- **Step-by-Step Explanations**: Provides detailed solutions for better understanding.
- **Reasoning Tool**: Handles logical and reasoning-based queries.
- Wikipedia Integration: Retrieves relevant information from Wikipedia.
- **Interactive Chat**: Allows a continuous conversation with session-based chat history.

## Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Hugging Face Transformers**
- **Wikipedia API**

## Installation

### Prerequisites

- Python 3.10
- Hugging Face API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com//PrinceGupta8//text-to-math-solver.git
   cd text-to-math-solver
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your Hugging Face API Key** in the sidebar.
2. **Input a math problem** in natural language.
3. **Click 'Find my answer'** to get a step-by-step solution.

## Example

**Input:**

```
I have 7 bananas and 5 apples. I eat 2 bananas and 1 apple. How many fruits are remaining?
```

**Output:**

```
You had 7 bananas and 5 apples.
You ate 2 bananas, so remaining bananas = 7 - 2 = 5.
You ate 1 apple, so remaining apples = 5 - 1 = 4.
Total remaining fruits = 5 + 4 = 9.
```

## API Keys

- Get your **Hugging Face API Key** from [Hugging Face](https://huggingface.co/settings/tokens).
- Enter it in the Streamlit sidebar.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

**Enjoy solving math problems effortlessly with AI!**

