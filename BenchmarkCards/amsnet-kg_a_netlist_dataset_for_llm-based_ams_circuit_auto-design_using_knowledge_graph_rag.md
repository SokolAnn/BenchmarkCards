# AMSnet-KG (A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using Knowledge Graph RAG)

## 📊 Benchmark Details

**Name**: AMSnet-KG (A Netlist Dataset for LLM-based AMS Circuit Auto-Design Using Knowledge Graph RAG)

**Overview**: AMSnet-KG is a comprehensive dataset that encompasses various AMS circuit schematics and netlists, constructed using detailed annotations on functional and performance characteristics. It facilitates the automated design of AMS circuits using large language models by providing structured knowledge for effective retrieval and circuit generation.

**Data Type**: circuit schematics and netlists

**Domains**:
- Electrical Engineering
- Electronic Design Automation

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2411.13560)

## 🎯 Purpose and Intended Users

**Goal**: To enable the automated design of analog and mixed-signal circuits through structured data and knowledge retrieval.

**Target Audience**:
- Electrical Engineers
- EDA Researchers
- Circuit Designers

**Tasks**:
- Circuit Design
- Netlist Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is derived from textbooks and academic papers containing AMS circuit schematics and descriptions, with data collected and structured into the proposed format.

**Size**: 894 circuits

**Format**: JSON

**Annotation**: Annotated with details on circuit functionalities, performance characteristics, and a knowledge graph structure.

## 🔬 Methodology

**Methods**:
- Data Collection
- Knowledge Graph Construction
- Automated Circuit Design Framework

**Metrics**:
- Success Rate of Design Generation
- Accuracy of Circuit Specifications

**Calculation**: The performance metrics were calculated based on the successful generation and compliance of circuit designs with specified performance characteristics.

**Interpretation**: A circuit is considered successful if it meets or exceeds the designated performance specifications and constraints outlined during the design phase.

**Validation**: The dataset is validated through multiple case studies demonstrating its effective application in generating operational amplifier and comparator designs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be open-sourced upon the publication of this paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
