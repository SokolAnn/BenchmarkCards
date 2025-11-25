# STORY WARS

## 📊 Benchmark Details

**Name**: STORY WARS

**Overview**: We introduce STORY WARS, a new dataset of over 40,000 collaborative stories written by 9,400 different authors from an online platform. We design 12 task types, comprising 7 understanding and 5 generation task types, on STORY WARS, deriving 101 diverse story-related tasks in total as a multi-task benchmark covering all fully-supervised, few-shot, and zero-shot scenarios.

**Data Type**: text (collaborative multi-turn stories; chapter-level text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ROCStories
- WritingPrompts
- Storium
- roleplayerguild
- LOT
- BIG-bench

**Resources**:
- [GitHub Repository](https://github.com/ylndu/storywars)
- [Resource](https://archive.md/sAOOq)
- [Resource](https://beta.openai.com/docs/api-reference/moderations)
- [GitHub Repository](https://github.com/unitaryai/detoxify)

## 🎯 Purpose and Intended Users

**Goal**: To provide a novel collaborative story dataset (STORY WARS) and a multitask benchmark of 12 task types (101 tasks) to test LLMs' understanding and generation abilities in collaborative storytelling across fully-supervised, few-shot, and zero-shot scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Genre Classification
- Authorship Attribution
- Authorship Verification
- Connectivity Inference
- Temporal Inference
- Story Scoring (Regression)
- Story Segmentation
- Next Chapter Generation
- Conditional Story Generation
- Chapter Infill (Chapter Inﬁlling)
- Global Infill (Global Inﬁlling)
- Temporal Ordering

**Limitations**: Fine-tuning on a new task may cause catastrophic forgetting and loss of multitask generalization; single-task fine-tuning requires multiple models to be served simultaneously, increasing computational costs; automatic evaluation metrics such as BERTScore may not be comprehensive enough for evaluating highly creative collaborative story generation.

## 💾 Data

**Source**: Scraped and parsed from story-wars.net (an online collaborative storytelling platform); initial 76k stories filtered to English via FastText and cleaned using GPT-2 perplexity filtering; harmful content identified/removed using OpenAI Content Moderation API and Detoxify; URLs, email addresses, and phone numbers replaced with tokens.

**Size**: 40,135 stories; average 367 words per story; 9,494 authors

**Format**: N/A

**Annotation**: Labels and annotations are derived from platform metadata (author IDs, likes, stars, genres). Story ratings (likes/stars) normalized to a 0-10 range and converted to strings. No manual crowdsourced annotation is described.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Macro-average evaluation across tasks within each task type
- Data splits for fully-supervised, few-shot, and zero-shot scenarios (training/dev/test where applicable)

**Metrics**:
- F1 Score
- Spearman correlation coefficient
- Boundary Similarity
- BERTScore
- Macro-average

**Calculation**: For each task, the chosen metric is computed; metrics for all tasks within a task type are macro-averaged to produce task-type scores; overall understanding, generation, and overall performance are computed as the macro-average across corresponding task types. Story ratings are normalized to 0-10 and converted to strings.

**Interpretation**: Higher metric scores indicate better model performance. BERTScore was chosen for generation tasks because it has been shown to correlate better with human evaluation at the story-level and system-level. Macro-averaging across tasks within a task type enables comparison across different task types.

**Baseline Results**: INSTRUCTSTORY outperforms the single-task fine-tuned T5 baseline by 1.53 points on average across all tasks. For understanding tasks INSTRUCTSTORY outperforms T5 by 2.06 points; for generation tasks INSTRUCTSTORY outperforms T5 by 0.77 points. Few-shot: INSTRUCTSTORY achieves 61.44 average vs FLAN-T5 59.45. Zero-shot: INSTRUCTSTORY achieves 60.00 average vs FLAN-T5 47.79 and T5 32.09.

**Validation**: For fully-supervised and few-shot tasks data are split into training, dev, and test sets. For zero-shot tasks all data are used as test sets by sampling. The fully-supervised, few-shot, and zero-shot datasets are disjoint to prevent data leakage. Best checkpoints for fully-supervised tasks are selected based on dev set performance; early stopping is used for few-shot.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Value Alignment**: Toxic output, Harmful output

**Demographic Analysis**: N/A

**Potential Harm**: ['Perpetuating stereotypes and societal biases', 'Exposing personal user information', 'Toxic or harmful content in generated stories']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Replaced all URLs, email addresses, and phone numbers with tokens <URL>, <EMAIL>, and <PHONE>. Removed potentially harmful content (toxicity, obscenity/sexual content, threats, insults, identity hate, self-harm) using OpenAI Content Moderation API and the Detoxify toxicity classifier.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
