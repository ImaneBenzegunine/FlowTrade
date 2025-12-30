
# ⚡ GCP Real-Time Financial Data Pipeline

![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PubSub](https://img.shields.io/badge/Pub%2FSub-Streaming-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

> **A scalable, event-driven architecture capturing Bitcoin, Ethereum, and Gold market data in real-time.**

---

## 📖 Project Overview

<img width="1085" height="605" alt="image" src="https://github.com/user-attachments/assets/68363022-a9dd-42f1-a97e-663b715d093f" />

This project is not just a data scraper; it is a fully automated **Cloud Data Engineering Pipeline**. It demonstrates the lifecycle of financial data—from extraction to visualization—using a modern **Google Cloud Platform (GCP)** infrastructure.

By leveraging **Serverless Computing**, **Streaming Protocols**, and **Data Lakes**, this system solves the challenge of handling high-frequency market data with fault tolerance and scalability.

<img width="904" height="384" alt="image" src="https://github.com/user-attachments/assets/6766e3fb-c551-45e0-b335-97032827806a" />

### 🎯 Key Objectives
*   **Ingestion:** Harvest live OHLCV (Open, High, Low, Close, Volume) data every 2 minutes.
*   **Decoupling:** Use Message Queues to ensure data is never lost, even if the processing layer fails.
*   **Data Lake:** Implement a "Raw" vs. "Curated" storage strategy for historical auditing.
*   **Visualization:** Provide a live, interactive dashboard for trend analysis.

---

## 🏗️ Cloud Migration to GCP

The system follows a linear DAG (Directed Acyclic Graph) workflow, moving data from ingestion to insight.
<img width="1060" height="133" alt="image" src="https://github.com/user-attachments/assets/62433940-1fbd-4732-84ee-2d8d2eb85d50" />

🛠️ Technology Stack

This project uses a "Best Tool for the Job" approach:

Component	Service / Tool	Description
Ingestion	GCP Compute Engine	Hosts a persistent FastAPI producer that queries Yahoo Finance on a cron schedule.
Streaming	Cloud Pub/Sub	Acts as the async message broker, buffering events to handle throughput spikes.
Storage	Cloud Storage (GCS)	Object storage acting as the Data Lake. Divided into buckets/raw (JSON) and buckets/curated (CSV).
ETL	PySpark / Python	Cleanses data, handles null values in crypto feeds, and dedupes records.
Frontend	Cloud Run	Hosts the Streamlit dashboard in a serverless container, auto-scaling based on traffic.
🚀 How It Works (The Pipeline)

The Trigger: A Python script on the VM wakes up every 60 seconds.

The Fetch: It requests the latest 1-minute candle for BTC-USD, ETH-USD, and GC=F (Gold).

The Stream: Data is serialized to JSON and pushed to a Pub/Sub Topic.

The Sink: A subscriber worker pulls the message and writes it to the Raw Data Zone (GCS).

The Transform: An ETL process picks up raw files, flattens the JSON, fixes timestamps, and writes clean rows to the Curated Zone.

The View: The Streamlit App (running on Cloud Run) reads the Curated CSVs and updates the charts in real-time.

