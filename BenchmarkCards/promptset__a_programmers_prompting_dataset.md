# PromptSet: A Programmer’s Prompting Dataset

## 📊 Benchmark Details

**Name**: PromptSet: A Programmer’s Prompting Dataset

**Overview**: PromptSet is a dataset containing more than 61,000 unique developer prompts used in open source Python programs, created to understand developer interactions with large language models (LLMs) integrated into applications.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/pisterlabs/promptset)
- [GitHub Repository](https://github.com/pisterlabs/promptset)

## 🎯 Purpose and Intended Users

**Goal**: To better understand how developers interact with large language models through prompt management and provide tools for better prompt hygiene.

**Target Audience**:
- ML Researchers
- Software Developers
- Industry Practitioners

**Tasks**:
- Prompt Management

**Limitations**: The dataset may not include all relevant data points and should be interpreted with caution due to potential gaps.

## 💾 Data

**Source**: Open source Python code files scraped from GitHub that utilize LLM libraries.

**Size**: 61,448 unique prompts

**Format**: JSON

**Annotation**: Prompts were extracted using an automated scraping process and categorized based on usage.

## 🔬 Methodology

**Methods**:
- Automated scraping
- Static analysis
- Data categorization

**Metrics**:
- Unique prompt count
- Prompt length distribution
- Language distribution

**Calculation**: Metrics calculated by analyzing the extracted prompt data for unique counts and distributions.

**Interpretation**: The metrics indicate the diversity and characteristics of prompts used in open-source projects.

**Validation**: Prompts were validated through manual reviews to identify extraction accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The majority of prompts were found to be in English, with minimal representation from other languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
