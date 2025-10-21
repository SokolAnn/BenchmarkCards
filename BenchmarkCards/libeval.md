# LibEval

## 📊 Benchmark Details

**Name**: LibEval

**Overview**: LibEval is a benchmark designed to evaluate the performance in the library migration recommendation task, assessing the effectiveness of various LLMs using 2,888 migration records.

**Data Type**: migration records

**Domains**:
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.09791)

## 🎯 Purpose and Intended Users

**Goal**: To assess the performance of LibRec in recommending target libraries for library migration.

**Target Audience**:
- ML Researchers
- Software Developers

**Tasks**:
- Library Migration Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Data was extracted from 2,324 Python repositories focusing specifically on library migrations.

**Size**: 2,888 migration records

**Format**: N/A

**Annotation**: Migration intents were extracted from commit messages using LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision @k
- Mean Reciprocal Rank (MRR)

**Calculation**: Precision @k measures the inclusion of the correct target library within the top-k recommendations.

**Interpretation**: Higher scores indicate better recommendation performance.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through human evaluation of the extracted migration intents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
