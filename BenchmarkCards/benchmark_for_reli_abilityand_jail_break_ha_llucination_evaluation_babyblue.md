# Benchmark for reli ABilitYand jail Break ha LlUcination Evaluation (BABYBLUE)

## 📊 Benchmark Details

**Name**: BABYBLUE

**Overview**: BABYBLUE introduces a specialized validation framework including various evaluators to enhance existing jailbreak benchmarks, ensuring outputs are useful malicious instructions. It aims to evaluate the true potential of jailbroken LLM outputs to cause harm to human society.

**Data Type**: N/A

**Domains**:
- Artificial Intelligence
- Natural Language Processing
- Safety Evaluation

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench
- HarmBench

**Resources**:
- [GitHub Repository](https://github.com/Meirtz/BabyBLUE-llm)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the true threats posed by LLM jailbreaks, distinguishing between genuine threats and hallucinations.

**Target Audience**:
- Researchers
- AI Safety Analysts
- Developers of Language Models

**Tasks**:
- Assessing AI safety
- Evaluating jailbreak vulnerabilities
- Improving robustness against adversarial prompts

**Limitations**: None

**Out of Scope Uses**:
- Harming individuals or groups
- Promoting illegal activities

## 💾 Data

**Source**: Augmented dataset with examples of existing malicious behaviors.

**Size**: N/A

**Format**: N/A

**Annotation**: Meticulously curated examples that include both new behaviors and enhancements or modifications to existing behaviors.

## 🔬 Methodology

**Methods**:
- Reasoning-based classification
- Textual quality evaluation
- Functionality evaluation

**Metrics**:
- Attack Success Rate (ASR)
- Precision
- Recall
- F1 Score

**Calculation**: Evaluators calculate metrics based on classifications and assessments of each completion.

**Interpretation**: Results are interpreted to differentiate between hallucinatory completions and genuinely harmful behaviors.

**Baseline Results**: N/A

**Validation**: Validation through comparison against human expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety
- Security

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Prompt injection attack, Extraction attack
- **Explainability**: Inaccessible training data

**Potential Harm**: ['Potential misuse of outputs for harmful instructions', 'Inducing hallucinatory behavior leading to false safety messages']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Maintains privacy and follows legal guidelines in dataset construction to avoid disclosing sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
