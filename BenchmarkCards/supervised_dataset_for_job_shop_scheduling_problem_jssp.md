# Supervised Dataset for Job Shop Scheduling Problem (JSSP)

## 📊 Benchmark Details

**Name**: Supervised Dataset for Job Shop Scheduling Problem (JSSP)

**Overview**: This paper introduces the very first supervised 120k dataset specifically designed to train Large Language Models (LLMs) for the Job Shop Scheduling Problem (JSSP), enabling effective LLM training through natural language descriptions of the scheduling problem and solutions.

**Data Type**: natural language descriptions and solutions of job scheduling problems

**Domains**:
- Artificial Intelligence
- Operations Research

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/starjob42/datasetjsp)

## 🎯 Purpose and Intended Users

**Goal**: To provide a specialized dataset for training and evaluating large language models in solving the Job Shop Scheduling Problem (JSSP).

**Target Audience**:
- ML Researchers
- AI Practitioners
- Operations Researchers

**Tasks**:
- Job Shop Scheduling

**Limitations**: N/A

## 💾 Data

**Source**: Generated using Google's OR-Tools for random JSSP problems.

**Size**: 120,000 examples

**Format**: Natural Language format

**Annotation**: Automatically generated using OR-Tools to solve scheduling problems.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Comparative analysis with existing neural approaches

**Metrics**:
- Makespan gap from optimal solutions

**Calculation**: Calculated by comparing the makespan of the generated schedules with the optimal makespan identified by the OR-Tools solver.

**Interpretation**: Lower gaps indicate better performance in scheduling; a gap closer to 0% is desirable.

**Baseline Results**: Average gap of 8.92% for the proposed model compared to 13.01% for existing methods.

**Validation**: Used a separate evaluation dataset of random problems distinct from the training data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
