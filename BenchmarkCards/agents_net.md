# AGENTS NET

## 📊 Benchmark Details

**Name**: AGENTS NET

**Overview**: AGENTS NET is a new benchmark for multi-agent reasoning that measures the ability of multi-agent systems to collaboratively form strategies for problem-solving, self-organization, and effective communication given a network topology. It evaluates multi-agent systems on fundamental distributed computing problems such as leader election, consensus, maximal matching, and others.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GAIA

**Resources**:
- [GitHub Repository](https://github.com/floriangroetschla/AgentsNet)
- [Resource](https://huggingface.co/datasets/disco-eth/AgentsNet)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of agentic networks to coordinate and collaborate to solve problems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Leader Election
- Consensus
- Maximal Matching
- Coloring
- Vertex Cover

**Limitations**: N/A

## 💾 Data

**Source**: Custom generated problems based on distributed computing tasks.

**Size**: Up to 100 agents with practically unlimited scalability.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores are based on strict correctness criteria, where instances are only considered solved if every agent satisfies the task specification.

**Interpretation**: A valid global solution confirms coordinated conflict resolution among agents.

**Baseline Results**: N/A

**Validation**: Validated by running multiple instances and averaging results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
