# Hummer

## 📊 Benchmark Details

**Name**: Hummer

**Overview**: Hummer is a novel pairwise preference dataset designed to reduce conflicts among alignment objectives, enhancing reinforcement learning from human feedback by minimizing competing dynamics in preference datasets.

**Data Type**: pairwise preference data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- UltraFeedback

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that reduces conflicts among alignment objectives to improve downstream applications in language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Preference Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Hummer is constructed based on the UltraFeedback dataset, utilizing AI feedback mechanisms such as GPT-4 for annotation and refinement.

**Size**: 46,000 examples

**Format**: Raw text files

**Annotation**: Annotated through human feedback using AI systems.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Alignment Dimension Conflict (ADC)
- Reward model accuracy

**Calculation**: The ADC is calculated as the second-order moment of negative performance deviation on all evaluation dimensions in the benchmark, focusing on performance reductions across different alignment objectives.

**Interpretation**: A lower ADC value indicates reduced conflict among alignment objectives, which is desirable for effective preference modeling.

**Baseline Results**: Compared with existing preference datasets like Anthropic HH and UltraFeedback, Hummer shows improved performance and reduced ADC.

**Validation**: Validated through performance comparison on standard evaluation metrics across different datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Reducing vulnerabilities to jailbreak attacks by balancing performance across objectives.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
