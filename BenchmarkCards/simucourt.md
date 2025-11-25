# SimuCourt

## 📊 Benchmark Details

**Name**: SimuCourt

**Overview**: SimuCourt is a judicial benchmark that encompasses 420 Chinese judgment documents across criminal, civil, and administrative cases. It is designed to evaluate the judicial analysis and decision-making capability of AI agents simulating judges.

**Data Type**: judgment documents

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- CAIL
- SLJA-SYN

**Resources**:
- [Resource](https://wenshu.court.gov.cn/)

## 🎯 Purpose and Intended Users

**Goal**: To reliably assess the judicial analysis and decision-making power of intelligent agents in a court-like setting.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- AI Developers

**Tasks**:
- Judicial Decision-Making

**Limitations**: Our data only includes Chinese documents from 'China Judgments Online'. Testing the agent system with real data from different legal systems is important.

## 💾 Data

**Source**: 420 judgment documents collected from the China Judgements Online, covering a range of judicial cases.

**Size**: 420 examples

**Format**: N/A

**Annotation**: Documents were rigorously inspected for accuracy and completeness in legal texts and information.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on matching generated legal articles against reference legal articles.

**Interpretation**: Higher scores correlate to better alignment of AI-generated outputs with standard legal judgments.

**Baseline Results**: AgentsCourt framework demonstrated improvements of 8.6% and 9.1% in F1 scores for legal article generation.

**Validation**: Validation was performed through extensive experiments and ablation studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: We have meticulously anonymized sensitive information in the judgement documents.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
