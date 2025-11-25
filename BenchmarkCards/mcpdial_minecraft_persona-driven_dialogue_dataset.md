# MCPDial (Minecraft Persona-driven Dialogue dataset)

## 📊 Benchmark Details

**Name**: MCPDial (Minecraft Persona-driven Dialogue dataset)

**Overview**: MCPDial is a persona-driven dialogue dataset for Minecraft that includes complex human-written player and NPC personas and conversations, incorporating natural language utterances as well as canonical function calls representing game APIs.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Gaming

**Languages**:
- English

**Similar Benchmarks**:
- PersonaChat
- LIGHT

**Resources**:
- [GitHub Repository](https://github.com/salavi/MCPDial-A-Minecraft-Persona-driven-Dialogue-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a valuable resource for training and evaluating conversational agents within the Minecraft domain.

**Target Audience**:
- ML Researchers
- Game Developers
- Dialogue System Researchers

**Tasks**:
- Dialogue Generation
- Conversational Agent Training

**Limitations**: One limitation of our dataset is the relatively small number (49) of human-written conversations, which may impact the diversity and coverage of various conversation topics.

## 💾 Data

**Source**: Expert-written conversations and LLM augmentation.

**Size**: 250 NPC personas, 750 player personas, 49 human-written conversations and 220 automatically-generated conversations.

**Format**: JSON

**Annotation**: Expert-generated and LLM-generated with a review process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based conversation generation

**Metrics**:
- Fluency
- Persona consistency
- Function call accuracy

**Calculation**: Average ratings from expert annotators on a scale of 1 to 5.

**Interpretation**: Higher scores indicate better quality that aligns with the characteristics of the provided personas and appropriate function calls.

**Validation**: Human evaluation confirmed high-quality conversations in terms of various criteria.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation

**Potential Harm**: ['Potential generation of biased or offensive content.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors ensured the absence of sensitive information and offensive content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
