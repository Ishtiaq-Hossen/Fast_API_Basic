# 🚀 FastAPI Quick Start Guide

## 📘 What is FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

### ⭐ Key Features:

- ⚡ **Fast**: Very high performance, on par with NodeJS and Go (thanks to ASGI).
- 🧼 **Easy to Use**: Clean, concise, and intuitive syntax.
- 📚 **Auto Docs**: Automatically generates OpenAPI (Swagger) documentation.
- 🛡️ **Validation**: Powerful request validation using **Pydantic**.
- 🔄 **Asynchronous**: Native async and await support for non-blocking code.

---

## 🛠️ Installation

### 🔰 Basic Installation (For Testing)

1. **Create a project folder** (e.g., `Fast_API`)
2. **Open your terminal in the folder and run the following commands:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi uvicorn
```

3. **Create a file named main.py and add the following code:**
```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}
```

4. **Run the application:**
```bash
uvicorn main:app --reload
```
# ⚙️ Advanced Project Structure
**Organize your project like this:**

```css
FAST_API/
├── app/
│   └── main.py
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── lib64/
│   └── pyvenv.cfg
└── requirements.txt
```

Make sure to activate the virtual environment and install dependencies as shown in the basic setup.

1. **🏃 Running the App (Advanced)**
```bash
uvicorn app.main:app --reload
```

2. **🌐 Custom Host and Port**
To run the server on a specific IP and port:

```bash
uvicorn app.main:app --host 172.168.9.132 --port 8080 --reload
```

# **🧾 Terminal Command Summary**

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn
python3
from fastapi import FastAPI
exit()
uvicorn app.main:app --reload
```


