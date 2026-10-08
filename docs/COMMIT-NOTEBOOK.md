# Commit notebook

Commit bodies of 30 lines or more, exported once on 2026-10-07 from the
history of `outlier-resilience-web`, newest first. Before the lab's commit convention these bodies
held the working notes: measurements, defects found and the reasoning behind a change.
They are copied here so they can be searched and cited. The commits themselves are
unchanged; `git show <hash>` returns the original.

| Date | Commit | Subject |
|---|---|---|
| 2026-09-10 | [`a44d293`](#a44d293) | Make the mark the O of the wordmark, and clear the copy of AI tells |

<a id="a44d293"></a>
## 2026-09-10 `a44d293` Make the mark the O of the wordmark, and clear the copy of AI tells

Author: Zach Asher. Full hash: `a44d2930a13c9bb8aed8d336df8bbadb3c60bfc8`.

The old mark set a point one unit away from a closed ring, so the two
shapes fused. At small size it read as the Mars symbol. The green favicon
tile read as the Instagram glyph. The horizontal lockup then put that ring
beside the typeface O, so the eye read "O OutRes".

The ring now replaces the letter O. It carries a gap where the point
escaped, and that gap also breaks both misreadings. Green marks the point
and the word "Res", so the point reads as intent and not as a speck.

Logo:

- Retire the horizontal lockup. The wordmark is the primary logo.
- Rebuild the favicon as a dark tile with a green ring. It holds at 16 px
  on a light tab bar and on a dark one.
- Bake the colors into the shipped SVGs. currentColor does not cross an
  <img> boundary, so the old logo-mark.svg rendered black on black. Only
  the -mono files keep currentColor.
- Add tools/build-assets.py. The SVGs are generated, so edit the script.

Copy:

- Remove all 12 em dashes, including the ones in the title and the social
  card.
- Reduce the "not X, but Y" construction from five uses to three. The
  three that remain carry the argument.
- Drop the intensifier in "simply insufficient". Replace the unclear
  "Which sets the bar:".
- Even up the figures row. The third label ran to two lines on its own.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01KYF6H8aFsV2YteBnZgoDUR

