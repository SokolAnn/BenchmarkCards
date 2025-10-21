# JAMBench

## 📊 Benchmark Details

**Name**: JAMBench

**Overview**: JAMBench is a harmful behavior benchmark designed to trigger and evaluate moderation guardrails of large language models. It consists of 160 manually crafted questions covering four major risk categories at multiple severity levels.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- In-the-Wild
- HarmBench
- JailbreakBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of jailbreaks against moderation guardrails in large language models.

**Target Audience**:
- Researchers
- Ethical Hackers
- AI Developers

**Tasks**:
- Red-Teaming Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Manually crafted questions by the authors, categorized into four critical risk areas.

**Size**: 160 examples

**Format**: N/A

**Annotation**: Manually crafted

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Jailbreak Success Rate
- Filtered-out Rate

**Calculation**: The jailbreak success rate (σ) is calculated as the number of successful jailbreaks divided by the total number of attempts. The filtered-out rate (ζ) is calculated as the number of responses filtered by the moderation guardrails divided by the total number of jailbreak attempts.

**Interpretation**: A higher jailbreak success rate indicates better effectiveness of the jailbreak method, while a lower filtered-out rate indicates fewer blockages by the moderation guardrails.

**Baseline Results**: Comparison against existing jailbreak methods from previous benchmarks.

**Validation**: Extensive experiments on four large language models: GPT-3.5, GPT-4, Gemini, and Llama-3.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethics

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Dangerous use

**Demographic Analysis**: N/A

**Potential Harm**: ['Self-harm', 'Violence']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
