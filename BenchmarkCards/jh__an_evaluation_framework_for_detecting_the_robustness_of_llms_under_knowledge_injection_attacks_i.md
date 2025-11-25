# J&H: an evaluation framework for detecting the robustness of LLMs under knowledge injection attacks in the legal domain

## 📊 Benchmark Details

**Name**: J&H: an evaluation framework for detecting the robustness of LLMs under knowledge injection attacks in the legal domain

**Overview**: This paper proposes a framework for evaluating the robustness of Large Language Models (LLMs) under knowledge injection attacks specifically in the legal domain, utilizing a syllogistic reasoning approach.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/THUlawtech/LegalAttack)

## 🎯 Purpose and Intended Users

**Goal**: To explore whether LLMs perform deductive reasoning when accomplishing legal tasks through knowledge injection attacks.

**Target Audience**:
- ML Researchers
- Legal Practitioners

**Tasks**:
- Legal Judgment Prediction

**Limitations**: N/A

## 💾 Data

**Source**: LEVEN and CAIL2018 legal datasets

**Size**: 15,806 examples for CAIL2018 and 8,116 examples for LEVEN

**Format**: Text

**Annotation**: Annotated by legal experts for legal synonyms, logical inference, and similar crime names.

## 🔬 Methodology

**Methods**:
- Knowledge injection attacks
- Adversarial attack methods

**Metrics**:
- Original Accuracy
- Attack Accuracy
- Performance Drop Ratio (PDR)

**Calculation**: PDR is calculated based on the reduction in accuracy after an attack compared to the original accuracy.

**Interpretation**: Higher PDR indicates lower model robustness under adversarial attacks.

**Baseline Results**: Various LLM models were evaluated, showing significant drops in performance under attacks.

**Validation**: Robustness of LLMs was evaluated through a series of structured logical reasoning tests and knowledge injection scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
