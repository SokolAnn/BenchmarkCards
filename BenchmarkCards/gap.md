<div align="center">

# GAP

<small><em>Original: Q18-1042.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

<p>
<img src="https://img.shields.io/badge/naturallanguageunderstanding-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="natural language understanding" style="margin-right:5px;">
<img src="https://img.shields.io/badge/coreferenceresolution-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="coreference resolution" style="margin-right:5px;">
</p>

</div>

## Table of Contents

- [📊 Benchmark Details](#-benchmark-details)
- [🎯 Purpose and Intended Users](#-purpose-and-intended-users)
- [💾 Data](#-data)
- [🔬 Methodology](#-methodology)
- [⚠️ Targeted Risks](#️-targeted-risks)
- [🔒 Ethical and Legal Considerations](#-ethical-and-legal-considerations)

<hr>

## 📊 Benchmark Details

<table>
<tr><td width="20%" align="center"><strong>Name</strong></td><td>
GAP
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
A gender-balanced labeled corpus of 8,908 ambiguous pronoun–name pairs sampled to provide diverse coverage of challenges posed by real-world text.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
corpus
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
<li>natural language understanding</li>
<li>coreference resolution</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>English</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
<ul>
<li>Winograd schemas</li>
<li>OntoNotes</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="http://goo.gl/language/gap-coreference">Resource</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To address gender bias in existing coreference corpora and provide a benchmark for evaluating coreference resolution systems on ambiguous gendered pronouns.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>researchers</li>
<li>developers of NLP systems</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>coreference resolution</li>
<li>gender bias analysis</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
Only contains ambiguous pronouns from Wikipedia.
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
<ul>
<li>non-ambiguous pronouns</li>
<li>data not reflecting gender dynamics</li>
</ul>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
Wikipedia
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
8,908 ambiguous pronoun-name pairs
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
labeled corpus
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
Human-annotated with multiple labels for coreference resolution.
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>coreference resolution analysis</li>
<li>gender bias detection</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>F1 score</li>
<li>Bias</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
F1 score calculated overall and by gender; Bias defined as the ratio of feminine to masculine F1 scores.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Lower F1 scores and high bias indicate systems favoring masculine pronouns.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
Best scoring baseline achieved 66.9% F1.
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Inter-annotator agreement was measured using Fleiss' kappa statistics.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>gender bias</li>
<li>inequitable representation</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias</li>
<li><strong>Societal Impact:</strong> Impact on affected communities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
The corpus aims for a balanced 1:1 gender ratio.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Potential reinforcement of gender stereotypes if biases are not addressed.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Not applicable as the data is extracted from publicly available Wikipedia articles.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Consent Procedures</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Compliance With Regulations</strong></td><td>
Not Applicable
</td></tr>
</table>

<hr>

<div align="center">
<p><em>This benchmark card was automatically generated.</em></p>
</div>