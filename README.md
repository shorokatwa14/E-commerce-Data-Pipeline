# Batch and Streaming E-commerce Data Pipeline with PySpark

## Overview
This project is part of the Samsung Innovation Campus training .this project demonstrates a PySpark-based data pipeline for batch and real-time processing of e-commerce data, including data ingestion, cleaning, transformation, analysis, and visualization.

## Features
- Batch data processing from CSV and JSON files (Customer Feedback, Transactions, Inventory)
- Real-time data streaming using Spark Streaming
- Data cleaning (missing values, anonymization)
- Data transformation and enrichment (normalization, categorization)
- Performance optimization (caching, repartitioning, broadcast joins)
- Visualizations (top products, revenue trends)

## Requirements
- **PySpark**: `pip install pyspark`
- **Matplotlib & Seaborn**: `pip install matplotlib seaborn` (for visualizations)

## Pipeline Flow
1. **Data Ingestion**: Load data from CSV/JSON files.
2. **Data Cleaning**: Handle missing data, anonymize sensitive info.
3. **Transformation**: Normalize and categorize data, join datasets.
4. **Analysis**: Run SQL queries for insights (top products, revenue trends).
5. **Optimization**: Cache, repartition, and broadcast join data for performance.
6. **Streaming**: Process real-time data via socket streaming.
7. **Storage**: Save batch processed data in Parquet format.


