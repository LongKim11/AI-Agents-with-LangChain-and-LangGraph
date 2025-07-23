# 🚀 LangChain- Develop AI Agents with LangChain & LangGraph

Udemy course..

## 🎯 Project Overview

This project contains two main applications:

### 🧊 Ice Breaker App

A Flask web application that generates personalized ice breakers by analyzing LinkedIn profiles and Twitter data using LangChain agents and AI.

### ⚛️ React LangChain

A Python application demonstrating LangChain agents with custom tools and ReAct pattern implementation.

## 🛠️ Prerequisites

- **Python 3.13+** (required by project configuration)
- **Git** for cloning the repository
- **OpenAI API Key** for AI functionality
- **Tavily API Key** for web search capabilities

## 📦 Installation

### Method 1: Using pip (Recommended)

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install project dependencies
pip install -e .
```

### Method 2: Using uv (Fast Python Package Manager)

```bash
# Install uv if not already installed
pip install uv

# Create virtual environment and install dependencies
uv sync
```

## 🔧 Setup

### 1. Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=

SCRAPIN_API_KEY=

TAVILY_API_KEY=

LANGCHAIN_API_KEY=
LANgCHAIN_TRACING_V2=
LANGCHAIN_PROJECT=
```
