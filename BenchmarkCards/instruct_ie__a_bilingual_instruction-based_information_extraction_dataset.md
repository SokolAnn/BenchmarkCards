# INSTRUCT IE: A Bilingual Instruction-based Information Extraction Dataset

## 📊 Benchmark Details

**Name**: INSTRUCT IE: A Bilingual Instruction-based Information Extraction Dataset

**Overview**: A bilingual instruction-based information extraction (IE) dataset constructed with the KG2Instruction framework that covers 12 domains; the dataset is automatically generated from Wikidata and Wikipedia, contains hundreds of thousands of instances, and includes a manually annotated test set to improve LLM instruction-based IE capabilities and generalization.

**Data Type**: text (instruction + text input with relation triple annotations)

**Domains**:
- Astronomy
- Transportation
- Building
- Creature
- Science
- Event
- Medicine
- Organization
- Person
- Artworks
- Product
- GPE

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- CoNLL2003
- MSRA
- NYT10
- FewRel
- DuIE2.0

**Resources**:
- [Resource](https://huggingface.co/datasets/zjunlp/InstructIE)
- [Resource](https://doi.org/10.5281/zenodo.10970777)
- [Resource](https://zenodo.org/records/10970777)
- [Resource](https://w3id.org/instructie/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a bilingual (Chinese and English) instruction-based information extraction dataset covering 12 domains to improve LLMs' instruction-following IE capabilities and generalization to unseen schemas.

**Target Audience**:
- Researchers working on Large Language Models
- Semantic Web community
- Knowledge Graph researchers

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Event Extraction

**Limitations**: Firstly, we only consider versions in two languages, Chinese and English. Secondly, the dataset covers only 12 domains. Finally, despite using LLMs to supplement missing triples and NLI to filter hallucinatory triples, we still identify a certain amount of noise within the training set of INSTRUCT IE.

## 💾 Data

**Source**: Wikidata and Wikipedia (Chinese and English Wikipedia paragraphs aligned with Wikidata).

**Size**: Reported figures in the paper: 'containing 364,074 instances' (abstract); section 3.3 reports '173,670 Chinese instances and 188,406 English instances'; manually annotated test set of 2,000 instances.

**Format**: N/A

**Annotation**: Automatically generated via the KG2Instruction pipeline (KG alignment, missing-triplet supplementation with an IE LLM, and NLI-based filtering), with crowdsourced/manual annotation for the test set (approximately 1,000 Chinese instances annotated by a team of 20 specialists in two rounds; each instance annotated independently by two annotators with administrator reconciliation; translations to English refined by GPT-4).

## 🔬 Methodology

**Methods**:
- Zero-shot learning
- In-context learning
- Fine-tuning (including LoRA)
- Automated evaluation using span-based micro F1

**Metrics**:
- Micro F1 (span-based)
- F1 Score (per-domain)
- Accuracy (for dataset quality control)

**Calculation**: Micro-F1 is span-based: a relation triple is considered accurate only when the head entity, tail entity, and relation strings are precisely predicted. The paper reports per-domain F1 and an overall micro F1 (micro F1 is not a macro average across domains).

**Interpretation**: Higher micro-F1 indicates better extraction performance; micro-F1 requires exact match of head, tail, and relation strings to count as a correct triple.

**Baseline Results**: Examples from the paper: Zero-shot ChatGPT overall micro-F1: 24.01 (INSTRUCT IE-ZH) and 21.01 (INSTRUCT IE-EN). Fine-tuned best results reported: Baichuan2-13B (ZH) 72.18 overall micro-F1; LLaMA2-13B (EN) 64.97 overall micro-F1.

**Validation**: Quality control: randomly selected 500 samples per domain for manual review; reported average accuracy: 82% for INSTRUCT IE-ZH and 75% for INSTRUCT IE-EN. Test set: 2,000 instances manually annotated (two annotators per instance with administrator reconciliation) and translations refined by GPT-4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution-NonCommercial-ShareAlike 4.0 International (the paper also states availability on Zenodo under CC BY-SA 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
