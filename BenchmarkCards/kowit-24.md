# KOWIT-24

## 📊 Benchmark Details

**Name**: KOWIT-24

**Overview**: KOWIT-24 is a dataset with fine-grained annotation of wordplay in 2,700 Russian news headlines, including the presence of wordplay, its type, wordplay anchors, and entities the wordplay refers to, accompanied by news leads and summaries.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- EnglishPuns
- ExPUN

**Resources**:
- [GitHub Repository](https://github.com/Humor-Research/KoWit-24)

## 🎯 Purpose and Intended Users

**Goal**: To provide a richly annotated dataset for wordplay detection and interpretation tasks using modern LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Wordplay Detection
- Wordplay Interpretation

**Limitations**: The annotation process may vary depending on individual interpretation and biases from the specific editorial style of the source.

## 💾 Data

**Source**: Collected from the Kommersant news outlet via RSS feed.

**Size**: 2,700 headlines

**Format**: JSON

**Annotation**: Manual annotation by fluent annotators including linguists and computer scientists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Precision

**Calculation**: Metrics were calculated based on the performance of five LLMs on wordplay detection and interpretation tasks.

**Interpretation**: Higher scores indicate better performance in recognizing and understanding wordplay.

**Baseline Results**: GPT-4o demonstrated the strongest performance in both tasks.

**Validation**: Data validation was performed through peer discussion and reconciliation of discrepancies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Instances of wordplay in sensitive topics may be deemed unacceptable by some audiences.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Dataset collected in accordance with Kommersant's copyright policy.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
