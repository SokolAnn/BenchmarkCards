# WebMall

## 📊 Benchmark Details

**Name**: WebMall

**Overview**: WebMall is a multi-shop benchmark for evaluating the effectiveness and efficiency of web agents for comparison-shopping. It consists of four simulated online shops populated with authentic product offers and a suite of 91 cross-shop tasks.

**Data Type**: product offers and tasks

**Domains**:
- E-Commerce

**Languages**:
- English

**Similar Benchmarks**:
- WebShop
- ShoppingBench

**Resources**:
- [GitHub Repository](https://github.com/wbsg-uni-mannheim/WebMall)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of WebMall is to evaluate and facilitate advancements in web agents' navigation, reasoning, and efficiency within e-commerce scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Comparison Shopping
- Product Search
- Shopping Cart Management
- Checkout Procedures

**Limitations**: N/A

## 💾 Data

**Source**: Four simulated online shops populated with authentic product offers sourced from the Common Crawl.

**Size**: 4,421 product offers

**Format**: JSON

**Annotation**: Manual selection and distribution of product offers across the shops.

## 🔬 Methodology

**Methods**:
- Baseline evaluation of eight agent configurations

**Metrics**:
- Completion Rate
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the results of the agents performing tasks, including aggregations across completed tasks.

**Interpretation**: Higher completion rates and F1 scores indicate better performance and efficiency of web agents.

**Baseline Results**: The best configuration achieved a completion rate of 75% and an F1 score of 87% for basic tasks.

**Validation**: Validation performed through baseline experiments with varying agent configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
