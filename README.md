# MongoDB EDA Case Study

A complete MongoDB case study covering installation, CRUD operations, MongoDB Shell (mongosh), MongoDB Compass, PyMongo, aggregation pipelines, and Exploratory Data Analysis (EDA) using Python.

This repository is designed as a hands-on learning resource for students to understand MongoDB from installation to data analysis through a real-world case study.

---

# Learning Objectives

After completing this project, you will be able to:

- Install MongoDB Community Edition
- Configure MongoDB Shell (mongosh)
- Use MongoDB Compass
- Connect MongoDB using PyMongo
- Perform CRUD operations
- Execute MongoDB queries
- Use Aggregation Pipelines
- Perform Exploratory Data Analysis (EDA) using Pandas
- Create data visualizations
- Generate business insights from MongoDB datasets

---

# Repository Structure

```
mongodb-eda-case-study/
│
├── data/                 # Dataset files
├── docs/                 # Documentation
├── notebooks/            # Jupyter Notebook
├── output/               # Generated outputs and graphs
├── screenshots/          # Screenshots used in documentation
│
├── requirements.txt
├── lib_versions.py
├── .gitignore
├── README.md
└── LICENSE
```

---

# Prerequisites

The following software should be installed on your system.

- Python 3.11 or later
- Git
- Visual Studio Code (Recommended)
- MongoDB Community Edition
- MongoDB Compass
- MongoDB Shell (mongosh) 
- Pymongo

---

# Clone the Repository

```bash
git clone https://github.com/<your-username>/mongodb-eda-case-study.git

cd mongodb-eda-case-study
```

---

# Create Virtual Environment

```bash
python -m venv mongodb
```

---

# Activate Virtual Environment

### Windows PowerShell

```powershell
.\mongodb\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
mongodb\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Update `.gitignore`

To prevent the virtual environment from being tracked by Git, add the following entry to the `.gitignore` file.

```gitignore
mongodb/*
```

This ensures that all files inside the virtual environment are ignored and are not committed to the Git repository.

---

# Verify Installation

Run the following command to verify that all required Python packages are installed correctly.

```bash
python lib_versions.py
```

The `lib_versions.py` script checks whether all the required Python packages for this project are installed and displays their installed version numbers. This helps verify that your Python environment is configured correctly before proceeding with the case study.

---

# Deactivate Virtual Environment

```bash
deactivate
```

---

# MongoDB Installation

This project uses the following MongoDB components:

- **[MongoDB Community Edition](https://www.mongodb.com/products/self-managed/community-edition)** – The database server that stores and manages data.
- **[MongoDB Shell (mongosh)](https://www.mongodb.com/try/download/shell)** – A command-line interface for interacting with MongoDB.
- **[MongoDB Compass](https://www.mongodb.com/products/tools/compass)** – A graphical user interface (GUI) for browsing and managing MongoDB databases.
- **PyMongo** – The official Python driver for connecting Python applications to MongoDB.

> **Note:** Installation steps are not covered in this repository. Please ensure that MongoDB Community Edition and MongoDB Shell (mongosh) are installed before proceeding.

---

# Verify MongoDB Installation

Verify the MongoDB Server installation:

```bash
mongod --version
```

Verify the MongoDB Shell installation:

```bash
mongosh --version
```

If both commands display version information, MongoDB has been installed successfully.

---

# Verify PyMongo Connection

Run the following command to verify that Python can connect to the MongoDB server:

```bash
python notebooks\connect.py
```

If the connection is successful, a confirmation message will be displayed indicating that PyMongo is connected to the MongoDB server successfully.

---


# Current Progress

- [x] GitHub Repository Created
- [x] Project Structure Created
- [x] Virtual Environment Created
- [x] Python Dependencies Installed
- [x] MongoDB Community Edition Installation
- [x] MongoDB Shell (mongosh)
- [x] MongoDB Compass
- [x] pymongo
- [ ] Dataset Import
- [ ] CRUD Operations
- [ ] Query Operators
- [ ] Aggregation Pipeline
- [ ] PyMongo Integration
- [ ] Exploratory Data Analysis
- [ ] Business Insights

---

# License

This project is licensed under the MIT License.

---

# Author

**Bahadursha A V L Sainadh**

Assistant Professor

Department of Computer Science and Engineering (Artificial Intelligence)

Vignan's Institute of Information Technology (VIIT)