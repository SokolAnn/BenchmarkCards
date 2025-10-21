# SKILL VERSE (Skill Versatile Evaluation)

## 📊 Benchmark Details

**Name**: SKILL VERSE (Skill Versatile Evaluation)

**Overview**: SKILL VERSE introduces an unsupervised tree-structured diagnosis framework for understanding the proficiency of language models in specific abilities, improving in-context learning and predicting model weaknesses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- ChatbotArena

**Resources**:
- [Resource](https://arxiv.org/abs/2506.00319)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic assessment framework for language model capabilities and to enhance model evaluation through detailed, granular insights.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Model Evaluation
- In-Context Learning Improvement
- Error Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Combination of datasets from ChatbotArena and Instruction-Following Eval (IFEval).

**Size**: 450 prompts from IFEval and 2,500 prompts from ChatbotArena

**Format**: JSON

**Annotation**: Atomic judgments generated from critiques provided by LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Hierarchical clustering

**Metrics**:
- Success rates
- Precision
- Recall

**Calculation**: Success rates calculated based on the ability to correctly identify model performance via atomic judgments and clustering results.

**Interpretation**: Higher success rates indicate better model performance on specific tasks.

**Baseline Results**: N/A

**Validation**: Cluster validity assessed through human evaluation and inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Misuse**: Non-disclosure

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
