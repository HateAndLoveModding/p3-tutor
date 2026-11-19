# Reservoir Sampling Resources

## Knowledge

- [Article: "Reservoir sampling" (Wikipedia)](https://en.wikipedia.org/wiki/Reservoir_sampling)
  Algorithm R with its induction proof, Algorithm L (skipping), and weighted variants (A-Res, A-ExpJ). Use for: the algorithm statements and complexity.
- [Paper: Vitter, "Random Sampling with a Reservoir", ACM TOMS 11(1), 1985 (BibSonomy record)](https://www.bibsonomy.org/bibtex/2f84bfb9fa8054f24e45dc2d4eb06cb70/ytyoun)
  The original paper; credits Algorithm R to Alan Waterman and introduces faster skipping algorithms. Use for: history and the faster variants.
- [Lecture notes: Princeton COS 493, Lecture 19](https://www.cs.princeton.edu/courses/archive/spr02/cs493/lec19.pdf)
  University notes proving that each item lands in the sample with probability k/n. Use for: the correctness proof.
- [Paper: Bitterli et al., "Spatiotemporal Reservoir Resampling for Real-Time Ray Tracing with Dynamic Direct Lighting" (NVIDIA Research)](https://research.nvidia.com/labs/rtr/publication/bitterli2020spatiotemporal)
  ReSTIR: per-pixel weighted reservoirs for choosing lights in real-time rendering. Use for: reservoir sampling in light-transport simulation.
- [Paper: "Decorrelating ReSTIR Samplers via MCMC Mutations" (arXiv 2211.00166)](https://arxiv.org/pdf/2211.00166)
  States the weighted reservoir update (replace with probability w / w_sum) as ReSTIR uses it. Use for: the weighted update rule.
- [Paper: "Weighted Reservoir Sampling With Replacement from Data Streams" (arXiv 2403.20256)](https://arxiv.org/pdf/2403.20256)
  Weighted reservoir sampling background, credits Chao (1982), notes no stream length is needed. Use for: weighted variants.

## Gaps

- No source yet on reservoir sampling specifically in discrete-event or Monte Carlo simulation output analysis.
