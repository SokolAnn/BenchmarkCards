# Colloquial Persian POS (CPPOS) Corpus

## 📊 Benchmark Details

**Name**: Colloquial Persian POS (CPPOS) Corpus

**Overview**: This paper introduces a novel corpus, 'Colloquial Persian POS' (CPPOS), specifically designed to support colloquial Persian text. The corpus includes formal and informal text collected from various domains such as political, social, and commercial on Telegram, Twitter, and Instagram with more than 520K labeled tokens.

**Data Type**: tokens

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- Bijankhan

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To address the gap in available datasets for part-of-speech tagging in colloquial Persian text.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Part-of-Speech Tagging

**Limitations**: N/A

## 💾 Data

**Source**: Social media platforms (Telegram, Twitter, and Instagram), with data collected over a period of one year.

**Size**: 520,000 tokens

**Format**: N/A

**Annotation**: Manual annotation by a team of linguistic experts following a defined guideline.

## 🔬 Methodology

**Methods**:
- Deep Learning Models
- BiLSTM

**Metrics**:
- Accuracy

**Calculation**: Categorical cross-entropy loss function to compute the loss between predicted and actual values.

**Interpretation**: Higher accuracy indicates better performance of the model on POS tagging.

**Baseline Results**: BiLSTM achieved 90.42% accuracy, outperforming Hazm which achieved 76.58%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
