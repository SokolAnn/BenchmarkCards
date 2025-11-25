# LegalAgentBench

## 📊 Benchmark Details

**Name**: LegalAgentBench

**Overview**: LegalAgentBench is a comprehensive benchmark specifically designed to evaluate LLM agents in the Chinese legal domain, including 17 corpora from real-world legal scenarios and providing 37 tools for interaction with external knowledge. It evaluates complex legal tasks through a scalable task construction framework and fine-grained metrics.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- AgentBench
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/CSHaitao/LegalAgentBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLM agents in the legal domain.

**Target Audience**:
- Legal Professionals
- ML Researchers

**Tasks**:
- Multi-hop Reasoning
- Legal Research
- Contract Drafting

**Limitations**: The current dataset is primarily constructed in Chinese, which limits its applicability in broader multilingual contexts.

## 💾 Data

**Source**: Real-world legal scenarios including court information, law firms, and legal documents.

**Size**: 300 tasks

**Format**: N/A

**Annotation**: Human-verified for accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Plan-and-Solve
- Plan-and-Execute
- ReAct

**Metrics**:
- Success Rate
- Process Rate
- BERT-Score

**Calculation**: Success Rate is calculated based on keyword matching between generated answers and reference answers. Process Rate incorporates intermediate keywords.

**Interpretation**: Higher success and process rates indicate better performance of LLM agents in handling legal tasks.

**Baseline Results**: Various LLMs including GLM-4, GPT-4o achieved varying success rates across tasks.

**Validation**: Tasks are validated through human verification of correctness and appropriateness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data has undergone privacy screening and anonymization processes.

**Data Licensing**: MIT License.

**Consent Procedures**: All data used complies with legal and ethical standards.

**Compliance With Regulations**: Not Applicable
