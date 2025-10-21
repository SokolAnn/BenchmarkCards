# SLM-Bench (Small Language Model-Benchmark)

## 📊 Benchmark Details

**Name**: SLM-Bench (Small Language Model-Benchmark)

**Overview**: SLM-Bench is the first benchmark specifically designed to assess Small Language Models (SLMs) across multiple dimensions, including accuracy, computational efficiency, and sustainability metrics. It evaluates 15 SLMs on 9 NLP tasks using 23 datasets spanning 14 domains.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare
- Finance
- Legal
- Education
- Computer Vision
- Social Activities
- Food & Beverage
- Video Games
- Chemistry

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [GitHub Repository](https://github.com/slm-bench/slm-bench-experiments)
- [Resource](https://slm-bench.github.io/leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To provide critical insights to guide the selection, optimization, and deployment of Small Language Models (SLMs), balancing accuracy, efficiency, and sustainability, especially in resource-constrained settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Reading Comprehension
- Sentiment Analysis
- Knowledge Extraction
- Text Generation
- Reasoning
- Problem Solving
- Classification

**Limitations**: Environmental metrics like energy consumption, CO₂ emissions, and runtime depend on hardware used.

## 💾 Data

**Source**: 23 datasets across diverse domains including customer behavior, healthcare, legal, and educational tasks.

**Size**: 799,594 samples

**Format**: Varied JSON and CSV, depending on dataset

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE
- METEOR
- Perplexity
- Runtime
- FLOP
- Cost
- CO2
- Energy Consumption

**Calculation**: Metrics are calculated based on the performance of models on specific tasks using standard evaluation techniques.

**Interpretation**: A higher number of medals correlates with better performance across tasks in terms of accuracy, efficiency, and sustainability.

**Baseline Results**: To be determined, models are compared to those of existing benchmarks.

**Validation**: Both controlled hardware conditions and standardized evaluation protocols are used.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Analysis of model performance across different demographic groups is recommended but not explicitly discussed.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
