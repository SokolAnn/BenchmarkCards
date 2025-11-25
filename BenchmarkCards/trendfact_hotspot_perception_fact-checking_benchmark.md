# TrendFact (Hotspot Perception Fact-Checking Benchmark)

## 📊 Benchmark Details

**Name**: TrendFact (Hotspot Perception Fact-Checking Benchmark)

**Overview**: TrendFact is the first hotspot perception fact-checking benchmark that comprehensively evaluates fact verification, evidence retrieval, and explanation generation tasks. It includes 7,643 curated samples and an evidence library consisting of 66,217 entries.

**Data Type**: fact-checking samples

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CHEF (Chinese Evidence-based Fact-checking Dataset)
- FEVEROUS

**Resources**:
- [GitHub Repository](https://github.com/zxc123cc/TrendFact)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal of TrendFact is to evaluate fact-checking systems’ performance in terms of explanation generation capabilities and their ability to perceive hotspot events.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Fact Verification
- Evidence Retrieval
- Explanation Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from trending platforms such as Weibo, Baidu, DouYin and existing datasets like CHEF.

**Size**: 7,643 samples

**Format**: N/A

**Annotation**: Data was annotated manually by a team of graduate students.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- ECS (Explanation Consistency Score)
- HCPI (Hotspot Claim Perception Index)

**Calculation**: Performance metrics are calculated based on responses to fact-checking tasks using predefined systems and metrics.

**Interpretation**: Good performance is indicated by high accuracy and consistency scores on the explanation tasks.

**Baseline Results**: Fact-checking model performance showed that even advanced systems struggle to achieve high accuracy, indicating the challenge presented by TrendFact.

**Validation**: TrendFact was validated through extensive experiments against various LLMs and RLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
