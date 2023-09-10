# 🛡️ Cyber LLM Project 🤖

🎉 **Welcome to the Cyber LLM Project!** Let's automate the cybersecurity threat hunting with state-of-the-art machine learning models and techniques. Detect Indicators of Compromise (IoCs) and identify APT groups effortlessly! 🎉

## 🎯 Objective

Our mission is complex but solvable! We're diving into raw security logs to identify any Indicators of Compromise (IoCs) with high confidence. Using Prompt Engineering, we'll send log embeddings to Llama 2 for analysis. High-confidence findings are stored in LangChain Memory, and when ready, we'll release a detailed report on the detected IoCs and the implicated APT group.

## 🛠️ Technologies & Concepts

- **LLama 2**: Our trained Language Model for MITRE ATT&CK tactics and APT groups.
- **Chroma**: For vector storage.
- **LangChain Memory**: To hold intermediate results and confidence levels.
- **RAG (Retrieval Augmented Generation)**: For enhanced context retrieval.
- **Vector Store**: To store embeddings for easy retrieval.
- **Embeddings**: Transformed representation of raw logs.
- **Prompt Engineering**: Techniques for accurate Language Model analysis.
- **FAISS**: Efficient similarity search and clustering of dense vectors.

### 🌐 Graphical Representation of Technologies

         +-------------+    +-------------------+
         |  Raw Logs   |--->|     FAISS Index    |
         +-------------+    +-------------------+
                 |                /        \
                 |               /          \
                 |              /            \
       +---------------+    +----------+  +---------------+
       | Text Chunks   |--->| Embedding |->|  Vector Store |
       +---------------+    +----------+  +---------------+
                 |                                |
                 |                                |
                 |                                |
         +---------------+                +---------------+
         |   Llama 2     |<---------------|    Chroma     |
         +---------------+                +---------------+
                 |                                |
                 |                                |
         +---------------+                +---------------+
         | LangChain Mem |<---------------|  RAG Context  |
         +---------------+                +---------------+


---
---

## 🏗️ Software Architecture 🏗️
---
### 🔹 Phase 1: Initialization & Configuration 🛠️

#### Why:
Initialize all required components to make them ready for the main analysis loop.

#### How:
- **Initialize FAISS index**: For efficient similarity search in high dimensions.
- **Initialize Chroma Vector Store, LangChain Memory, and Llama 2**: These will hold our embeddings, intermediate results, and handle our analysis respectively.
---
### 🔹 Phase 2: Data Loading & Preprocessing 📤

#### Why:
To load raw logs and prepare the data for feature engineering.

#### How:
- **Read the raw logs into a DataFrame**: Use Pandas for this.
- **Preprocess Data**: Clean and possibly normalize the logs for easier handling.
---
### 🔹 Phase 3: Feature Engineering 🔍

#### Why:
To transform raw data into a format that's easier to analyze.

#### How:
- **Convert Logs to Embeddings**: Use Prompt Engineering to generate dense vectors.
- **Store in Chroma**: For fast retrieval and analysis.
---
### 🔹 Phase 4: Contextual Retrieval with RAG 🗂️

#### Why:
To enrich the dataset and make it more suitable for accurate prediction.

#### How:
- **Use RAG to fetch additional context**: The context will help Llama 2 in understanding and classifying the log vectors.
---
### 🔹 Phase 5: Analysis & Memory Storage 🧠

#### Why:
To analyze each log vector for potential IoCs and APT groups.

#### How:
- **Send vectors to Llama 2**: And get the analysis results.
- **Store intermediate results**: Store these in LangChain Memory with their confidence levels.
---
### 🔹 Phase 6: Evaluation & Output 📊

#### Why:
To finally decide whether an IoC and an APT group have been detected.

#### How:
- **Check the confidence level**: If it's above a certain threshold, release the data.
- **Notify the user**: Provide the list of detected IoCs and APT groups.
---
### 🔹 Phase 7: Resource Cleanup 🧹

#### Why:
To release any resources and close open connections.

#### How:
- **Close any network connections**: Free up resources.

---

