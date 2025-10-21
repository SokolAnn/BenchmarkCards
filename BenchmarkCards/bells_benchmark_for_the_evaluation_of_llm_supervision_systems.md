# BELLS (Benchmark for the Evaluation of LLM Supervision Systems)

## 📊 Benchmark Details

**Name**: BELLS (Benchmark for the Evaluation of LLM Supervision Systems)

**Overview**: The BELLS benchmark systematically evaluates supervision systems for LLMs across two key axes—harm severity and adversarial sophistication—covering three jailbreak families and eleven harm categories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GuardBench
- JailbreakBench
- HarmBench
- SORRY-Bench

**Resources**:
- [GitHub Repository](https://github.com/yourusername/bells)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive public benchmark that verifies the performance of supervision systems under realistic and diverse attacks.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Misuse Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing harm taxonomies and non-adversarial prompt collections, with adversarial data augmented using various techniques.

**Size**: 5,990 prompts (990 non-adversarial prompts and 5,000+ adversarial prompts)

**Format**: N/A

**Annotation**: Initial categorization by GPT-4 followed by independent human review.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Detection Rate Adversarial Harmful
- Detection Rate Non-Adversarial Harmful
- False Positive Rate
- BELLS Score

**Calculation**: The BELLS Score combines detection rates on adversarial and non-adversarial harmful prompts, penalized by false positive rates.

**Interpretation**: Higher BELLS Scores indicate better overall performance in detecting harmful content while minimizing false positives.

**Baseline Results**: N/A

**Validation**: Benchmark evaluated against specialized supervision systems and general-purpose LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: ['Misuse of LLMs', 'Harmful content production']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
