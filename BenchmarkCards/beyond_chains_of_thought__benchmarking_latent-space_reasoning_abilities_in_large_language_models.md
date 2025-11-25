# Beyond Chains of Thought: Benchmarking Latent-Space Reasoning Abilities in Large Language Models

## 📊 Benchmark Details

**Name**: Beyond Chains of Thought: Benchmarking Latent-Space Reasoning Abilities in Large Language Models

**Overview**: This study introduces a benchmark designed to quantify model-internal reasoning in different domains by having LLMs indicate the correct solution to reasoning problems using a language different from English, thereby requiring complex reasoning leaps.

**Data Type**: reasoning items

**Domains**:
- Natural Language Processing

**Languages**:
- Italian
- Afrikaans
- Spanish
- German
- French
- Indonesian
- Russian
- Polish

**Resources**:
- [Resource](https://osf.io/u269r/)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and quantify reasoning leaps in large language models by evaluating their internal reasoning abilities.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated using GPT-4.5 and manually designed template benchmark items.

**Size**: 4,000 items

**Format**: N/A

**Annotation**: Manually double-checked and automatically validated using LLM-based scripts.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Statistical differences between models evaluated using a two-proportion z-test.

**Interpretation**: Higher accuracy indicates better model-internal reasoning capabilities.

**Baseline Results**: GPT-4.5 achieved 74.7% accuracy.

**Validation**: Validated through control experiments and difficulty scaling analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
