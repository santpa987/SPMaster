# AI Agents with PhiData and Groq

This project demonstrates how to create and deploy local AI agents using PhiData and Groq in Python. The project features three task-specific AI agents:

- **Financial Agent**: Analyzes financial data, retrieves stock prices, and provides insights.
- **Web Search Agent**: Searches the web for information and includes credible sources.
- **Weekend Planner Agent**: Plans personalized weekend itineraries based on user preferences.

## Features

- **Local Deployment**: Run AI agents entirely on your local machine.
- **Task-Specific Agents**: Each agent is tailored for a specific use case.
- **Extensibility**: Easily add or modify agents.
- **Secure API Integration**: Uses environment variables to store API keys securely.

## Prerequisites

- Python 3.8 or above
- A valid `PHI_API_KEY`
- Basic knowledge of Python

## Folder Structure

```
project-root/
│
├── playground.py           # Main Python file for running the application
├── requirements.txt # List of Python dependencies
├── .env             # API keys (not shared publicly)
├── README.md        # Documentation (this file)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/santpa987/SPMaster.git
   cd projects/cookbook/AIAgent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```env
   PHI_API_KEY=your_phi_api_key
   GROQ_API_KEY=your_groq_api_key
   ```
   Replace key with your actual API key.

## Usage

1. Run the application:
   ```bash
   python playground.py
   ```

2. Open the local server in your browser:
   ```
   http://localhost:7777
   ```

3. Interact with the agents in phidata.com by providing the localhost url in it:
   - **Web Search Agent**: Search for information on the web.
   - **Financial Agent**: Analyze stock prices, company fundamentals, and more.
   - **Weekend Planner Agent**: Plan your weekend with personalized suggestions.

## Agents Overview

### Web Search Agent
- **Role**: Searches the web for user queries.
- **Key Features**:
  - Uses DuckDuckGo for web searches.
  - Always includes credible sources.

### Financial Agent
- **Role**: Provides financial insights and recommendations.
- **Key Features**:
  - Fetches stock prices and company fundamentals.
  - Displays results in a bullet-point format.

### Weekend Planner Agent
- **Role**: Helps users plan their weekends.
- **Key Features**:
  - Suggests events, activities, and dining options.
  - Structures recommendations in sections for clarity.

## Technologies Used

- **PhiData**: Framework for creating AI agents.
- **Groq**: Language model powering the agents.
- **Tools**:
  - `DuckDuckGo`: Web search functionality.
  - `YFinanceTools`: Financial data analysis.
  - `ExaTools`: Weekend planning support.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request for any improvements or additional features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or issues, please reach out at santoshpandey987@gmail.com
