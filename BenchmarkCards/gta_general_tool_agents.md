# GTA (General Tool Agents)

## 📊 Benchmark Details

**Name**: GTA (General Tool Agents)

**Overview**: GTA is a benchmark for evaluating the tool-use capabilities of LLMs through human-designed queries with real-world objectives, requiring implicit tool use, supported by an evaluation platform with executable tools and multimodal inputs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GAIA

**Resources**:
- [GitHub Repository](https://github.com/open-compass/GTA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the general tool-use ability of LLMs in real-world scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Use Evaluation

**Limitations**: Human-designed queries limit language diversity, as all queries are in English.

## 💾 Data

**Source**: Human-designed queries and images sourced from various platforms and personal annotations.

**Size**: 229 queries, 252 images

**Format**: JSON

**Annotation**: Manual verification and annotation by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Instruction-following accuracy (InstAcc)
- Tool selection accuracy (ToolAcc)
- Argument accuracy (ArgAcc)
- Summary accuracy (SummAcc)
- Answer accuracy (AnsAcc)

**Calculation**: Metrics are calculated based on the evaluation of the LLMs' outputs against a ground truth tool chain.

**Interpretation**: High scores in metrics indicate better tool-use capabilities and reasoning abilities of the LLMs.

**Validation**: The benchmark was validated through systematic testing of LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Potential Harm**: ['Potential copyright concerns related to image data collection.', 'Privacy concerns involving the presence of individuals in images.', 'Risk of generating harmful information due to LLM hallucinations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the Apache License.

**Consent Procedures**: Images used are from approved sources, ensuring proper documentation.

**Compliance With Regulations**: Not Applicable
