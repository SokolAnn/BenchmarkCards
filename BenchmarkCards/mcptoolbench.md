# MCPToolBench++

## 📊 Benchmark Details

**Name**: MCPToolBench++

**Overview**: MCPToolBench++ is a large-scale, multi-domain AI Agent tool use benchmark designed to evaluate LLM and AI Agents' abilities to use Model Context Protocol (MCP) tools effectively. It consists of 1.5K question-answer pairs covering various domains and is built upon a marketplace of over 4k MCP servers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance
- Web Services
- File Systems
- Maps

**Languages**:
- English
- Chinese
- French
- Russian

**Similar Benchmarks**:
- GAIA
- Berkeley Function Calling Leaderboard (BFCL)
- ComplexFuncBench

**Resources**:
- [GitHub Repository](https://github.com/mcp-tool-bench/MCPToolBenchPP)
- [Resource](https://huggingface.co/datasets/MCPToolBench/MCPToolBenchPP)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLMs and AI agents in using MCP tools across various domains and tasks.

**Target Audience**:
- ML Researchers
- AI Developers
- Industry Practitioners

**Tasks**:
- Tool usage evaluation
- Multi-step tool calling
- Function calling capabilities

**Limitations**: N/A

## 💾 Data

**Source**: MCP servers gathered from open MCP marketplaces

**Size**: 1,500 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated from MCP tool schemas and user query templates

## 🔬 Methodology

**Methods**:
- Automated metrics
- Tool call evaluation
- AST (Abstract Syntax Tree) evaluation

**Metrics**:
- AST Accuracy
- Pass@K Accuracy

**Calculation**: AST Accuracy is evaluated by comparing predicted outputs with ground truth labels for function and parameter matches. Pass@K measures the correctness of the tool call execution.

**Interpretation**: Higher AST and Pass@K scores indicate better performance in selecting and executing tool calls.

**Baseline Results**: N/A

**Validation**: The evaluation is validated across different task domains and various LLM models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
