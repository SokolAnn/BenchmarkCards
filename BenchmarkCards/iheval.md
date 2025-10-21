# IHEval

## 📊 Benchmark Details

**Name**: IHEval

**Overview**: IHEval is a novel benchmark comprising 3,538 examples across nine tasks, designed to evaluate models' ability to follow the instruction hierarchy while handling cases where instructions may align or conflict.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish

**Similar Benchmarks**:
- SysBench

**Resources**:
- [Resource](https://ytyz1307zzh.github.io/iheval.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models' ability to follow the instruction hierarchy and identify their weaknesses in handling conflicting instructions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Rule Following
- Task Execution
- Safety Defense
- Tool Use

**Limitations**: N/A

## 💾 Data

**Source**: Internally created dataset with examples derived from public benchmarks and expert reviews.

**Size**: 3,538 examples

**Format**: N/A

**Annotation**: Manually reviewed by experts to ensure data quality and coherence.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the models' output adherence to the instruction hierarchy.

**Interpretation**: Higher scores indicate better adherence to the instruction hierarchy, while significant drops signal difficulty managing instruction conflicts.

**Baseline Results**: N/A

**Validation**: Programmatic evaluation ensuring efficient and reproducible results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from public benchmarks and reviewed to avoid sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
