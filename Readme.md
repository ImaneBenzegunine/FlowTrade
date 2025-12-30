---

### Part 2: The Meeting Presentation Script

Use this script to present your architecture. It is broken down by the flow of data, explaining *what* the tech is and *why* you used it.

**[Opening]**
"Hello everyone. Today I am presenting my **Real-Time Financial Data Pipeline**.

The goal of this project was to move away from simple local scripts and build a robust, scalable cloud architecture that can handle real-time market data for Bitcoin, Ethereum, and Gold. I have migrated the entire infrastructure to **Google Cloud Platform (GCP)** to leverage its specialized data services.

Here is how the data flows through the cloud."

**[Step 1: Ingestion (IaaS)]**
"First, we start with **Data Ingestion**.
*   **The Tech:** I am using **Google Compute Engine**, which is GCP's Infrastructure-as-a-Service (IaaS).
*   **The Logic:** I provisioned a Virtual Machine running Linux. On this VM, I deployed a **FastAPI** application.
*   **The Role:** This acts as our 'Producer'. It wakes up every minute, queries the Yahoo Finance API, and packages the data. We use a VM here because we need a persistent environment to manage the scheduling."

**[Step 2: Streaming (Messaging)]**
"Next, instead of saving files directly, I send the data to **Cloud Pub/Sub**.
*   **The Tech:** This is GCP's asynchronous messaging service.
*   **The Role:** This is critical for decoupling. If my processing server goes down, Pub/Sub holds the messages so we don't lose any financial data. It acts as a buffer between the source and the storage."

**[Step 3: Storage (Data Lake)]**
"From the stream, the data lands in **Google Cloud Storage (GCS)**.
*   **The Tech:** This is Object Storage (similar to S3).
*   **The Role:** I set up a 'Multi-Zone' Data Lake architecture:
    1.  **The Raw Zone:** Where we dump the raw JSON files exactly as they come from the API.
    2.  **The Curated Zone:** Where the clean data lives.
    This separates our 'messy' data from our 'analytics-ready' data."

**[Step 4: ETL (Processing)]**
"To get data from Raw to Curated, I use an **ETL Process**.
*   **The Tech:** I am using **PySpark** on a separate compute instance.
*   **The Role:** This extracts the JSON, fixes the 'missing crypto data' issues we identified earlier, removes duplicates, and converts the files into structured CSVs ready for analysis."

**[Step 5: Visualization (Serverless)]**
"Finally, for the end-user, I deployed a dashboard using **Cloud Run**.
*   **The Tech:** This is GCP's Serverless Container platform.
*   **The Role:** It hosts a **Streamlit** application. The beauty of Cloud Run is that it automatically scales. If 100 people view the dashboard, it scales up; if no one uses it, it scales down to zero to save costs."

**[Closing & Disclaimer]**
"A quick note on usage: This is currently a **live, real-time project**. The pipelines are active and incurring costs. Therefore, the repository is restricted. If anyone here is interested in testing the live dashboard or reviewing the source code, please contact me directly, and I can provision access credentials.

Thank you. I am happy to answer questions about the GCP architecture."
