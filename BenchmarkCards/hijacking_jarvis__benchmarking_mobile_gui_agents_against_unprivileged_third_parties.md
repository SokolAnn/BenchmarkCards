# Hijacking JARVIS: Benchmarking Mobile GUI Agents against Unprivileged Third Parties

## 📊 Benchmark Details

**Name**: Hijacking JARVIS: Benchmarking Mobile GUI Agents against Unprivileged Third Parties

**Overview**: This paper presents a systematic investigation into the vulnerabilities of mobile GUI agents through a benchmark suite that evaluates their robustness against misleading content injected by unprivileged third parties. It introduces AgentHazard, a framework for simulating attack scenarios, and develops a comprehensive suite comprising a dynamic task execution environment and a static dataset.

**Data Type**: vision-language-action tuples

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.04227)

## 🎯 Purpose and Intended Users

**Goal**: To systematically study the vulnerabilities of mobile GUI agents against misleading content attacks and to improve their robustness.

**Target Audience**:
- Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Task Automation
- User Interface Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 210 screenshots of 14 popular commercial applications.

**Size**: 840 unique tasks and over 3,000 attack scenarios

**Format**: N/A

**Annotation**: Manual crafting by human annotators based on selected screenshots.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Behavioral analysis

**Metrics**:
- Success Rate (SR)
- Misleading Rate (MR)

**Calculation**: Metrics calculated based on the percentage of successful task completion versus misleading agent behavior.

**Interpretation**: A lower SR indicates greater vulnerability to misleading content.

**Baseline Results**: Varied across agents; UGround exhibited strongest performance with 48.3% baseline SR.

**Validation**: Tests conducted on 7 mobile GUI agents and various backbone LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['User data loss due to misleading instructions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
