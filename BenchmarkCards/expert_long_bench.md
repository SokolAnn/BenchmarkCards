# EXPERT LONG BENCH

## 📊 Benchmark Details

**Name**: EXPERT LONG BENCH

**Overview**: EXPERT LONG BENCH is an expert-level benchmark containing 11 tasks from 9 domains that reflect realistic expert workflows and applications, designed to evaluate long-form outputs that adhere to domain-specific requirements.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare
- Legal
- Education
- Finance
- Computer Science
- Chemistry
- Biology
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- ExpertQA
- WildBench
- BIG-Bench
- GPQA

**Resources**:
- [Resource](https://huggingface.co/spaces/launch/ExpertLongBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multi-disciplinary benchmark designed to evaluate the capabilities of large language models on real-world expert-level tasks that require long-form inputs and outputs, using expert-written references for grounded evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering
- Named Entity Recognition
- Machine Translation
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: VARIOUS EXPERT DOMAINS

**Size**: 1050 samples

**Format**: text

**Annotation**: Manual annotations by domain experts, structured according to expert-designed rubrics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Checklist-based evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on checklist-mapped evaluations of model outputs against expert references.

**Interpretation**: Higher F1 and accuracy scores indicate better performance on complex, domain-specific tasks.

**Baseline Results**: Top-performing models evaluated against the expert-level benchmark include Gemini-2.0-Flash and GPT-4o.

**Validation**: Validation is based on manual verification of model outputs matched to human-written references and expert-designed rubrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0 for most datasets, with some datasets remaining private.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
