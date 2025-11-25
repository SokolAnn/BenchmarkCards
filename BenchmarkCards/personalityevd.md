# PersonalityEvd

## 📊 Benchmark Details

**Name**: PersonalityEvd

**Overview**: PersonalityEvd is an explainable personality recognition dataset constructed based on the Chain-of-Personality-Evidence (CoPE) framework, consisting of dialogues annotated with personality state and trait labels along with corresponding reasoning evidence.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- FriendsPersona
- PAN-2015
- MyPersonality

**Resources**:
- [GitHub Repository](https://github.com/Lei-Sun-RUC/PersonalityEvd)

## 🎯 Purpose and Intended Users

**Goal**: To support research in explainable personality recognition by providing a dataset and tasks that require revealing the reasoning process behind personality trait predictions.

**Target Audience**:
- ML Researchers
- Psychology Researchers
- Industry Practitioners

**Tasks**:
- Evidence grounded Personality State Recognition
- Evidence grounded Personality Trait Recognition

**Limitations**: The dataset primarily contains Chinese dialogues, and its small size is constrained by the high cost of annotation.

## 💾 Data

**Source**: Constructed from the CPED corpus, which is a large-scale Chinese emotional dialogue dataset.

**Size**: 1,924 dialogues

**Format**: N/A

**Annotation**: Annotated manually by psychology experts, combined with pre-annotations from GPT-4.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BERTScore

**Calculation**: Metrics are calculated based on predicted personality state and trait labels compared to ground truth.

**Interpretation**: Higher accuracy and F1 scores indicate better model performance in recognizing personality traits.

**Baseline Results**: ChatGLM3-6B-32K outperforms other models for personality recognition tasks, achieving high F1 scores.

**Validation**: Extensive human evaluation ensures the quality of annotated data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes a demographic breakdown based on the Big Five personality assessments.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses publicly available dialogues without intellectual property concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent is obtained from participants used in the originating dataset.

**Compliance With Regulations**: Not Applicable
