# PIPPA (Personal Interaction Pairs between People and AI)

## 📊 Benchmark Details

**Name**: PIPPA (Personal Interaction Pairs between People and AI)

**Overview**: PIPPA is a large-scale dataset comprising approximately 1 million messages exchanged between humans and dialogue agents across nearly 26,000 unique conversations. It aims to support future research and development in the fine-tuning of models to generate persona-driven, contextually rich conversations.

**Data Type**: dialogue sessions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LIGHT
- MultiLIGHT
- FIREBALL
- DailyDialog
- Cornell Movie Dialogs Corpus

**Resources**:
- [Resource](https://huggingface.co/datasets/PygmalionAI/PIPPA)
- [GitHub Repository](https://github.com/0x000011b/characterai-dumper)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rich resource for researchers and AI developers to explore and refine conversational AI systems in the context of role-play scenarios.

**Target Audience**:
- AI Researchers
- AI Developers
- Natural Language Processing Specialists

**Tasks**:
- Role-Play Simulation
- Conversational Model Fine-Tuning

**Limitations**: The dataset is primarily tailored for supervised fine-tuning applications. Any endeavor to apply the PIPPA dataset to unsupervised fine-tuning objectives may necessitate a comprehensive overhaul of the dataset’s structure and content presentation.

## 💾 Data

**Source**: Community-driven crowdsourcing effort through Character.AI interactions.

**Size**: 1,049,015 dialogue sessions

**Format**: JSONL

**Annotation**: Crowdsourced with user submission process to ensure only data from users who explicitly consented is included.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Statistical analysis

**Metrics**:
- Conversation length
- Message verbosity

**Calculation**: Examined the number of turns in conversations and message lengths to gauge dataset characteristics.

**Interpretation**: Conversations exhibit diverse lengths with a median of 10 turns and a mean of 40.41 turns, reflecting varied user engagement.

**Validation**: The dataset has not undergone exhaustive validation, which implies potential variations in quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Ethics

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The dataset may contain instances of unsuitable or inappropriate material due to the community-driven curation process.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive personal information has been redacted to the best of our ability, however, residual instances might persist due to human oversight.

**Data Licensing**: Not Applicable

**Consent Procedures**: Users were allowed to opt out of including their conversations in the public release.

**Compliance With Regulations**: Not Applicable
