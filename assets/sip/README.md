# SIP article sources

`distributed-systems.html` is based on Jimmy’s supplied `SIP Presentation.pdf` (78 PDF pages, including animation steps), `SIP Presentation Video Transcript - Polished.pdf` (four pages), and the current résumé. Neither complete PDF is published here. Page numbers below are **one-based PDF pages**, not the printed slide numbers.

## Matching the narration to the animation sequence

| Slide PDF pages | Transcript location | Topic and use in the article |
| --- | --- | --- |
| 1 | Page 1, introductions | Project title, team, UCSC SIP 2024, mentor Priyanka Mondal. Jimmy clarified that Mondal was then a UCSC PhD candidate advised by Prof. Owen Arden and Prof. Ioannis Demertzis. The title image spells the coauthor’s name Allison Shi; the transcript uses Alison. Use the title image’s spelling. |
| 2–10 | Page 1, Alison: Distributed Systems and Fault Tolerance | Introductory networks, cat-picture analogy, unavailability versus incorrect responses. Article explains the distinction without repeating the analogy. |
| 11–20 | Pages 1–2, replication and disagreement | Single point of failure, added replicas, conflicting responses, majority assumption. Multiple animation frames become one concise motivation. |
| 21–24 | Page 2, Amy: Choreographic Programming and HasChor | High-level abstractions; separate sends/receives versus global choreography and endpoint projection. Page 24 supplies the communication diagram. |
| 25–32 | Pages 2–3, concurrent bookseller | Separate buyer and seller programs, matching sends/receives, purchase and decline branches. |
| 33–40 | Page 3, HasChor bookseller | Located values, locally, communication, cond, optional delivery date. Four-line excerpt transcribed from page 33; the remaining frames highlight the successive operations. |
| 41–45 | Page 3, two-terminal bookseller demonstration | Same-machine execution with logging. Not represented as a multi-machine experiment. |
| 46–51 | Page 3, Jimmy: Implementing the Majority Quorum | compare: equal inputs yield their shared result; differing inputs yield failure. |
| 52–57 | Page 3, select explanation | select obtains a successful non-failure, non-timeout result. Do not invent scheduling or tie-breaking semantics. |
| 58 | Page 3, composing the quorum | All three pairs compared; nested selection combines their results. Source of the quorum diagram. |
| 59–67 | Pages 3–4, bank-balance analogy | $1,500 versus two $1,000 responses and the assumption of at most one incorrect replica. Article separates this illustrative ordering from the actual terminal inputs. |
| 68–71 | Page 4, proxies and Haskell implementation | Four participants, balance retrieval and communication, local pairwise comparisons, selection, wait, output. Comparison/selection/output excerpt transcribed from page 71. |
| 72–74 | Page 4, three recorded cases | Success with unanimous 1,000; success with inputs 1,000 / 1,500 / 1,000; failure with 1,000 / 100 / 500. Page 74 contains the complete final terminal capture. |
| 75–78 | Page 4, conclusion and acknowledgments | Team context, mentor, foundational references. No reflection section or claim of formal security verification. |

## Figure extraction

Figures are rectangular regions rendered directly from the original PDF with PyMuPDF at a scale of 3 (216 dpi). Coordinates are PDF points `(left, top, right, bottom)` on its 720 × 405 pages. Crops omit slide titles, page numbers, and unused margins; their diagram and terminal contents are unchanged. PNGs preserve the rendered pixels without generative editing.

| Asset | PDF page | Clip rectangle | Dimensions |
| --- | --- | --- | --- |
| `choreography.png` | 24 | `(125, 75, 575, 378)` | 1350 × 909 |
| `majority-quorum.png` | 58 | `(18, 105, 691, 325)` | 2019 × 660 |
| `quorum-runs.png` | 74 | `(7, 63, 714, 368)` | 2121 × 915 |

The results table transcribes the recorded bank inputs and user outputs. The illustrations and terminal outputs are historical source material, not newly executed experiments. The code blocks are accessible text transcriptions of excerpts, with surrounding declarations, imports, and setup omitted. They are not a complete runnable package. No timing, throughput, network-failure, or timeout experiment is claimed.

The references on PDF page 77 identify HasChor, FLAQR, and Priyanka Mondal’s FlameChor repository. The public FlameChor README was consulted for its HasChor repository link and the canonical FLAQR paper title; current upstream capabilities are not attributed to the student project. No current upstream program is passed off as Jimmy’s historical source code.
