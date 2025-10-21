# MATHARENA

## 📊 Benchmark Details

**Name**: MATHARENA

**Overview**: MATHARENA is a dynamic publicly available benchmark designed to evaluate LLMs on uncontaminated problems sourced from recurring math competitions, targeting mathematical reasoning and proof-writing capabilities.

**Data Type**: problem-solving tasks

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- AIME
- FrontierMath
- HLE
- GSM8K
- MINIF2F

**Resources**:
- [Resource](https://matharena.ai/)
- [GitHub Repository](https://github.com/eth-sri/matharena)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the mathematical reasoning capabilities of large language models using uncontaminated math competition problems.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Problem Solving
- Proof Writing

**Limitations**: The benchmark is limited by the number of annual competitions available.

## 💾 Data

**Source**: Problems sourced from various math competitions including AIME, HMMT, USAMO, and others.

**Size**: 162 problems across 7 competitions

**Format**: JSON

**Annotation**: Problems are formatted and pre-validated for accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the average performance across multiple model runs per problem.

**Interpretation**: Higher accuracy indicates better reasoning capabilities in LLMs, while the leaderboard ranks models based on their performance.

**Validation**: Regular updates with newly released competition problems ensure the relevance and difficulty of the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis includes performance across different types of math problems, addressing any potential biases in problem distribution.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is available under CC-BY-NC-SA 4.0 license for non-commercial use.

**Consent Procedures**: All data releases comply with the policies of competition organizers.

**Compliance With Regulations**: Not Applicable
