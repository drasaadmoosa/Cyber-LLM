# Cyber LLM Project 🛡️🔍🤖

Welcome to the Cyber LLM Project! Here we're all about securing the digital world one vector at a time. Using a range of spiffy technologies like FAISS, Chroma, LangChain Memory, and Llama2, we're putting the "smart" in "smart cybersecurity." 🌐🔐✨

---
# What is "Cyber LLM" 🤖

In this innovative playground, we're not just doing cybersecurity; we're doing it smartly and efficiently! 🌐🔐✨

## The Objective 🎯

Got a massive text file of raw computer logs? Wondering if sneaky attackers are compromising your system? We've got you covered! Our project leverages cutting-edge technologies to sift through around 100MB of your security logs to find the proverbial needle in the haystack. 📊🔍

Here's the rundown: We use _prompt engineering_ to transform your logs into embeddings, which are then stored in a Chroma Vector Store. Next, our trained Llama2 model, an expert in MITRE ATT&CK tactics and Advanced Persistent Threat (APT) groups, takes these embeddings and scrutinizes them for any Indicators of Compromise (IoC). If we find anything fishy 🐟, it's stored in a LangChain Memory until we're pretty darn sure there's a compromise and can pinpoint the APT group behind it. The grand finale? We give you a concise list of IoCs and the name of the naughty APT group. 🚨🕵️‍♂️

Jump in and explore the architecture below to understand the gears that make this machine run smoothly! 🛠️⚙️




---

## Software Architecture 🏗️

---

### Phase 1: Initialization & Configuration 🌟

#### Function: `initialize_components()`

🎯 **Objective**: Initialize all the gears and cogs to get this machine up and running.

1️⃣ **FAISS Index**: Super-fast similarity searches among vectors with L2 distance metric.  
2️⃣ **Chroma Vector Store**: Our personal vault for storing vectors converted from text chunks.  
3️⃣ **LangChain Memory**: The brain where we store IoCs, APT groups, and confidence levels.  
4️⃣ **Llama2 LLM**: Our prediction wizard that identifies potential IoCs and APT groups.

---

### Phase 2: Data Loading & Preprocessing 📦

#### Function: `load_and_preprocess(filename)`

🎯 **Objective**: Open the treasure chest and prepare the loot!

1️⃣ **Load Data**: Import text from a CSV into a Pandas DataFrame.  
2️⃣ **Split Text**: Break the DataFrame into manageable text chunks.

---

### Phase 3: Feature Engineering 🛠️

#### Function: `convert_and_store(chunks, index, vector_store)`

🎯 **Objective**: Time to forge our text chunks into shiny vectors.

1️⃣ **Convert to Vectors**: Transform those text chunks to vectors using FAISS.  
2️⃣ **Store in FAISS**: Place the new vectors in our FAISS index.  
3️⃣ **Store in Chroma**: Keep a copy in our Chroma Vector Store.

---

### Phase 4: Analysis & Memory Storage 🧠

#### Function: `analyze_and_store(vector_store, llm, memory)`

🎯 **Objective**: Analyze and categorize. This is where the magic happens!

1️⃣ **Iterate Vectors**: Go through each vector in our Chroma store.  
2️⃣ **Make Predictions**: Consult Llama2 to predict potential IoCs and APT groups.  
3️⃣ **Save the Day**: Store these critical findings in LangChain Memory.

---

### Phase 5: Evaluation & Output 📊

#### Function: `evaluate_and_output(memory, threshold=0.9)`

🎯 **Objective**: Judgment time! Do we have enough to sound the alarms? 🚨

1️⃣ **Confidence Check**: See if we've reached the confidence threshold.  
2️⃣ **Reveal Findings**: If yes, unveil the identified APT group and IoCs.

---

### Phase 6: Resource Cleanup 🧹 (Not Implemented Yet)

🎯 **Objective**: Time to close shop and ensure everything is spick and span!

---

And there you have it! A whirlwind tour of the Cyber LLM architecture! Feel free to dive into the code, raise issues, or contribute. Together, we're making the digital world a safer place! 🌍💪🔒

