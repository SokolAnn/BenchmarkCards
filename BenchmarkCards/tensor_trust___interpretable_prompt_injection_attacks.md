# Tensor Trust : Interpretable Prompt Injection Attacks

## 📊 Benchmark Details

**Name**: Tensor Trust : Interpretable Prompt Injection Attacks

**Overview**: Tensor Trust is a web-based game that allows players to create defense prompts for LLMs and attempt to bypass these defenses using prompt injections. The paper releases a dataset of over 126,000 prompt injection attacks and 46,000 defenses created by players, and introduces benchmarks for assessing LLMs' robustness against prompt extraction and hijacking attacks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Jailbreaking datasets

**Resources**:
- [Resource](https://tensortrust.ai/paper)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of LLMs against prompt injection attacks and to provide a dataset that facilitates research in this area.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners
- Model Developers

**Tasks**:
- Prompt Injection Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Created by players of the Tensor Trust online game, involving user-generated prompt injection attacks and defenses.

**Size**: 126,808 attacks and 46,457 defenses

**Format**: N/A

**Annotation**: Manual verification of attacks and defenses by the players.

## 🔬 Methodology

**Methods**:
- Dataset generation through user interaction in a web game
- Evaluation against multiple LLMs

**Metrics**:
- Hijacking Robustness Rate (HRR)
- Defense Validity (DV)
- Extraction Robustness Rate (ERR)

**Calculation**: HRR is calculated as the percentage of times the model avoids outputting 'Access Granted' during prompt hijacking attacks; DV measures the percentage of times valid defenses produce 'Access Granted' outputs when given the actual access code.

**Interpretation**: Higher scores in HRR indicate better resistance to prompt hijacking, while higher DV reflects effective defense prompts.

**Baseline Results**: Evaluated against models: GPT-3.5 Turbo, GPT-4, Claude Instant 1.2, Claude 2.0, and LLaMA models.

**Validation**: Adversarial filtering of attacks and defenses based on their performance against reference LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Security

**Atlas Risks**:
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User consent was obtained for data collection; data released is anonymized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were informed of data release as part of user consent.

**Compliance With Regulations**: Not Applicable
