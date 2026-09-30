# 🚀 JD Analyzer Agent

An asynchronous, production-ready AI agent built with **FastAPI** and **Google Gemini 3.5 Flash**. This service analyzes job descriptions (JDs) to extract the primary tech stack, identify top skills, and dynamically generate highly relevant technical interview questions. 

Designed for scalability and seamless deployment, the agent enforces structured JSON outputs using **Pydantic v2** and is containerized via **Docker** with an automated **CI/CD pipeline** to Render.

---

## ✨ Features

- **Asynchronous AI Processing:** Utilizes the latest Google GenAI SDK (`genai.Client().aio`) for non-blocking, high-performance LLM calls.
- **Strict Data Validation:** Guarantees deterministic, structured JSON responses using Pydantic schemas, eliminating parsing errors.
- **Production-Ready Server:** Built on FastAPI with built-in Swagger UI documentation and health check endpoints.
- **Isolated Environment:** Managed by `uv`, ensuring lightning-fast dependency resolution and isolated builds without bloated virtual environments in production.
- **Automated CI/CD:** Integrated with GitHub Actions to run `pytest` suites and automatically trigger Docker deployments on Render.

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **AI/LLM:** Google Gemini API
- **Validation:** Pydantic v2
- **Package Manager:** `uv` (Astral)
- **Containerization:** Docker
- **Testing:** `pytest` & `httpx`
- **Deployment:** Render (PaaS) & GitHub Actions

---

## 🚀 Local Development

### Prerequisites
- [Docker Desktop](https://www.docker.com/) (or Docker Engine)
- A [Google AI Studio API Key](https://aistudio.google.com/app/apikey)

### 1. Clone the Repository
```bash
git clone https://github.com/sambar226/jd-agent.git
cd jd-agent
