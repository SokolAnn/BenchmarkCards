# Vending-Bench

## 📊 Benchmark Details

**Name**: Vending-Bench

**Overview**: Vending-Bench is a simulated environment designed to test an LLM-based agent’s ability to manage a long-running business scenario: operating a vending machine, including tasks such as balancing inventories, placing orders, setting prices, and handling daily fees.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2502.15840)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate long-term coherence capabilities of LLM-based agents in managing a vending machine business.

**Target Audience**:
- ML Researchers
- AI Safety Researchers

**Tasks**:
- Resource Management
- Decision-Making
- Economic Simulation

**Limitations**: N/A

## 💾 Data

**Source**: Simulated environment with agent interactions and economic modeling.

**Size**: 5,000 messages

**Format**: N/A

**Annotation**: Automatically generated interactions based on predefined business rules and economic models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Net Worth

**Calculation**: Net Worth is calculated as the sum of cash on hand, cash not yet emptied from the vending machine, and the value of unsold products.

**Interpretation**: Higher net worth indicates better performance in managing the vending machine business.

**Validation**: Evaluated against human performance in completing similar tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
