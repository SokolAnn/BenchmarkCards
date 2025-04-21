# PromptRobust

## 📊 Benchmark Details

**Name**: PromptRobust

**Overview**: PromptRobust is a robustness benchmark designed to measure LLMs’ resilience to adversarial prompts across multiple levels: character, word, sentence, and semantic.

**Data Type**: Text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AdvGLUE
- ANLI

**Resources**:
- [Resource](https://arxiv.org/abs/2306.04528)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of LLMs to adversarial prompts and provide insights for better prompt composition.

**Target Audience**:
- Researchers
- Practitioners
- Model developers
- End-users

**Tasks**:
- Sentiment analysis
- Natural language inference
- Machine translation
- Reading comprehension
- Math problem solving

**Limitations**: The benchmark primarily evaluates robustness against adversarial prompts, not input samples.

**Out of Scope Uses**:
- Non-adversarial evaluations
- Evaluation on samples alone

## 💾 Data

**Source**: Generated through various prompt conditions and attacks.

**Size**: 4788 adversarial prompts generated.

**Format**: Text

**Annotation**: Prompts perturbed to simulate user errors and analyze responsiveness of LLMs.

## 🔬 Methodology

**Methods**:
- Character-level attacks
- Word-level attacks
- Sentence-level attacks
- Semantic-level attacks

**Metrics**:
- Performance Drop Rate (PDR)

**Calculation**: Performance Drop Rate calculated based on relative performance decline post-prompt attack.

**Interpretation**: Higher PDR indicates lower model robustness to adversarial prompts.

**Baseline Results**: Initial performance of LLMs without prompt attacks.

**Validation**: Comprehensive evaluation across 9 LLMs using diverse tasks and datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Privacy

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Data poisoning
- **Fairness**: Data bias
- **Privacy**: Reidentification, Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: Adversarial prompts may lead to incorrect outputs in critical tasks affecting user decisions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Adversarial prompts created for testing without user data.

**Data Licensing**: Adversarial prompts generated from public datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Follows ethical standards in ML research.
