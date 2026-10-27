# Building a Computational Vaccine Institution in HK/GBA

*2026-10-27 · Thomas Yuan*

This document lays out the full plan for building a computational vaccine design and de-risking institution anchored in Hong Kong, with a Shenzhen commercial node added at Phase 2. The founding IP — barrier metric framework, VC2 deletion design methodology, reversion analysis pipeline — is Thomas's independently generated work, unencumbered by HKU or Haibo.

---

## 宏观 — The Big Picture

Live-attenuated vaccines (LAVs) are among the most effective human interventions against viral disease: the oral poliovirus vaccine (OPV), yellow fever 17D, and varicella-zoster virus (Oka strain) have collectively prevented hundreds of millions of infections. Yet every LAV carries an inherent tension — the attenuating mutations that reduce pathogenicity are subject to reversion under evolutionary pressure, and the quantitative boundary between safe attenuation and reversion risk has never been formally specified.

The canonical failure case is OPV. Circulating vaccine-derived polioviruses (cVDPVs) emerged in under-immunized populations as the Sabin strains accumulated reversion mutations, causing paralytic outbreaks across sub-Saharan Africa and South Asia; the number of reported cVDPV outbreaks more than tripled between 2017–2018 and 2018–2019, with 86% caused by type 2 reversion [Jorba et al. 2019]. The mechanistic root is well-established: specific attenuating substitutions and recombination events revert to neurovirulence when the vaccine strain circulates long enough in an under-vaccinated population [Pliaka et al. 2012]. The global response — a novel nOPV2 stabilized against reversion, supplemental immunization campaigns, and transmission modeling to guide response timing [Sun et al. 2024] — required decades of surveillance and is still not complete. The OPV case is not an outlier; it is the template for what happens when reversion risk is managed retrospectively rather than quantified prospectively.

**The disease burden that justifies a new approach.** Herpesviruses are among the most prevalent human pathogens, and the existing vaccine pipeline has repeatedly failed. HSV-2 infects an estimated 536 million people aged 15–49 globally, with 23.6 million new infections per year [Looker et al. 2008]. Despite this burden, no licensed HSV vaccine of any kind exists; recent subunit and live-attenuated candidates have failed in Phase 2/3 trials on clinical endpoints, in part because the immune correlates of protection remain undefined and no quantitative reversion safety standard exists for live designs [Stanfield & Kousoulas et al. 2021]. HCMV infects approximately 60% of adults in developed countries and over 90% in developing countries and is the leading infectious cause of congenital disability worldwide [Griffiths & Reeves 2021]; all vaccine candidates have failed clinical endpoints, and the field's consensus is that correlates of protection are the critical missing input for rational vaccine design [Itell et al. 2017]. In both cases the barrier is not immunological ignorance — it is the absence of quantitative frameworks linking genomic design to safety and efficacy outcomes.

**The regulatory gap.** No institution currently provides a quantitative, reproducible, genome-level reversion probability framework as a regulatory or design product. Vaccine developers who wish to argue live-attenuated safety in an IND dossier must rely on passage experiments, animal neurovirulence models, and precedent analogies — not on a principled probabilistic model of reversion risk tied to the specific deletion coordinates in their construct. The barrier metric framework this institution is built on addresses that gap directly: it converts a genomic design decision into a quantitative safety prediction that is verifiable, reproducible, and citable.

**Why HK/GBA, and why now.** The Greater Bay Area offers a regulatory corridor unavailable elsewhere. Hong Kong provides legal clarity, IP enforcement under common law, and access to HKEX-listed biotech financing. Shenzhen provides BSL-2/3 wet-lab infrastructure, NMPA-track development capability, and manufacturing at scale without the regulatory overhead of EU or US trials for Phase 1/2 work. The combination of large publicly accessible genome databases (NCBI GenBank: >5 million viral sequences), modern AI/ML-assisted pipeline infrastructure, and mounting regulatory pressure for quantitative safety data makes a computational-first approach not merely feasible but necessary for the next generation of LAV development.

---

## Brand Identity

**English name:** Meridian Institute  
**Chinese name:** 楓旭研究院 (Fengxu Institute)  
**Email:** inquiry@meridianinstitute.org  
**Legal structure:** HK private limited company (HK Ltd.) + institute brand  
**Model:** Arc Institute register — independent identity, research-first, no commercial language  

The name "Meridian" was selected for its register: universal, precision-scientific, no geographic friction globally or in HK/GBA. "Meridian" connotes a line that runs through all latitudes — positioning without planting a flag. The Chinese name shares the concept (maple + rising sun) without being a transliteration.

---

## What This Institution Is

A computational vaccine design studio: a small, IP-generating research entity whose output is validated quantitative safety and efficacy frameworks, not drug approvals. It sits between academia (which produces methods but rarely validates them against real constructs) and biotech (which runs expensive wet-lab programs before the design is de-risked). The institution's commercial proposition is that its frameworks reduce the cost and failure rate of live-attenuated vaccine development by answering the hardest questions — reversion risk, barrier geometry, correlates of protection — computationally, before any animal work starts.

This is not a CRO, not a lab, and not a traditional biotech. It does not manufacture or run clinical trials. It generates IP, licenses it, and consults on design decisions. Revenue comes from three sources: research grants, IP licensing fees from vaccine developers who use the barrier metric framework in their regulatory dossiers, and contract de-risking engagements for specific constructs.

---

## Legal Setup

**Most cost-effective route: DIY via cr.gov.hk e-Registry. No lawyer needed. Total cost under HK$3,500.**

**Step 1: Incorporate a HK private limited company (1–2 business days, ~HK$1,720)**

Go to cr.gov.hk → e-Registry → Incorporate a Local Company. What you need before you start:

1. **Company name** — check availability on the Registry name search first (bilingual, English + Chinese both issued on the certificate).
2. **Registered HK address** — required by law. Use a virtual office provider if you have no HK office. Cheapest credible options: Compass Offices, Regus HK, or local providers in Kwun Tong — ~HK$800–1,500/year for mail handling only.
3. **Director and shareholder** — Thomas as sole director and sole shareholder (1 share, HK$1 paid up).
4. **Articles of Association** — use the standard Table A articles provided by the Registry.

Filing fee: HK$1,720 online. Certificate in 1–2 business days. Total at incorporation: HK$1,720 + virtual office year 1 (~HK$1,000–1,500) = under HK$3,500.

**Step 2: IP assignment agreement (draft within 30 days of incorporation)**

A one-to-two page document assigning all rights to the barrier metric framework, VC2 deletion design methodology, multi-seed k-mer walk reversion analysis pipeline, and all derivative works to the HK company.

**Step 3: Bank account and basic compliance**

Open a HK business bank account (HSBC, Hang Seng, or ZA Bank). Annual filing: profits tax return + annual return (~HK$105/year).

**Step 4: Check one edge case with HKU**

Confirm in writing with HKU's TTO that no HKU resources were involved in VC2 work. One-paragraph email to TTO asking for a non-assertion confirmation.

**Total cost to be legally operational:** approximately HK$2,000–5,000 all-in.

---

## Phased Roadmap

| Phase | Timeline | Key milestones | Gate to next phase |
|-------|----------|----------------|--------------------| 
| 0 — Legal foundation | Now – 3 months | Incorporate HK company; execute IP assignment; TTO non-assertion email; open bank account | Company exists, IP assigned in writing |
| 1 — Proof of concept | Months 3–18 | Publish reversion barrier paper; apply for ITF grant; present at one international conference; first Haibo licensing conversation | Peer-reviewed publication accepted or in revision |
| 2 — First external funding | Months 12–36 | Receive first grant (ITF or HMRF); hire first research scientist; expand to second construct or virus | Active grant + one signed license |
| 3 — Shenzhen node | Months 30–48 | Register Shenzhen subsidiary; NMPA-track partnership with Chinese vaccine developer | Shenzhen entity operational |
| 4 — Institution scale | Year 4–7 | 4–8 person team; multiple licensing contracts; faculty affiliation formalized | Self-sustaining on grants + licensing |

**Non-negotiable near-term deadlines:**
- Haibo PCT filing deadline: **2027-06-24** — inventorship must be correct before this date
- Reversion barrier paper: target submission within 6 months of PhD completion
- HKU PhD completion: do not let institution-building delay conversion or thesis

---

## Commercial Strategy: Zhifei Anchor

**Target:** Zhifei Biological Products (智飞生物, SZ:300122) — China's largest independent vaccine distributor (>RMB 20B revenue), expanding into domestic R&D. First anchor client for the reversion risk framework.

**Value proposition:** Quantitative genome-level reversion risk assessment for regulatory dossiers (IND/NDA), delivered computationally at a fraction of wet-lab equivalents. No competing standardized product exists.

**Upstream positioning:** Become the reversion risk clearinghouse upstream of all major LAV developers:
- Zhifei anchor (China) → India (Serum Institute + Bharat Biotech) → Global

---

## Wet-Lab Validation Partner: Haibo (Shenzhen)

Shenzhen Haibo Biotechnology (深圳海渤生物技术有限公司) is the institution's wet-lab validation partner. HB01 — the ICP0/RL2 deletion construct — is already in their hands.

The collaboration agreement (one page) covers: scope, authorship, IP ownership, licensing terms (HK$200–500K range for barrier metric framework licensing), and disclosure of the family relationship as competing interest.

---

## Virtual Agent Infrastructure

Six standing agents:

| Agent | What it executes | Output |
|-------|-----------------|--------|
| Sequence surveillance | Weekly GenBank scan for new HSV sequences; auto-runs barrier metric on each deposit | Digest: any genome below VC2 RVx201 threshold flagged |
| Literature watch | bioRxiv + PubMed for relevant keywords | Weekly digest ranked by relevance |
| Patent watch | CN and PCT filings in herpesviridae + LAV class | Monthly alert on overlapping filings |
| Computation (Biomni) | All analysis pipelines; QC on wet-lab data | Logged outputs with MD5s; Zenodo DOI on each release |
| Atlas curation | Extracts structured data from phenotype papers | Curated entries pending Thomas review |
| Grant radar | Tracks ITF, HMRF, InnoHK, NIH R21 cycles | Deadline calendar; draft sections queued for review |

**Governance principle:** agents execute; Thomas decides. No agent publishes, files IP, or writes to the knowledge base without a human review gate.

---

## References

- **Bernstein et al. 2018** — Stanfield B et al. *Vaccine* 37(1):61–69. PMID 30471955.
- **Griffiths & Reeves 2021** — *Nat Rev Microbiol* 19(12):759–773. PMID 34168328.
- **Itell et al. 2017** — *Placenta* 59(Suppl 1):S28–S35. PMID 28456432.
- **Jorba et al. 2019** — *MMWR* 68(45):1024–1028. PMID 31725706.
- **Looker et al. 2008** — *Bull World Health Organ* 86(10):805–812. PMID 18949218.
- **Nabi et al. 2021** — *Front Immunol* 12:789454. PMID 34868077.
- **Pliaka et al. 2012** — *Expert Rev Vaccines* 11(5):609–628. PMID 22827246.
- **Stanfield & Kousoulas et al. 2021** — *Viruses* 13(8):1637. PMID 34452501.
- **Sun et al. 2024** — *Vaccine X* 18:100476. PMID 38617838.
