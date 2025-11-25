from typing import List, Optional, Dict
from pydantic import BaseModel


class BenchmarkDetails(BaseModel):
    name: str
    overview: str
    data_type: str
    domains: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    similar_benchmarks: Optional[List[str]] = None
    resources: Optional[List[str]] = None


class PurposeAndIntendedUsers(BaseModel):
    goal: str
    audience: List[str]
    tasks: List[str]
    limitations: Optional[str] = None
    out_of_scope_uses: Optional[List[str]] = None


class DataSection(BaseModel):
    source: str
    size: str
    format: str
    annotation: str


class Methodology(BaseModel):
    methods: List[str]
    metrics: List[str]
    calculation: str
    interpretation: str
    baseline_results: Optional[str] = None
    validation: str


class TargetedRisks(BaseModel):
    risk_categories: List[str]
    atlas_risks: Optional[Dict] = None
    demographic_analysis: Optional[str] = None
    harm: Optional[str] = None


class EthicalAndLegalConsiderations(BaseModel):
    privacy_and_anonymity: str
    data_licensing: str
    consent_procedures: str
    compliance_with_regulations: str


class BenchmarkCard(BaseModel):
    benchmark_details: BenchmarkDetails
    purpose_and_intended_users: PurposeAndIntendedUsers
    data: DataSection
    methodology: Methodology
    targeted_risks: TargetedRisks
    ethical_and_legal_considerations: EthicalAndLegalConsiderations