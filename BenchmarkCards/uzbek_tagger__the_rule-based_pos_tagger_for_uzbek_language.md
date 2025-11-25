# Uzbek Tagger: The rule-based POS tagger for Uzbek language

## 📊 Benchmark Details

**Name**: Uzbek Tagger: The rule-based POS tagger for Uzbek language

**Overview**: This paper presents a part-of-speech (POS) annotated dataset and a rule-based POS-tagger tool (UzbekTagger) for the low-resource Uzbek language. The dataset includes 12 POS tags and is balanced over 23 distinct fields. The tagger is based on stemming with affix/suffix stripping and a database of stem forms and was evaluated on the annotated dataset, reporting high accuracy (about 90% overall).

**Data Type**: POS-annotated text (sentences with POS tags)

**Domains**:
- Natural Language Processing

**Languages**:
- Uzbek

**Similar Benchmarks**:
- Universal Dependencies

**Resources**:
- [Resource](https://universaldependencies.org/u/pos/)
- [Resource](https://pypi.org/project/UzbekTagger)
- [GitHub Repository](https://github.com/apertium/apertium-uzb)
- [Resource](https://kitob.uz)
- [GitHub Repository](https://github.com/MaksudSharipov/UzbekTokenizer)

## 🎯 Purpose and Intended Users

**Goal**: To provide a publicly available POS-annotated dataset for Uzbek and an open rule-based POS-tagger tool to support NLP tasks for the Uzbek language (e.g., language modeling, machine translation, text-to-speech synthesis).

**Target Audience**:
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Part-of-Speech Tagging
- Language Modeling
- Machine Translation
- Text-to-Speech Synthesis

**Limitations**: Limited dataset size (1,581 sentences, 23,482 words). Terminology coverage in the tagger's stems dictionary is insufficient for some fields, leading to lower accuracy in fields such as Agriculture, Mother tongue, and Law.

## 💾 Data

**Source**: Manually annotated corpus constructed from raw texts obtained from the Republican Youth E-Library (kitob.uz); lemma dictionary and stem resources sourced from prior work (Sharipov & Sobirov, 2022) and the Apertium monolingual package for Uzbek. A dictionary of more than 80,000 Uzbek words with POS tags was created in XML format as part of the project.

**Size**: 1,581 sentences; 23,482 words

**Format**: N/A

**Annotation**: Manual annotation by four expert-level Uzbek linguists over six months; each sentence annotated by at least two annotators; conflicts resolved by group discussion. POS-tagging guidelines of Universal Dependencies (version 2) were followed.

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy) comparing tagger output to manual annotations

**Metrics**:
- Accuracy

**Calculation**: Mistakes were counted by comparing the tagger output to the manually annotated sentence. If the same word appears wrongly tagged more than once, it was considered as one mistake. Total mistakes per category were calculated and reported; accuracy per category is reported in Table 3.

**Interpretation**: Higher Accuracy indicates better tagging performance. The authors report about 90% overall accuracy and per-category accuracies (reported per Table 3); lower accuracy in a category indicates the need to enrich the tagger's stems/terminology for that field.

**Validation**: Validation performed by evaluating the tagger on the manually annotated corpus (23 categories). The corpus was annotated by multiple expert annotators (each sentence annotated by at least two) and disagreements were resolved via group discussion.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
