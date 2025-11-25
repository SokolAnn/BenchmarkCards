# IMPersona

## 📊 Benchmark Details

**Name**: IMPersona

**Overview**: IMPersona is a framework introduced to evaluate language models' capabilities to impersonate specific individuals’ writing styles and personal knowledge. It involves a modified Turing test where participants interact with different IMPersona configurations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://impersona-website.vercel.app/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models’ capabilities in individual-level impersonation based on personal data.

**Target Audience**:
- ML Researchers
- AI Safety Researchers

**Tasks**:
- Natural Language Understanding
- Dialogue Generation

**Limitations**: N/A

## 💾 Data

**Source**: Messaging data from volunteers who provided consent.

**Size**: 13,000 examples

**Format**: N/A

**Annotation**: Manual annotation based on conversational exchanges and evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Blind conversation tests
- Automated metrics

**Metrics**:
- Pass Rate
- Humanness Score

**Calculation**: Calculated as the percentage of conversations where the AI is identified as human and rated on a scale of 1-7.

**Interpretation**: A higher pass rate and humanness score indicate better impersonation capabilities.

**Baseline Results**: Best configuration achieved a 44.44% pass rate compared to 25.00% for the best prompting-based approach.

**Validation**: Tested through interactions with human participants familiar with the impersonated individuals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse in social engineering and identity theft through realistic impersonation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Maintained through explicit consent from all participants, with control over their data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collection proceeded with explicit permission from all parties involved.

**Compliance With Regulations**: Conducted under full Institutional Review Board (IRB) approval.
