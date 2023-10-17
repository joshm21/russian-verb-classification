# russian-verb-classification
Classifying Russian verbs based on conjugation types

# learning tips
memorize the first and second person singular, and third person plural present/future forms. helps to identify patterns

# wiktionary classification types
| class | model       | description                                                      |
| ----- | ----------- | ---------------------------------------------------------------- |
| 1     | знать       | The easiest case. Stress is always on the stem and never shifts. |
| 2     | чувствовать | \-овать/-евать verbs                                             |
| 3     | вернуться   | \-нуть and -стичь verbs                                          |
| 4     | говорить    | \-ить verbs with type II conjugation.                            |
| 5     | видеть      | non-ить verbs that (surprisingly) have type II conjugation       |
| 6     | сказать     | \-ать/-ять verbs that (surprisingly) don't conjugate like знать. |
| 7     | вести       | \-сти/-сть/-зти/-зть verbs                                       |
| 8     | мочь        | \-чь verbs, except -стичь                                        |
| 9-16  |             | small groupings of reamining verbs                               |

# kaikki pivot table results
| COUNTA of infinitive | stress |      |      |      |             |
| -------------------- | ------ | ---- | ---- | ---- | ----------- |
| class                |        | a    | b    | c    | Grand Total |
| 1                    |        | 5025 |      |      | 5025        |
| 2                    |        | 993  | 31   |      | 1024        |
| 3                    |        | 378  | 278  | 40   | 696         |
| 4                    |        | 1039 | 1024 | 821  | 2884        |
| 5                    |        | 35   | 238  | 89   | 362         |
| 6                    |        | 157  | 160  | 199  | 516         |
| 7                    |        | 33   | 231  |      | 264         |
| 8                    |        | 15   | 113  | 7    | 135         |
| 9                    |        | 3    | 41   |      | 44          |
| 10                   |        | 3    |      | 28   | 31          |
| 11                   |        | 7    | 91   |      | 98          |
| 12                   |        | 110  | 15   |      | 125         |
| 13                   |        |      | 66   |      | 66          |
| 14                   |        | 1    | 51   | 23   | 75          |
| 15                   |        | 38   |      |      | 38          |
| 16                   |        | 2    | 30   |      | 32          |
| irreg                | 145    |      |      |      | 145         |
| Grand Total          | 145    | 7839 | 2369 | 1207 | 11560       |

# see-also
* [kaikki russian verb dump](https://kaikki.org/dictionary/Russian/pos-verb.html)
* [wiktionary russian verb classifications](https://en.wiktionary.org/wiki/Appendix:Russian_verbs)
* reddit threads
  * [https://www.reddit.com/r/russian/comments/w60f9u/verb_conjugation/]
  * [https://www.reddit.com/r/russian/comments/115yfnr/a_complete_classification_of_the_top_3000_russian/]
