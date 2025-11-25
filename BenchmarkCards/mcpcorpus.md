# MCPCorpus

## 📊 Benchmark Details

**Name**: MCPCorpus

**Overview**: MCPCorpus is a large-scale dataset containing around 14K MCP servers and 300 MCP clients, annotated with 20+ normalized attributes capturing their identity, interface configuration, GitHub activity, and metadata, providing a comprehensive view of the real-world MCP ecosystem.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Snakinya/MCPCorpus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for analyzing the Model Context Protocol (MCP) ecosystem, enabling studies of adoption trends, ecosystem health, and implementation diversity.

**Target Audience**:
- ML Researchers
- Security Analysts
- Software Developers

**Tasks**:
- Ecosystem Analysis
- Security Auditing
- Tool Integration

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from MCP.so and GitHub repositories, focusing on metadata-rich, actively maintained platforms.

**Size**: 14,175 artifacts

**Format**: JSONL

**Annotation**: Static inspection of public repositories.

## 🔬 Methodology

**Methods**:
- Automated data collection
- Registry crawling
- Metadata normalization

**Metrics**:
- Artifact completeness
- Metadata richness

**Calculation**: Each artifact is assessed based on the completeness of its metadata and its activity on GitHub.

**Interpretation**: Higher artifact completeness and metadata richness indicate a more useful dataset for understanding the MCP ecosystem.

**Validation**: The dataset was validated through comparison with existing MCP resource archives for consistency and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
