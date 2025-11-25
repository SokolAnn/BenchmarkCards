# SemEval 2022 Task 12: Symlink — Linking Mathematical Symbols to their Descriptions

## 📊 Benchmark Details

**Name**: SemEval 2022 Task 12: Symlink — Linking Mathematical Symbols to their Descriptions

**Overview**: Symlink is a SemEval 2022 shared task for extracting mathematical symbols and their descriptions from LaTeX source of scientific documents. The paper describes the task, the creation of a large-scale annotated dataset for English scientific literature, the evaluation methodology, and analysis of participant system results. The data used in this task is publicly accessible at https://github.com/nlp-uoregon/symlink.

**Data Type**: text (LaTeX source paragraphs with embedded mathematical formulae; annotated entity spans and relation pairs; provided as JSON)

**Domains**:
- Mathematics
- Physics
- Biology
- Economics
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- MathAlign
- DEFT

**Resources**:
- [GitHub Repository](https://github.com/nlp-uoregon/symlink)
- [Resource](https://arxiv.org/abs/2202.09695)

## 🎯 Purpose and Intended Users

**Goal**: The ultimate goal of Symlink shared task is to extract pairs of mathematical symbols and descriptions from scientific documents (a combination of entity recognition and entity linking/relation extraction) using LaTeX source.

**Target Audience**:
- Scientific knowledge extraction community
- Automated knowledge base construction community

**Tasks**:
- Named Entity Recognition
- Relation Extraction

**Limitations**: The dataset is challenging due to the complexity of LaTeX source and domain differences. The paper notes that some unique characteristics of the dataset (such as LaTeX syntax and hierarchical structure of formulae) have not been investigated. The subtasks (NER and RE) are hard to separate due to their constraints.

## 💾 Data

**Source**: LaTeX sources of arXiv.org preprints (only articles under the CC BY license were selected); five subjects annotated: mathematics, physics, biology, economics, and computer science.

**Size**: 102 documents; 3,690 paragraphs; 29,121 sentences; 595K tokens; 31,471 entities; 20,653 relation instances

**Format**: JSON (each paragraph stored as a JSON object with id, topic, original LaTeX source, entities, and relations)

**Annotation**: Manual annotation by 10 annotators recruited via Upwork with demonstrated experience in scientific documents (each subject annotated by two annotators); co-annotation with discussion and consolidation to resolve conflicts; average Cohen's Kappa inter-annotator agreement: 0.79.

## 🔬 Methodology

**Methods**:
- Automated metrics for evaluation
- Named Entity Recognition evaluation using entity-based partial/type metric from SemEval 2013 Task 9.1
- Relation Extraction evaluation using Precision, Recall, and F1 Score

**Metrics**:
- Precision
- Recall
- F1 Score
- Entity-based partial/type (SemEval 2013 Task 9.1)

**Calculation**: For Named Entity Recognition, entity-based partial/type metric from SemEval 2013 Task 9.1 was used. For Relation Extraction, standard Precision, Recall, and F1-score were used. A predicted relation is correct only if the prediction label strictly matches the gold standard.

**Interpretation**: N/A

**Baseline Results**: Top-performing submitted system (JBNU-CCLab, ensemble variant) reported Entity F1 (partial) = 47.61, Entity F1 (type) = 47.70; Relation Precision = 38.20, Recall = 36.23, F1-score = 37.19. During the evaluation period 59 submissions were made and 37 submissions passed validation and were scored.

**Validation**: Annotators resolved conflicts to produce a consolidated gold standard. Inter-annotator agreement averaged Cohen's Kappa = 0.79. Submissions were validated on CodaLab; 37 submissions passed validation and were scored.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Selected arXiv articles under the CC BY license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
