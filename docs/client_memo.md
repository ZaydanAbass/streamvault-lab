# Memo to Kwame

**From:** Zaydan
**Date:** October 31, 2026
**Subject:** Licensing Recommendation: Franchise Bundles vs. Standalone Hits

## What I found
The board's choice between franchise bundles and standalone hits is not a coin flip. The data shows franchise bundles are consistently safer, with a higher median return and a much higher floor. 

The fear of buying a bundle is that you overpay for weak middle entries. The data proves this fear is overblown for our top target. We define ROI as profit as a multiple of production budget. While the typical franchise bundle returns 4.63x (against 4.00x for standalones), our top target—*The Lord of the Rings*—returns a combined 10.0x. More importantly, even the weakest film in the LOTR bundle returns 8.37x, whereas the next-best bundle (Ice Age) has a weakest film returning only 5.50x. The picture holds up if we only look at the 2000-onward window: bundles still outperform (4.08x vs. 3.49x), and LOTR still leads.

## What I built
A fully automated data pipeline that extracts, cleans, and analyzes candidate films, dynamically calculating ROIs and flagging franchise bundles.

| What you asked for | Status | Evidence |
| :--- | :--- | :--- |
| A defensible recommendation | **Complete** | Bundles win in both windows (4.53x vs 4.00x all years; 4.05x vs 3.49x post-2000). |
| A shortlist to negotiate from | **Complete** | Top bundles: LOTR, Ice Age, Avengers. Top recent standalones: Spirited Away, The Incredibles, Inception. |
| A read on talent leverage | **Complete** | Directors are the stronger signal; Christopher Nolan is a top reliable indicator in the 2000-onward window. |
| Deal note for strongest candidate | **Complete** | LOTR targeted with a proposed walk-away point anchored at 8.37x. |
| Transparency on limits | **Complete** | See "What I could not stand behind" below. |

## What I recommend
Go to the board and recommend securing **The Lord of the Rings collection**. 

Because the weakest film in the bundle returns 8.37x, we should anchor our walk-away price to that **8.37x multiple**. We should pay a premium over the typical bundle (4.63x), but we should not pay above 8.37x. At that price, a weaker middle entry drags the whole bundle below the safety of our typical standalone return. 

If the board prefers standalones, focus your leverage on the 2000-onward hits: *Spirited Away* (13.47x), *The Incredibles* (5.86x), *Inception* (4.24x), *The Smurfs* (4.12x), and *Monsters, Inc.* (4.00x). 

## What I could not stand behind
You should know the limits of this evidence before you walk into the room:
1. **Box Office vs. Streaming Value:** Our ROI is based on theatrical box office vs. production budget, not the actual licensing revenue a title will generate on StreamVault.
2. **Math Caveat:** Bundle figures combine the money of all films, while standalone figures are per film, so they are not a strictly perfect like-for-like comparison.
3. **Missing Data:** 15 of the original 127 lines were dropped (1 blank, 6 duplicates, 1 bad text, 1 invalid, 1 hidden IMDb duplicate, 5 API 404s). We analyzed 112 films.
4. **Bundle Size:** Our data shows 3 films for the LOTR collection. If the studio's actual bundle contains more than 3, the math changes.