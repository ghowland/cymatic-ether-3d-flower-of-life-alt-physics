# Zenodo Publication Checklist

## Pre-Publication Steps

### 1. Complete Manuscript
- [ ] Full manuscript written (manuscript.md)
- [ ] All equations verified
- [ ] All references cited
- [ ] Figures created and captioned
- [ ] Supplementary materials prepared
- [ ] Abstract finalized (<300 words)
- [ ] Keywords selected (10-15)

### 2. Metadata Preparation
- [ ] .zenodo.json file created
- [ ] Author information added (name, affiliation, ORCID)
- [ ] Title finalized
- [ ] Description written
- [ ] Keywords listed
- [ ] License selected (CC-BY-4.0)
- [ ] Related identifiers added (GitHub, etc.)

### 3. Code and Data
- [ ] simulation.py tested and working
- [ ] Code comments complete
- [ ] Requirements documented (Python 3.7+, NumPy)
- [ ] Sample outputs included
- [ ] Analysis scripts provided

### 4. Documentation
- [ ] README.md complete
- [ ] CHANGELOG.md up to date
- [ ] LICENSE file included
- [ ] Experimental protocols documented
- [ ] FAQ section written

### 5. Quality Checks
- [ ] All links working
- [ ] All files properly named
- [ ] Directory structure logical
- [ ] File sizes reasonable (<100MB total)
- [ ] No sensitive information included

### 6. Legal/Ethical
- [ ] Copyright cleared
- [ ] Co-author approval (if applicable)
- [ ] Data usage rights confirmed
- [ ] Ethics statement (if applicable)

## Publication Process

### 1. Create Zenodo Account
- [ ] Register at zenodo.org
- [ ] Link ORCID
- [ ] Complete profile

### 2. Upload Files
**Via Web Interface**:
- [ ] Go to zenodo.org/deposit/new
- [ ] Upload all files
- [ ] Add metadata (auto-populated from .zenodo.json)
- [ ] Preview deposit

**Via GitHub Integration** (Alternative):
- [ ] Create GitHub repository
- [ ] Enable Zenodo integration
- [ ] Create GitHub release
- [ ] Zenodo auto-archives

### 3. Metadata Entry
- [ ] Title
- [ ] Authors (with affiliations)
- [ ] Description
- [ ] Publication date
- [ ] Version
- [ ] License
- [ ] Keywords
- [ ] Related identifiers
- [ ] Communities (optional)

### 4. Pre-publish Review
- [ ] Preview record
- [ ] Check all links
- [ ] Verify metadata accuracy
- [ ] Test file downloads
- [ ] Proofread description

### 5. Publish
- [ ] Click "Publish" button
- [ ] **Note**: Cannot be deleted after this (only new versions)
- [ ] Receive DOI
- [ ] Save DOI for citations

## Post-Publication

### 1. Immediate Actions
- [ ] Copy DOI and add to all documents
- [ ] Update GitHub README with DOI badge
- [ ] Share on social media (Twitter, LinkedIn)
- [ ] Post to relevant forums (Physics Stack Exchange, r/Physics)
- [ ] Email to interested colleagues

### 2. Promotion
- [ ] Submit to arXiv (if applicable - check policy)
- [ ] Post on ResearchGate
- [ ] Add to Google Scholar profile
- [ ] List on personal website
- [ ] Submit preprint announcement to mailing lists

### 3. Community Engagement
- [ ] Monitor Zenodo page for views/downloads
- [ ] Respond to comments/questions
- [ ] Update GitHub repository with DOI
- [ ] Create discussion forum (GitHub Discussions)
- [ ] Set up email alerts for citations

### 4. Version Management
- [ ] Plan for version updates
- [ ] Document changelog
- [ ] Re-upload new versions as needed
- [ ] Update DOI references

## Files to Include in Upload

### Core Documents (Required)
```
✓ manuscript.md (or manuscript.pdf)
✓ README.md
✓ LICENSE
✓ .zenodo.json
✓ simulation.py
✓ CHANGELOG.md
```

### Supplementary Materials (Recommended)
```
✓ supplementary/experimental_protocols.md
✓ supplementary/mathematical_derivations.pdf
✓ supplementary/comparison_table.xlsx
✓ supplementary/flatland_comparison.md
```

### Optional (If Available)
```
○ figures/ (all visualizations)
○ data/ (simulation outputs)
○ code/ (analysis scripts)
○ videos/ (animations)
```

## File Naming Conventions

- Use lowercase
- Use underscores (not spaces)
- Be descriptive
- Include version if applicable

Examples:
- `manuscript_v5.0.pdf`
- `simulation_bubble_substrate.py`
- `figure_01_lattice_structure.png`
- `data_coherence_evolution.csv`

## Recommended File Organization

```
zenodo_package/
├── manuscript.pdf                    # Main paper
├── README.md                         # Package overview
├── LICENSE                          # CC-BY-4.0
├── CHANGELOG.md                     # Version history
├── .zenodo.json                     # Metadata
├── simulation.py                    # Working code
├── requirements.txt                 # Python dependencies
├── figures/
│   ├── fig01_bubble_lattice.png
│   ├── fig02_phase_evolution.png
│   └── fig03_dark_energy.png
├── supplementary/
│   ├── experimental_protocols.md
│   ├── mathematical_derivations.pdf
│   ├── comparison_table.xlsx
│   └── flatland_comparison.md
└── code/
    ├── plot_results.py
    ├── compute_g_factor.py
    └── measure_coherence.py
```

## Size Limits

- Individual file: 50 GB max
- Total upload: 50 GB max (contact Zenodo for larger)
- Recommended: Keep under 1 GB for faster downloads

## License Recommendation

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)
- ✓ Allows commercial use
- ✓ Allows modifications
- ✓ Allows distribution
- ✓ Requires attribution
- ✓ Compatible with open science

## Communities to Join

Consider submitting to these Zenodo communities:
- General Physics
- Quantum Gravity
- Cosmology
- Alternative Physics
- Computational Physics
- Open Science

## DOI Badge

After publication, add this to your README:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

Replace XXXXXXX with your actual DOI number.

## Citation Format

Provide this in your README:

**APA**:
```
[Your Name]. (2026). Unified Field Theory via Discrete Cymatic Substrate (Version 5.0). Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

**BibTeX**:
```bibtex
@misc{cymatic_substrate_2026,
  author = {[Your Name]},
  title = {Unified Field Theory via Discrete Cymatic Substrate},
  year = {2026},
  publisher = {Zenodo},
  version = {5.0},
  doi = {10.5281/zenodo.XXXXXXX},
  url = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

## Troubleshooting

**Upload fails**:
- Check file size limits
- Verify internet connection
- Try smaller batches
- Use Zenodo API for large uploads

**Metadata not displaying**:
- Validate .zenodo.json syntax
- Check character encoding (UTF-8)
- Remove special characters

**DOI not working**:
- Wait 24 hours for propagation
- Clear browser cache
- Contact Zenodo support

## Support

- Zenodo documentation: https://help.zenodo.org
- Email support: info@zenodo.org
- Community forum: https://github.com/zenodo/zenodo/discussions

## Final Checklist Before Publishing

Ask yourself:
1. Is the manuscript ready for permanent archiving?
2. Are all co-authors aware and approving?
3. Have I double-checked all metadata?
4. Is the license appropriate?
5. Do I have all necessary rights?
6. **Am I ready for this to be permanent?**

Once published on Zenodo:
- ✓ Permanent (cannot be deleted)
- ✓ Citable (has DOI)
- ✓ Discoverable (indexed)
- ✓ Preserved (long-term)
- ✗ Cannot be un-published (only new versions)

---

**Ready to publish?** Double-check everything, then proceed!

**Questions?** Contact: [your email]

**Last updated**: February 2026
