# Mol-Instructions

## 📊 Benchmark Details

**Name**: Mol-Instructions

**Overview**: We introduce Mol-Instructions, a comprehensive instruction dataset designed for the biomolecular domain. Mol-Instructions encompasses three key components: molecule-oriented instructions, protein-oriented instructions, and biomolecular text instructions, aiming to improve the understanding and prediction capabilities of LLMs concerning biomolecular features and behaviors.

**Data Type**: text (instruction-input-output entries); molecular string representations (SELFIES/SMILES); protein amino acid sequences

**Domains**:
- Natural Language Processing
- Bioinformatics
- Computational Chemistry
- Structural Biology
- Drug Discovery

**Similar Benchmarks**:
- Stanford Alpaca
- Dolly-v2
- Baize
- FLAN
- InstructGPT
- ShareGPT
- COIG
- Galactica
- PCdes
- ChEBI-20
- PubChemSTM
- MoMu

**Resources**:
- [GitHub Repository](https://github.com/zjunlp/Mol-Instructions)
- [Resource](https://huggingface.co/datasets/zjunlp/Mol-Instructions)
- [Resource](https://huggingface.co/zjunlp/llama-molinst-molecule-7b)
- [Resource](https://huggingface.co/zjunlp/llama-molinst-protein-7b)
- [Resource](https://huggingface.co/zjunlp/llama-molinst-biotext-7b)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale instruction dataset tailored to biomolecular studies (molecule-oriented, protein-oriented, and biomolecular text instructions) to empower LLMs with domain-specific insights and improve their ability to decode and predict biomolecular features and behaviors.

**Target Audience**:
- Biomolecular research community
- Researchers

**Tasks**:
- Molecule Description Generation
- Molecule Generation (description-guided)
- Forward Reaction Prediction
- Retrosynthesis
- Reagent Prediction
- Property Prediction
- Protein Design
- Protein Function Prediction (Gene Ontology)
- Catalytic Activity Prediction
- Domain/Motif Prediction
- Protein Functional Description Generation
- Chemical Entity Recognition
- Chemical-Protein Interaction Extraction
- Chemical-Disease Interaction Extraction
- Multiple-choice Question Answering
- True/False Question Answering
- Open-ended Question Answering

**Limitations**: Evaluation in life sciences is complex; wet-lab validation or exhaustive expert review of outputs is impractical and quantitative metrics capture only a slice of performance. The model obtained via instruction tuning is a preliminary demonstration and its application potential for real-world, production-level tasks is limited. The scope of collected properties may be somewhat narrow and will be enriched over time.

**Out of Scope Uses**:
- Any usage of the dataset that may lead to harm or pose a detriment to society is strictly forbidden.

## 💾 Data

**Source**: Collected and derived from multiple publicly available biochemical and biomedical resources including PubChem, USPTO (reaction data), UniProtKB/Swiss-Prot and UniProtKB/TrEMBL, PubMed abstracts, BC4CHEMD, ChemProt, BC5CDR, MedMCQA, MMLU, QM9 (MoleculeNet), and others as detailed in Appendix A.2 and Table 5.

**Size**: 2,043,587 instructions (total). Breakdown provided in paper: molecule-oriented ~148.4K; protein-oriented ~505K; biomolecular text ~53K; additional per-task counts (e.g., 331,261 description-guided entries, 401,229 property prediction entries, 200,000 protein design entries, etc.) as reported in the paper.

**Format**: JSON/JSONL instruction entries with fields (instruction, input, output); molecular descriptors stored in SELFIES (converted to SMILES where needed); protein sequences as amino acid strings.

**Annotation**: Mixed process: human-written task descriptions (manually reviewed) combined with AI-assisted generation (gpt-3.5-turbo) for diversified task descriptions and Q&A pairs; information derivation from existing labeled datasets; template-based conversion of structured annotations (e.g., UniProt annotations) into textual instructions; manual quality control, filtering (e.g., MMseqs clustering at 90%), and chemical validation (RDKit/SELFIES).

## 🔬 Methodology

**Methods**:
- Instruction tuning (LoRA and full fine-tuning on LLaMA-7B and variations)
- Automated metrics-based evaluation
- Model-based baseline comparisons
- BLAST sequence alignment for protein design validation

**Metrics**:
- BLEU Score
- ROUGE
- METEOR
- Mean Absolute Error (MAE)
- Exact Match
- Levenshtein Distance
- RDKit fingerprint similarity (RDKit FTS)
- MACCS fingerprint similarity (MACCS FTS)
- Morgan fingerprint similarity (Morgan FTS)
- Validity (RDKit)

**Calculation**: For molecule generation: validate generated strings as molecules using RDKit, compute exact match with reference, and compute molecular similarity via RDKit/MACCS/Morgan fingerprints, Levenshtein distance, and BLEU. For molecular property prediction: compute MAE for continuous values. For protein functional description generation: use ROUGE to quantify generated description quality. For NLP tasks (entity/relation/QA): use standard NLP evaluation metrics as applicable.

**Interpretation**: Higher BLEU/ROUGE/METEOR/fingerprint similarity/exact match/validity indicate better performance; lower MAE and lower Levenshtein distance indicate better performance. Quantitative metrics capture partial aspects of performance and do not replace expert or experimental validation in biomolecular contexts.

**Baseline Results**: See paper tables for detailed baseline numbers. Example: Table 3 (Property Prediction MAE) reports ALPACA 322.109, BAIZE 261.343, LLAMA 5.553, VICUNA 860.051, GALACTICA 0.568, OURS (Mol-Instructions tuned) 0.5550.013. Table 4 provides extensive per-task metric comparisons (Exact match, BLEU, Levenshtein, RDKit FTS, MACCS FTS, Morgan FTS, Validity) across baselines including ALPACA, BAIZE, CHATGLM, LLAMA, VICUNA, GALACTICA, TEXT+CHEM T5, MolT5, and OURS.

**Validation**: Dataset partitioned into training, validation, and testing subsets. Training and validation used for instruction tuning; test set used for evaluation. For each distinct task, nearly 1k samples allocated as test set; remaining samples split training/validation at an 8:2 ratio. Protein redundancy mitigated via MMseqs clustering at 90% similarity and representative selection. Quality control steps include SMILES filtering, conversion to SELFIES, and chemical/protein validation procedures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Misuse
- Ethical concerns
- Legal and licensing

**Atlas Risks**:
- **Misuse**: Dangerous use, Improper usage
- **Data Laws**: Data usage restrictions
- **Legal Compliance**: Model usage rights restrictions
- **Governance**: Incomplete usage definition

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for malicious actors to harness the combined capabilities of LLMs and biomolecular data to generate harmful substances (e.g., biochemical weapons or illicit drugs) as explicitly noted in the paper.', 'Risk of societal harm if dataset/tools are used irresponsibly.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors state the dataset does not contain any personally identifiable or privacy-sensitive information; rigorous quality control and security checks were implemented to prevent harmful or malicious content.

**Data Licensing**: Mol-Instructions is released under CC BY-NC-SA 4.0 as stated in the paper (the paper also discusses compliance with CC BY 4.0 in Appendix A.3). Component data sources use various licenses as detailed in Table 5 (examples: PubChem/public domain, DrugBank/CC BY-NC 4.0, ChEBI/CC BY 4.0, etc.).

**Consent Procedures**: Biomolecular data were sourced from publicly available datasets and the authors state that necessary permissions and licenses for third-party content were obtained (detailed in Appendix A.2).

**Compliance With Regulations**: Authors state that data sources and data rights were scrutinized to ensure licenses permit the research and usage pursued; necessary permissions and licenses were obtained and are detailed in Appendix A.2.
