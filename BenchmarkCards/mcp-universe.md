# MCP-Universe

## 📊 Benchmark Details

**Name**: MCP-Universe

**Overview**: MCP-Universe is the first comprehensive benchmark specifically designed to evaluate LLMs in realistic and challenging tasks through interaction with real-world Model Context Protocol (MCP) servers across six domains, including Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching.

**Data Type**: task instances with real-world interaction

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MCP-RADAR
- MCPWorld

**Resources**:
- [GitHub Repository](https://github.com/SalesforceAIResearch/MCP-Universe)
- [Resource](https://mcp-universe.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models (LLMs) in realistic MCP environments, addressing long-context handling, tool unfamiliarity, and application across diverse scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Location Navigation
- Repository Management
- Financial Analysis
- 3D Design
- Browser Automation
- Web Searching

**Limitations**: N/A

## 💾 Data

**Source**: Real-world MCP servers and user-created tasks.

**Size**: 231 tasks

**Format**: N/A

**Annotation**: Task instructions designed and validated by authors.

## 🔬 Methodology

**Methods**:
- Execution-based evaluation

**Metrics**:
- Success rate

**Calculation**: Success is determined through automated checks based on real-time data from MCP servers.

**Interpretation**: Higher success rates indicate better model performance across diverse real-world tasks.

**Baseline Results**: Top-performing models include GPT-5 (43.72% success rate), Grok-4 (33.33% success rate), and Claude-4.0-Sonnet (29.44% success rate).

**Validation**: Automated evaluation processes are designed to ensure rigorous testing and accurate task completion assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Misuse']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
